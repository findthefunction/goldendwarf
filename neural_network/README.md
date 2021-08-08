# Prophet

Developed by Facebook Open Source to provide rapid model fitting and does not require data pre-processing 
Prophet uses Stan to fit models; a platform for statistical modeling and high-performance statistical computation.

After test several iterations of models, we selected Prophet due to is ability to process and sample data automatically with the Stan backend.
This gave several advantage for our live dashboard; speed and efficiency is key. Regardless of how well a model works on time series data, the results are rendered
ineffective if the predictions are old.  Prophet enabled us to establish an advantage in conjunction with technical analysis and produce functional result within the target 
timeframe.

![prediction_sample](https://user-images.githubusercontent.com/31022640/128647236-ef162c6f-d3dc-4fd9-b61d-b86f261b4af1.png)

Utilizing closing price and volume data we are able to produce results that have generated short term alpha.
The model takes in 500 minutes (1 minute intervals) and generates a prediction for selected period.
The accuracy was reduced beyond 30 minutes, with 15 minutes being optimal for generating tradable insight.
Automatic changepoint detection, by defining a large number of potential changepoints.

## Prophet breakdown

### Markov chain Monte Carlo

Markov chain Monte Carlo (MCMC) are a class of algorithms for sampling from a probability distribution.
Provides the probabilities of occurrence of different possible outcomes.
creates samples from a continuous random variable, with probability density proportional to a known function.

### Penalized Maximum Likelihood

Limited memory Broyden–Fletcher–Goldfarb–Shanno (BFGS) algorithm is an iterative method for solving unconstrained nonlinear optimization problems
Penalized maximum likelihood estimation with optimization (L-BFGS)
  - Uses an estimate of the inverse Hessian matrix to steer its search through variable space
  - L-BFGS stores only a few vectors that represent the approximation implicitly
  - Effective at parameter estimation
 
### Automatic Differentiation Variational Inference

Approximate Bayesian inference with variational inference (ADVI)
Stan implements an automatic variational inference algorithm, called Automatic Differentiation Variational Inference (ADVI).
It searches over a family of simple densities to find the best approximate posterior density derived from previous data.

Prophet represents a new wave of machine learning, many other large tech companies are creating accessible models they have developed.  
By handling preprocessing and splitting automatically and utilizing pacjages written in task specific languages the models are optimized 
and can produce results quickly and consistently.  This reduces the number of moving parts required to produce predictions, eliminating steps
that could introduce complications. Prophet handles missing values and outliers automatically.

## Bi-Direction Neural Network

We developed a functional RNN that was able to gain desirably high accuracy scores. 

![image](https://user-images.githubusercontent.com/31022640/128648041-335e2bca-e386-421c-b994-fe70f62df44c.png)

The limits of this model came down to time and processing data.
In order to input data into the RNN the data needed to be processed, split and balanced which typically took 15-20 seconds depending on the size of dataset.
Preprocessing the data then gave us a dataset that was not directly interpretable quickly.  

![image](https://user-images.githubusercontent.com/31022640/128648112-055e516b-6304-4194-ba80-6325435358d0.png)

Once the model was run the data needed to be interpreted again to integrate it into 
the dashboard and presented in a format that could be utilized for real time trading actions.  


Future iterations of the buy/ sell signal generation capability of project Goldendwarf will include newly available auto-regressive recursive neural network from DEEPar,
This is a project that has been developed by Amazon.  The options for this project are limitless and due to the earth rotation in our solar system we elected to present our
proof of concept model using prophet with the intent to add various capabilities. Provide a robust single source platform to gain insight and alpha 
from the comfort of a desktop computer.

Feel free to explore the project, download the files and if you have curiousities or contributions let us know.







