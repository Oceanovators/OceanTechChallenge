import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Mock data for Trash Bins
trash_bin_data = pd.DataFrame({
    'Bin_ID': [1, 2, 3, 4, 5, 6, 7],
    'Category': ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic', 'Compost', 'Trash'],
    'Warnings': [2, 0, 1, 0, 3, 2, 1],
    'Fill_Level': [random.randint(0, 100) for _ in range(7)]  # Mock fill levels
})

# Mock data for Drones
drone_data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
    'Waste_Type': ['Plastic', 'Metal', 'Paper', 'Plastic', 'Glass'],
    'Quantity': [50, 30, 20, 40, 25]
})

# Mock data for Landfills/Beaches
landfill_data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
    'Waste_Type': ['Plastic', 'Metal', 'Paper', 'Plastic', 'Glass'],
    'Quantity': [100, 80, 60, 120, 90]
})

# Streamlit App
st.title("Waste Surveillance Dashboard")

# Sidebar Navigation
selected_page = st.sidebar.radio("Navigation", ["Trash Bin", "Drone", "Landfill"])

# Trash Bin Section
if selected_page == "Trash Bin":
    st.header("Trash Bin Monitoring")
    st.table(trash_bin_data)

# Drone Section
elif selected_page == "Drone":
    st.header("Drone Data")
    st.plotly_chart(px.scatter(drone_data, x='Date', y='Quantity', color='Waste_Type', title='Drone Data'))

# Landfills/Beaches Section
elif selected_page == "Landfill":
    st.header("Landfills/Beaches Monitoring")
    st.plotly_chart(px.bar(landfill_data, x='Date', y='Quantity', color='Waste_Type', title='Landfills/Beaches Data'))
