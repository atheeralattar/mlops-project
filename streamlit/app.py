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

df = pd.read_csv('mlops/dataset/dist.csv')

starting_airports = df['startingAirport'].unique()
destination_airports = df['destinationAirport'].unique()

# selected_starting_airport = st.selectbox("Select Starting Airport", starting_airports, key="starting_airport_dropdown")
# selected_destination_airport = st.selectbox("Select Destination Airport", destination_airports, key="destination_airport_dropdown")

selected_options = create_airport_dropdowns(df)

st.write ('Estimated Trip Price: ')