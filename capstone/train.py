from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core import Workspace
from azureml.core.dataset import Dataset

run = Run.get_context()

def clean_data(ds):

    df = ds.to_pandas_dataframe()

    # Drop columns
    df.drop(['PassengerId', 'Name', 'Cabin', 'Ticket'], axis=1, inplace=True)

    # Fill na
    df['Embarked'] = df['Embarked'].fillna('S')  # Since df['Embarked'].value_counts() has 'S' as highest
    mean_age = df['Age'].mean()
    df['Age'] = df['Age'].fillna(mean_age)

    # Encode as numeric values
    df["Sex"] = df.Sex.apply(lambda s: 1 if s == "M" else 0)
    Emb_map = {"C":0, "Q":1, "S":2}
    df["Embarked"] = df.Embarked.map(Emb_map)

    # Remove label
    y_df = df.pop("Survived")

    return df, y_df

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

    os.makedirs('outputs', exist_ok=True)
    # files saved in the "outputs" folder are automatically uploaded into run history
    joblib.dump(model, 'outputs/model-hyperdrive.joblib')   


if __name__ == '__main__':

    # Get dataset 
    data_file = "https://github.com/shbv/azure_ml/blob/main/capstone/titanic_data.csv"
    ds = Dataset.Tabular.from_delimited_files(data_file)

    x, y = clean_data(ds)

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

    main()