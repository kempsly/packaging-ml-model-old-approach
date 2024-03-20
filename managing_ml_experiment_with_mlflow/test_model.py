import mlflow

# Set the tracking URI to a valid URI with the 'http' or 'https' scheme
mlflow.set_tracking_uri("http://127.0.0.1:5000")

logged_model = 'runs:/e494b111ff5749db9b2505506640ca6c/RandomForestClassifier'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Define the data for prediction
data = [[
    1.0,
    0.0,
    0.0,
    0.0,
    0.0,
    4.98745,
    360.0,
    1.0,
    2.0,
    8.698
]]

# Predict on a Pandas DataFrame.
import pandas as pd
prediction = loaded_model.predict(pd.DataFrame(data))
print(f"Prediction is : {prediction}")
