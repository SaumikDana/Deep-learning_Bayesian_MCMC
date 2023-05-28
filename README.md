# Python version

dl_inference is a Python script that implements a Rate State model and performs Bayesian inference on the generated time series. It utilizes the `rsf` module and `matplotlib` library.

A paper which gives the modeling framework is https://www.sciencedirect.com/science/article/pii/S266654412200003X

<img width="684" alt="Screen Shot 2023-05-28 at 5 12 24 PM" src="https://github.com/SaumikDana/Bayesian_MCMC_Deep-Learning/assets/9474631/b35e4ed4-85c8-455a-92d8-6f002400f117">

And here is Google Bard summarizing it:

## Summary of the Paper

The paper proposes a Bayesian inference framework for estimating the critical slip distance (CSD) parameter in the rate and state (RS) fault friction model. The RS model is a widely used model for describing the frictional behavior of faults. The CSD parameter is a key parameter in the RS model, and its value can vary widely depending on the fault properties and the loading conditions.

The Bayesian inference framework uses Markov chain Monte Carlo (MCMC) methods to sample from the posterior distribution of the CSD parameter. The posterior distribution is obtained by combining the prior distribution of the CSD parameter with the likelihood function, which is a function of the observed data.

The authors evaluated the performance of the Bayesian inference framework using synthetic data. The synthetic data was generated using the RS model with different values of the CSD parameter. The Bayesian inference framework was able to accurately estimate the CSD parameter from the synthetic data.

The authors also applied the Bayesian inference framework to real data from the Parkfield earthquake sequence. The Parkfield earthquake sequence is a well-studied sequence of earthquakes that occurred in California. The authors were able to estimate the CSD parameter from the real data, and their results were consistent with previous studies.

The Bayesian inference framework proposed in the paper is a promising new method for estimating the CSD parameter in the RS fault friction model. The framework is able to accurately estimate the CSD parameter from both synthetic and real data. The framework can be used to improve our understanding of fault behavior and to predict the likelihood of future earthquakes.

### Key Takeaways:

- Bayesian inference is a powerful tool for estimating parameters in complex models.
- Markov chain Monte Carlo methods can be used to efficiently sample from the posterior distribution of a parameter.
- The Bayesian inference framework proposed in the paper can be used to accurately estimate the CSD parameter in the RS fault friction model.
- The framework can be used to improve our understanding of fault behavior and to predict the likelihood of future earthquakes.


A version that uses deep learning to generate a reduced order Rate State model is under development.

## Prerequisites
- Python 3.x
- `rsf` module
- `matplotlib` library

## Usage
1. Install the required dependencies.
2. Run the script using a Python interpreter.
    ```shell
    python dl_inference.py
    ```

## Description
The code performs the following steps:

1. Initializes the Rate State model with the specified parameters: `number_slip_values`, `lowest_slip_value`, `largest_slip_value`, and `plotfigs` (for plotting figures).
2. Generates the time series for the Rate State model.
3. Sets the starting value for the parameter `qstart`.
4. Defines the prior distribution for the parameter `qstart` using the "Uniform" distribution with bounds [0, 10000].
5. Performs Bayesian inference by calling the `inference` method with `nsamples=500`.
6. Displays the generated figures using `matplotlib`.
7. Closes all open figures.

## Customization
- You can modify the parameters `number_slip_values`, `lowest_slip_value`, `largest_slip_value`, and `plotfigs` to fit your specific needs.
- Adjust the `qstart` parameter and its prior distribution to tailor the Bayesian inference.
- Modify the `nsamples` parameter in the `inference` method to control the number of samples used in the inference process.

# C++ version

```
g++ -std=c++17 -o executable dl_inference.cpp fileIO.cpp RateStateModel.cpp MCMC.cpp -I/opt/homebrew/Cellar/boost/1.81.0_1/include -I/opt/homebrew/Cellar/gsl/2.7.1/include -I/opt/homebrew/Cellar/eigen/3.4.0_1/include/eigen3 -L/opt/homebrew/Cellar/boost/1.81.0_1/lib -lboost_iostreams -L/opt/homebrew/Cellar/gsl/2.7.1/lib -lgsl -lgslcblas -lm
```

## Contact
dana.spk5@gmail.com
