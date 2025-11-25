import pandas as pd
import joblib
import os

def init():
    global model
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "lasso_best_model.pkl")
    model = joblib.load(model_path)

def run(df: pd.DataFrame):
    # df contains all columns from batch_input.csv
    predictions = model.predict(df)
    
    # return DataFrame so batch endpoint writes a CSV output
    return pd.DataFrame({"prediction": predictions})