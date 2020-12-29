*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Train and deploy machine learning model using Microsoft Azure Machine learning 

*TODO:* Write a short introduction to your project.
In this project, 
- We train and deploy machine learning model to predict survival on Titanic using Microsoft Azure Machine Learning.
- We compare performance of model trained using Azure Hyperdrive and Azure AutoML 
- We pick the best model among them, deploy it as REST endpoint and consume the endpoint

Here is the workflow:  
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/capstone-diagram.png)

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.
Clone this repository, and run the individual notebooks on Microsoft Azure compute instance.


## Dataset

### Overview
*TODO*: Explain about the data you are using and where you got it from.  

In this project, we will be working on Titanic survival dataset from Kaggle (https://www.kaggle.com/c/titanic/data).

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.  

It consists of details of 891 people on Titanic. This includes 11 attributes for each person and whether they survived the distaster or not.
We build a binary classification machine learning model to predict the survival based on the person's attibutes.

### Access
*TODO*: Explain how you are accessing the data in your workspace.  

The CSV file is attached to this repository. We access it directly by passing its URI to Python SDK Dataset.Tabular.from_delimited_files() method 


## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment  

Azure Auto ML (Automated machine learning) tries different models and algorithms during the automation and tuning process. There is no need for user to specify the algorithm. It supports various classificaion models e.g.: RandomForest, LightGBM, XGBoostClassifier, LogisticRegression, etc.  
Ref: https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-auto-train

- We optimize for "accuracy", so its set as the primary metric.
- We allow for automated featurization like feature scaling etc. that AutoML supports out of the box.
- We enable early stopping for computational efficiency.
- We set a few settings like experiment/iteration timeout minutes due to time limitations of project's VM.
- Number of concurrent iterations is set to be equal to the maximum number of nodes provisioned.

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?  

- The final high performing model from AutoML was VotingEnsemble, with an accuracy of 0.7407.  
  It is an ensemble of many child run models (mentioned above) with soft-voting (i.e. weighted averages of their predictions).  
- Some of the parameters if the model from AutoML model, including voting weights are:
  - Standardscalerwrapper followed by LightGBMClassifier(boosting_type='goss',class_weight=None, colsample_bytree=0.3966666666666666, num_leaves=31,
                                                                               objective=None, random_state=None, reg_alpha=0.0, reg_lambda=0.0, silent=True,
                                                                               subsample=1.0, subsample_for_bin=200000, subsample_freq=0)
  - weights = [0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 0.2222222222222222, 0.1111111111111111, 0.1111111111111111]

- To improve the model: 
  - We can train AutoML longer by relaxing the experiment/iteration timeout setting.
  - We can also perform better Feature engineering by setting better values for the missing data, and also extract relevant features from existing features.


*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

- RunDetails widget:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/automl-1.png)


- ML studio showing the algorithms AutoML tried:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/automl-2.png)


- Best AutoML model with its run id:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/automl-3.png)


- Some parameters of best AutoML model:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/automl-4.png)



## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search

We use Logistic regression, which is a linear classification model. We chose it for its simplicity, which makes it a good starting point for ML modeling.
We use Azure Hyperdrive to tune the model's hyperparameters:
- Hyperparameters:
  - The inverse of regularization strength (C). Smaller values of C implies more regularization and less model overfitting to training dataset. More values between 0.1 & 1.0 and fewer values less than 0.1 and greater than 1.0 were chosen
  - Max number of iterations (max_iter) allowed for solver convergence during model training. Few values greater than default setting of 100 were chosen.
- Early Termination policy:
  - Bandit policy terminates any run that doesn't fall within the slack factor or slack amount of the evaluation metric with respect to the best performing run.
  - It therefore increase the computational efficiency of training.
- Sampling policy:
  - Random sampling policy is chosen & a total of 15 runs from 30 total possible combinations of hyperparameters will be chosen & run by Hyperdrive.  
  
Refs:   
https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression  
https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.hyperdrive.randomparametersampling?preserve-view=true&view=azure-ml-py  
https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.hyperdrive.banditpolicy?preserve-view=true&view=azure-ml-py#&preserve-view=truedefinition

### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

- The final high performing model from Hyperdrive has an accuracy of 0.7578.  
- The hyperparameters for this model are C=0.1 and max_iter=200
- To improve the model:
    - We can increase the maximum number of runs per experiment to allow searching more hyperparameters
    - We can try other sampling policies like Bayesian, so that the hyperparameter search is not completely random
    - We can perform more fine-grained hyperparameter search around this C=0.1. 
    - We can also perform better Feature engineering by setting better values for the missing data, and also extract relevant features from existing features.
    - We can use 5 fold cross validation like AutoML, instead of a single validation set.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

- RunDetails widget:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/hd-1.png)


- ML studio showing different hyperparameters that Hyperdrive tried:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/hd-2.png)


- Best Hyperdrive model with its run id:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/hd-3.png)


- Hyperparameters of best Hyperdrive model:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/hd-4.png)


## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

Since the best Hyperdrive model (accuracy: 0.7578) performs better than the best AutoML model (accuracy: 0.7407), we register and deploy this model as shown below.
We get an active REST endpoint for this model. 

- Best Hyperdrive model registered:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/hd-d-1.png)


- Best Hyperdrive model deployed:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/hd-d-2.png)


- ML studio showing the deployed Hyperdrive model and its REST endpoint:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/hd-d-3.png)


In order to query the endpoint and run inference on it, we pass sample inputs in JSON format to score.py.
score.py runs inference using saved model and returns a response. Here is an example query script:
```
import requests
import json

# URL for the web service, should be similar to:
scoring_uri = 'http://f8d1e41d-c5d4-4c94-9e2d-28b0a90d2f61.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'OcpXMJyELqbmAcJggQqegBSyeWacPxCA'

# 2 Data points to score, so we get 2 results back
data = {"data":
        [
          {
            "Pclass": 2,
            "Sex": 1,
            "Age": 40.0,
            "SibSp": 0,
            "Parch": 0,
            "Fare": 70,
            "Embarked": 1
          },
          {
            "Pclass": 1,
            "Sex": 0,
            "Age": 33.0,
            "SibSp": 0,
            "Parch": 0,
            "Fare": 70,
            "Embarked": 2
          }
        ]
    }
    
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
```

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

The screencast recording is available at [link](https://youtu.be/XMMesPDcZU0)


## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
