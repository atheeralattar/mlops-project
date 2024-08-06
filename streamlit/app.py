import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlops.streamlit.streamlit import *
from mlops.data_processing.data_prep import *
# Set the title of the app
st.title('Flight Price Predictor')

models_versions = get_registered_models()

selected_model = st.selectbox("Select a model", list(models_versions.keys()))

mlflow.set_tracking_uri('http://mlflow:5000')
client = MlflowClient()

run_id = client.get_model_version(selected_model, '1').run_id


dv_uri = f'runs:/{run_id}/dict_vectorizer'
loaded_dv = mlflow.sklearn.load_model(dv_uri)
logged_model_uri = f'runs:/{run_id}/model'
loaded_model = mlflow.pyfunc.load_model(logged_model_uri)

df = pd.read_csv('mlops/dataset/dist.csv')
starting_airports = df['startingAirport'].unique()
destination_airports = df['destinationAirport'].unique()

selected_options = create_airport_dropdowns(df)

startingAirport = selected_options['startingAirport']
destinationAirport = selected_options['destinationAirport']

try:
    distance = df.query('startingAirport == @startingAirport and destinationAirport == @destinationAirport')['DISTANCE'].iloc[0]
    selected_options['DISTANCE'] = distance
    transformed_data = loaded_dv.transform(selected_options)
    if destinationAirport == startingAirport:
        fare_estimate = 'Start and Destination airports are the same.'
    else:        
        fare_estimate = loaded_model.predict(transformed_data)
except:
    fare_estimate = 'No available trips for this route.'

st.write (f'Estimated Trip Price: {fare_estimate}')