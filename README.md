# OceanTechChallenge

Runninng in conda sandbox with 
Python 3.7.9 version 

Create conda environment using: 
conda create -n sandbox python=3.7.9

Dependencies installed: 
streamlit pandas plotly

Run the code as: 
streamlit run waste_dashboard.py


Dashboard for AI-Enhanced Waste Surveillance System

### Trash Bin Monitoring:
The dashboard provides insights into the monitoring of trash bins. Each bin is assigned a unique ID (`Bin_ID`) and a specific waste category (`Category`), such as cardboard, glass, metal, paper, plastic, compost, or general trash. The dashboard displays the number of warnings (`Warnings`) issued and the fill level (`Fill_Level`) of each bin.

### Drone Data:
This section of the dashboard focuses on the data collected by drones equipped with waste detection hardware. Drones fly over oceans to identify and classify floating waste. The data includes the date of the drone operation (`Date`), the type of waste detected (`Waste_Type`), and the quantity of each type of waste (`Quantity`). The quantities are generated based on a normal distribution, with a higher average quantity for plastic waste.

### Landfills/Beaches Monitoring:
This part of the dashboard provides insights into the monitoring of landfills and beaches. It includes data about the types of waste disposed of in landfills, represented by the columns `Date`, `Waste_Type`, and `Quantity`. The quantities are generated randomly, with a higher average quantity for plastic waste.

### Dashboard Navigation:
The dashboard includes a navigation sidebar allowing users to switch between different sections, such as Trash Bin Monitoring, Drone Data, and Landfills/Beaches Monitoring.

### Mock Data:
The dashboard utilizes mock data to simulate real-world scenarios. This is helpful for testing and demonstrating the capabilities of a waste surveillance system. The data includes information on waste categories, warnings, fill levels, drone-detected waste, and landfill waste.


### Future Applications:
The dashboard can be scaled and adapted for real-world applications. It could support municipalities, waste management companies, or environmental agencies in optimizing waste collection, identifying areas with high pollution levels, and planning effective cleanup operations. The ability to visualize and analyze data contributes to informed decision-making and sustainable waste management practices.

https://github.com/sijan67/OceanTechChallenge/assets/70575969/1b70b85c-d3d0-4a9a-92d3-a3ebecae4154

