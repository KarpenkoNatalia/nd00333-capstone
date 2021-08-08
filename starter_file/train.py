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
from azureml.data.dataset_factory import TabularDatasetFactory as tdf


# Create dataframe
file ='winequality-red.csv'


ds= pd.read_csv(file)


def clean_data(data):

    # Clean data
	
    x_df = data.dropna()

    # transform response variable: if quality >= 7: wine is "good" (1) else "not good"(0) 
    y_df = x_df.pop("quality").apply(lambda s: 1 if s >= 7 else 0)	

    return x_df, y_df

# clear data:
x, y = clean_data(ds)

# Split data into train and test sets

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

run = Run.get_context()
    

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
    joblib.dump(value=model, filename='outputs/model_wine001.pkl')

if __name__ == '__main__':
    main()