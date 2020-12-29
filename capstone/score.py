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
