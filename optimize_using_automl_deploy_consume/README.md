*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.


# Your Project Title Here

*TODO:* Write an overview to your project.  

In this project, 
- We train a machine learning model and deploy it using Azure ML studio. We then consume its endpoint using Python SDK and script using a JSON payload. 
- We also create a pipeline to run AutoML using Python SDK and Jupyter notebook. We publish this pipeline to get a REST endpoint, and use this endpoint to trigger pipeline runs from Jupyter notebook.

## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model".    

The following steps are performed in this project:
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/flow_ops_architecture.png)

## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

The following are the screenshots after key steps in the flow of operations:

- Registered Dataset in ML studio (Bank-marketing-dataset):
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/dataset.png)


- Compute Cluster created for training:
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/compute.png)


- Experiment completed:
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/experiment.png)


- AutoML model details (all models and best model with 0.9164 accuracy):
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/model-1.png)
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/model-2.png)


- Deployed model details:
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/deploy-model.png)
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/deploy-model-1.png)


- Enabled logging using logs.py script:
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/logs.png)


- Enabled Application insights using logs.py:
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/appinsights.png)
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/appinsights-1.png)


- Swagger running on localhost, and showing HTTP API methods/responses for the model:
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/swagger_ui.png)


- endpoint.py script run against the API to produces JSON output from the model:
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/endpoint-0.png)
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/endpoint.png)


- Apache benchmark run against the HTTP API to retrieve performance results:
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/apb.png)


- Pipeline created using SDK & jupyter notebook:
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/pipeline-0.png)


- Pipeline created and run completed 
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/pipeline-1.png)
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/pipeline-2.png)


- Published pipeline, showing REST endpoint & Active status
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/pipeline-3.png)


- Pipeline triggered using REST endpoint and completed the run
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/pipeline-4.png)
![alt text](https://github.com/shbv/azure_ml/blob/main/optimize_using_automl_deploy_consume/images/pipeline-5.png)

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:  
The screencast recording is available at [link](https://youtu.be/qdDArLVlJoQ)

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
