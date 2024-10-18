import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and documentation
st.title("Interactive Data Exploration App")
st.markdown("""
This is a basic interactive Streamlit app. Below are two interactive elements:
1. A slider to select a year range.
2. A dropdown to select the type of data visualization.

Instructions:
- Use the slider to choose the year range you want to visualize.
- Use the dropdown menu to select the type of chart (e.g., line chart or bar chart).
""")

# Sample data (create a dataframe)
data = {
    'Year': list(range(1990, 2023)),
    'Value': [i * 100 for i in range(1990, 2023)]
}
df = pd.DataFrame(data)

# Interactive element 1: Year range slider
year_range = st.slider('Select year range', 1990, 2022, (2000, 2022))

# Filter data based on the selected year range
filtered_data = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

# Interactive element 2: Select visualization type
chart_type = st.selectbox('Select Chart Type', ['Line Chart', 'Bar Chart'])

# Visualization based on user selection
st.write(f"Displaying {chart_type} for the year range {year_range[0]} - {year_range[1]}")

if chart_type == 'Line Chart':
    st.line_chart(filtered_data.set_index('Year'))
elif chart_type == 'Bar Chart':
    st.bar_chart(filtered_data.set_index('Year'))

# Footer documentation
st.markdown("""
### About this app
This app allows users to visualize data interactively based on the year range and chart type.
""")


