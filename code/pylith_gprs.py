from parse_vtk import parse_vtk
import numpy as np
import os


class pylith_gprs:
   '''
   Driver class for Pylith GPRS model
   '''
   def __init__(self):

       self.num_p = 7
       start_q = 100.0
       end_q = 400.0
       self.p_ = np.linspace(start_q,end_q,self.num_p)

       self.num_tsteps = 112
       self.t_ = np.linspace(1,self.num_tsteps,self.num_tsteps)

       self.window = 28 # make sure num_tsteps is exact multiple of window!!!
       self.stride = self.window
       self.num_features = 2


   def time_series(self):

       num_p = self.num_p
       p_ = self.p_
       t_ = self.t_
       num_tsteps = self.num_tsteps
       num_features = self.num_features
       num_features = self.num_features

       t_appended =  np.zeros((num_p*num_tsteps,num_features))
       u_appended =  np.zeros((num_p*num_tsteps,num_features))
       ux_appended =  np.zeros((num_p*num_tsteps,num_features))
       uy_appended = np.zeros((num_p*num_tsteps,num_features))
       
       u, ux, uy = np.zeros((num_tsteps,2)), np.zeros((num_tsteps,2)), np.zeros((num_tsteps,2))
       count_q = 0
       for rate in p_:
          directory = './vtk_plots' + '/%s' % int(rate)
          count_ = 0
          for file_name in sorted(os.listdir(directory)):
              filename = os.path.join(directory, file_name)
              if os.path.isfile(filename):
                  parser = parse_vtk(filename)
                  u[count_,0], ux[count_,0], uy[count_,0] = parser.get_surface_information("displacement")
                  u[count_,1] = u[count_,0]
                  ux[count_,1] = ux[count_,0]
                  uy[count_,1] = uy[count_,0]
                  count_ += 1

          u_ = u.reshape(-1,num_features)
          ux_ = ux.reshape(-1,num_features)
          uy_ = uy.reshape(-1,num_features)
          start_ = count_q*num_tsteps
          end_ = start_ + num_tsteps
          t_appended[start_:end_,0] = t_[:]
          t_appended[start_:end_,1] = rate
          u_appended[start_:end_,0] = u_[:,0]
          u_appended[start_:end_,0] = u_[:,0]
          ux_appended[start_:end_,1] = ux_[:,1]
          ux_appended[start_:end_,1] = ux_[:,1]
          uy_appended[start_:end_,0] = uy_[:,0]
          uy_appended[start_:end_,1] = uy_[:,1]
          count_q += 1
   
       # save objects!!! 
       my_file = Path(os.getcwd()+'/u_appended.pickle')
       if not my_file.is_file():
          save_object(u_appended,"u_appended.pickle")
   
       return t_appended, u_appended, ux_appended, uy_appended


   def plot_results(self,lstm_model, T_, X_, Y_, stride, window, dataset_type, objective, num_samples, num_p, p_, num_tsteps):
     '''
     plot examples of the lstm encoder-decoder evaluated on the training/test data
     
     '''
   
     Y_return = np.zeros([int(num_samples*window)])     
     count_q = 0
     for q in p_:
   
         X = np.zeros([int(num_samples*window/num_p)]) 
         Y = np.zeros([int(num_samples*window/num_p)])     
         T = np.zeros([int(num_samples*window/num_p)])     
   
         num_samples_per_q = int(num_samples/num_p) 
   
         for ii in range(num_samples_per_q):
   
             start = ii*stride
             end = start + window
   
             train_plt = X_[:, count_q*num_samples_per_q+ii, :]
             Y_train_pred = lstm_model.predict(torch.from_numpy(train_plt).type(torch.Tensor), target_len = window)
   
             X[start:end] = Y_[:, count_q*num_samples_per_q+ii, 0]
             Y[start:end] = Y_train_pred[:, 0]
             T[start:end] = T_[:, count_q*num_samples_per_q+ii, 0]
             Y_return[count_q*num_tsteps+start:count_q*num_tsteps+end] = Y_train_pred[:, 0]
   
         plt.figure()
         plt.plot(T, X, '-', color = (0.2, 0.42, 0.72), linewidth = 1.0, markersize = 1.0, label = 'Target')
         plt.plot(T, Y, '-', color = (0.76, 0.01, 0.01), linewidth = 1.0, markersize = 1.0, label = '%s' % objective)
         plt.xlabel('Time stamp')
         plt.ylabel('Disp X $(m)$')
         plt.legend(frameon=False)
         plt.suptitle('%s data set for q=%s MSCF/day' % (dataset_type,q), x = 0.445, y = 1.)
         plt.tight_layout()
         plt.savefig('plots/%s_%s.png' % (q,dataset_type))
   
         count_q += 1
   
         del X,Y,T
   
   
