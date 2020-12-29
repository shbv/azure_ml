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

## Dataset

### Overview
*TODO*: Explain about the data you are using and where you got it from.

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.

### Access
*TODO*: Explain how you are accessing the data in your workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

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


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

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

- Best Hyperdrive model registered:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/hd-d-1.png)


- Best Hyperdrive model deployed:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/hd-d-2.png)


- ML studio showing the deployed Hyperdrive model and its REST endpoint:
![alt text](https://github.com/shbv/azure_ml/blob/main/capstone/images/hd-d-3.png)

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

The screencast recording is available at [link](https://youtu.be/qdDArLVlJoQ)

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
