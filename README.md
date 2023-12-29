# Bayesian MCMC in Rate State Models

## Directory Structure
```
Bayesian_MCMC_Deep-Learning/
│
├── .github/ - Contains GitHub Actions workflow files.
│   └── workflows/
│       └── python-app.yml - Configuration for Python application workflow.
│
├── .vscode/ - Contains settings for Visual Studio Code.
│   ├── launch.json - Debugging configurations.
│   ├── settings.json - VSCode settings.
│   └── tasks.json - Task configurations for VSCode.
│
├── source_c++/ - C++ source files for MCMC and deep learning inference.
│   ├── MCMC.cpp - Markov Chain Monte Carlo implementation.
│   ├── MCMC.h
│   ├── RateStateModel.cpp - Rate state models for simulations.
│   ├── RateStateModel.h
│   └── dl_inference.cpp - Deep learning inference related scripts.
│
├── source_python/ - Python scripts for MCMC, deep learning, and utilities.
│   ├── MCMC.py - Markov Chain Monte Carlo implementation in Python.
│   ├── RSF.py - Related to rate state functions or models.
│   ├── RateStateModel.py - Python implementation of rate state models.
│   ├── __init__.py - Initializes the Python package.
│   ├── __pycache__/ - Compiled Python files for faster loading.
│   ├── dl_inference.py - Scripts for deep learning inference.
│   ├── lstm/ - Contains LSTM related models and utilities.
│   │   ├── lstm_encoder_decoder.py
│   │   └── utils.py
│   ├── tests/ - Test scripts for MCMC and other functionalities.
│   │   ├── __init__.py
│   │   ├── test_mcmc.py
│   │   └── test_rsf.py
│   └── utils/ - Utility scripts for operations like JSON and MySQL interactions.
│       ├── json_save_load.py
│       └── mysql_save_load.py
│
├── .DS_Store - A file used by macOS to store custom attributes of a folder.
├── README.md - The repository's readme file with an overview and instructions.
├── __init__.py - An initialization script for Python packages.
└── requirements.txt - Lists the Python dependencies for the project.
```

## Introduction

![bayesmcmc](https://github.com/SaumikDana/Bayesian-Markov-chain-Monte-Carlo/assets/9474631/f755e7ea-3ee5-4684-8337-55454f8a7d76)

![mcmc_target](https://github.com/SaumikDana/Bayesian-Markov-chain-Monte-Carlo/assets/9474631/94ba3448-e8fe-42d0-8200-11dd06aed8d0)


## Adaptive Metropolis Algorithm in a nutshell

<img width="870" alt="Screen Shot 2023-12-29 at 5 07 41 PM" src="https://github.com/SaumikDana/Bayesian-Markov-chain-Monte-Carlo/assets/9474631/6b2445ef-5eca-41d0-8136-9d4be5fc7c2d">


## Running the Source code Directly
### Python Version
1. Install dependencies.
2. Run Script: `python3 -m source_python.dl_inference`

### C++ Version
1. Install dependencies (boost, gsl, eigen)
2. Navigate to source_c++ folder
3. Compile: `g++ -std=c++17 -o executable dl_inference.cpp RateStateModel.cpp MCMC.cpp [...]`
4. Run executable

### Features
- Rate State Model Initialization with customizable parameters.
- Time Series Generation and Bayesian Inference using MCMC.
- Visualization with `matplotlib`.

## Paper Summary
Based on "Arriving at estimates of a rate and state fault friction model parameter using Bayesian inference and Markov chain Monte Carlo", https://www.sciencedirect.com/science/article/pii/S266654412200003X

## Contact
For support or collaboration: dana.spk5@gmail.com

---
Copyright © [Saumik Dana]
---
