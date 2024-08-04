import mlflow
import streamlit as st
from mlflow import MlflowClient
import calendar
def get_registered_models():
    mlflow.set_tracking_uri('http://mlflow:5000')
    client = MlflowClient()
    registered_models = client.search_registered_models()
    
    model_dict = {}
    for model in registered_models:
        model_name = model.name
        versions = [version.version for version in model.latest_versions]
        model_dict[model_name] = versions
    
    return model_dict


def create_airport_dropdowns(df):
    """
    Create dropdowns in Streamlit for selecting various flight options.
    
    Args:
    df (pd.DataFrame): DataFrame containing 'startingAirport' and 'destinationAirport' columns.
    
    Returns:
    A dictionary with selected values from the dropdowns.
    """
    # Get unique values for airport dropdowns
    starting_airports = sorted(df['startingAirport'].unique())
    destination_airports = sorted(df['destinationAirport'].unique())
    
    # Define month names
    month_names = list(calendar.month_name)[1:]  # Excludes the empty string at index 0
    
    # Define day names (for days of the week)
    day_names = list(calendar.day_name)
    
    # Define day numbers (for day of the month)
    day_numbers = [str(day) for day in range(1, 32)]
    
    # Create columns for layout
    col1, col2, col3 = st.columns(3)
    
    # Create the dropdowns in separate columns
    with col1:
        selected_starting_airport = st.selectbox("Starting Airport", starting_airports, key="starting_airport_dropdown")
        basic_economy = st.selectbox("Basic Economy", ["Yes", "No"], key="basic_economy_dropdown")
        is_refundable = st.selectbox("Is Refundable", ["Yes", "No"], key="is_refundable_dropdown")
        departure_day_of_week = st.selectbox("Day of Week", day_names, key="departure_day_of_week_dropdown")
    
    with col2:
        selected_destination_airport = st.selectbox("Destination Airport", destination_airports, key="destination_airport_dropdown")
        is_non_stop = st.selectbox("Is Non-Stop", ["Yes", "No"], key="is_non_stop_dropdown")
        departure_hour = st.selectbox("Departure Hour", list(range(24)), key="departure_hour_dropdown")
        departure_day = st.selectbox("Day of Month", day_numbers, key="departure_day_dropdown")
    
    with col3:
        departure_month = st.selectbox("Departure Month", month_names, key="departure_month_dropdown")
        days_to_departure = st.number_input("Days to Departure", min_value=0, step=1, key="days_to_departure_input")
    
    return {
        "starting_airport": selected_starting_airport,
        "destination_airport": selected_destination_airport,
        "basic_economy": basic_economy,
        "is_refundable": is_refundable,
        "is_non_stop": is_non_stop,
        "departure_hour": departure_hour,
        "departure_day_of_week": departure_day_of_week,
        "departure_day": departure_day,
        "departure_month": departure_month,
        "days_to_departure": days_to_departure
    }
    
    