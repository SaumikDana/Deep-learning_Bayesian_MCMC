from rsf import rsf
import numpy as np
from MCMC import MCMC
import sys
import matplotlib.pyplot as plt


import generate_dataset
import lstm_encoder_decoder
import plotting_time_series 


import pickle


def save_object(obj,filename):
    try:
        with open(filename, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


def main(problem):

    if problem == 'rsf':
       problem_ = rsf()
       t_appended, acc_appended, acc_appended_noise = problem_.time_series() 
    
    num_features = problem_.num_features
    window = problem_.window
    stride = problem_.stride
    num_dc = problem_.num_dc
    num_tsteps = problem_.num_tsteps
    dc_ = problem_.dc_

    t_ = t_appended.reshape(-1,num_features); acc_ = acc_appended.reshape(-1,num_features)
    num_samples_train, Ttrain, Ytrain = generate_dataset.windowed_dataset(t_, acc_, window, stride, num_features) 
    T_train, Y_train = generate_dataset.numpy_to_torch(Ttrain, Ytrain)
    
    #----------------------------------------------------------------------------------------------------------------
    # LSTM encoder-decoder!!!
    hidden_size = window; batch_size = 1; n_epochs = int(sys.argv[1]); num_layers = 1 
    input_tensor = T_train
    model_lstm = lstm_encoder_decoder.lstm_seq2seq(input_size = input_tensor.shape[2], hidden_size = hidden_size, num_layers = num_layers, bidirectional = False)
    loss = model_lstm.train_model(input_tensor, Y_train, n_epochs = n_epochs, target_len = window, batch_size = batch_size, training_prediction = 'mixed_teacher_forcing', teacher_forcing_ratio = 0.6, learning_rate = 0.01, dynamic_tf = False)
    plotting_time_series.plot_train_test_results(model_lstm, Ttrain, Ttrain, Ytrain, stride, window, 'Training', 'Reconstruction', num_samples_train, num_dc, dc_, num_tsteps)

#    #----------------------------------------------------------------------------------------------------------------
#    # save objects!!!
#
#    save_object(model_lstm,"model_lstm.pickle") 
#    save_object(acc_appended_noise,"acc_appended_noise.pickle")
#
#    #----------------------------------------------------------------------------------------------------------------
#    # Bayesian comparison
#    
#    # load objects!!!
#    model_lstm = load_object("model_lstm.pickle")  # ROM
#    acc_appended_noise = load_object("acc_appended_noise.pickle") # noisy data
#    # load objects!!!
#
#    for ii in range(0,num_dc):
#
#        if ii == 2 or ii == 11 or ii == 13 or ii == 15 or ii == 16 or ii == 17:
#           # noisy data!!!
#           acc = acc_appended_noise[ii*num_tsteps:ii*num_tsteps+num_tsteps,0]
#           acc = acc.reshape(1, num_tsteps)
#     
#           dc = dc_[ii]
#           print('--- dc is %s ---' % dc)
#
#           qstart={"Dc":100} # initial guess
#           qpriors={"Dc":["Uniform",0.1, 1000]}
#
#           nsamples = int(sys.argv[2])
#           nburn = nsamples/2
#           
#           problem_type = 'full'
#           MCMCobj1=MCMC(model,qpriors=qpriors,nsamples=nsamples,nburn=nburn,data=acc,problem_type=problem_type,lstm_model=model_lstm,qstart=qstart,adapt_interval=10,verbose=True)
#           qparams1=MCMCobj1.sample() # run the Bayesian/MCMC algorithm
#           std_MCMC1 = MCMCobj1.std2
#           MCMCobj1.plot_dist(qparams1,'full',dc)
#
#           problem_type = 'rom'
#           MCMCobj2=MCMC(model,qpriors=qpriors,nsamples=nsamples,nburn=nburn,data=acc,problem_type=problem_type,lstm_model=model_lstm,qstart=qstart,adapt_interval=10,verbose=True)
#           qparams2=MCMCobj2.sample() # run the Bayesian/MCMC algorithm
#           std_MCMC2 = MCMCobj2.std2
#           MCMCobj2.plot_dist(qparams2,'reduced order',dc)
#
    #----------------------------------------------------------------------------------------------------------------
    # Close it out
    plt.show()
    plt.close('all')

if __name__ == '__main__':

    problem = 'rsf'
    main(problem)




