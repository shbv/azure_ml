# Source: https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-and-where?tabs=python

import json
import numpy as np
import os
#from sklearn.externals import joblib
from azureml.core import Model
import pandas as pd
import joblib
#import pickle

def init():
    global model
    #model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'sklearn_mnist_model.pkl')
    model_path = Model.get_model_path('hyperdrive')
    model = joblib.load(model_path)

def run(data):
    try:
        data_dict = json.loads(data)
        data = pd.DataFrame(data_dict["data"])
        result = model.predict(data)
        # You can return any data type, as long as it is JSON serializable.
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error
        
# ================
# Deployment code:
# ================

from azureml.core.environment import Environment
from azureml.core.model import InferenceConfig
from azureml.core.webservice import LocalWebservice, AciWebservice

# Create inference config and deployment config
inference_config = InferenceConfig(entry_script='score.py',environment=env) 
deployment_config = AciWebservice.deploy_configuration(auth_enabled=True)

# Deploy model and wait
service = Model.deploy(workspace=ws, name='hyperdrive-deploy', models=[model], inference_config = inference_config, deployment_config = deployment_config)
service.wait_for_deployment(show_output=True)

# Check status
print(service.state)

# Get uri & keys
scoring_uri = service.scoring_uri
print(scoring_uri)
key, secondary_key = service.get_keys()
print(key)

# =============
# Consume endpoint code:
# =============

import requests
import json

# URL for the web service, should be similar to:
#scoring_uri = ''
# If the service is authenticated, set the key or token
#key = ''

# 1 Datapoint to score, so we get 1 result back
data = {"data":
        [
          {
            "Pclass": 2,
            "Sex": 1,
            "Age": 30.0,
            "SibSp": 0,
            "Parch": 0,
            "Fare": 70,
            "Embarked": 1
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
print(resp.json())



# Get logs
print(service.get_logs())

# Delete service
service.delete()
