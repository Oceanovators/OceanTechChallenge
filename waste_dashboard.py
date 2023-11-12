import streamlit as st
import pandas as pd
import plotly.express as px
import random
import numpy as np

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
    'Quantity': [random.randint(10, 50) for _ in range(5)]  # Mock quantities for each waste type
})

# Expand drone data to include quantities for all waste categories
all_categories = ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic', 'Compost', 'Trash']
expanded_drone_data = pd.DataFrame(columns=['Date', 'Waste_Type', 'Quantity'])
for date in drone_data['Date']:
    for category in all_categories:
        if category == 'Plastic':
            quantity = int(np.random.normal(30, 5))  # Generating normally distributed quantities for plastic
        else:
            quantity = random.randint(5, 20)
        expanded_drone_data = expanded_drone_data.append({'Date': date, 'Waste_Type': category, 'Quantity': max(quantity, 0)}, ignore_index=True)

# Mock data for Landfills/Beaches
landfill_data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
    'Waste_Type': ['Plastic', 'Metal', 'Paper', 'Plastic', 'Glass'],
    'Quantity': [random.randint(50, 100) for _ in range(5)]  # Mock quantities for each waste type
})

# Expand landfill data to include quantities for all waste categories
expanded_landfill_data = pd.DataFrame(columns=['Date', 'Waste_Type', 'Quantity'])
for date in landfill_data['Date']:
    for category in all_categories:
        if category == 'Plastic':
            quantity = int(np.random.normal(70, 10))  # Generating normally distributed quantities for plastic
        else:
            quantity = random.randint(30, 80)
        expanded_landfill_data = expanded_landfill_data.append({'Date': date, 'Waste_Type': category, 'Quantity': max(quantity, 0)}, ignore_index=True)

# Streamlit App
st.title("Waste Surveillance Dashboard")

# Sidebar Navigation
selected_page = st.sidebar.radio("Navigation", ["Trash Bin", "Drone", "Beach"])

# Trash Bin Section
if selected_page == "Trash Bin":
    st.header("Trash Bin Monitoring")
    st.table(trash_bin_data)

# Drone Section
elif selected_page == "Drone":
    st.header("Drone Data")
    st.plotly_chart(px.scatter(expanded_drone_data, x='Date', y='Quantity', color='Waste_Type', title='Drone Data'))

# Landfills/Beaches Section
elif selected_page == "Beach":
    st.header("Beaches Monitoring")
    st.plotly_chart(px.bar(expanded_landfill_data, x='Date', y='Quantity', color='Waste_Type', title='Landfills/Beaches Data'))
