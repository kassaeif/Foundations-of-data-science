import pandas as pd
import plotly.express as px
import streamlit as st
import statsmodels.api as sm

def plot_divorce_rates():
    # Plot 2: Divorce Rates
    st.write("### Divorce Rates Over Time (1990-2022)")

    # Load the dataset (Divorce Rates)
    file_path = r'C:/Users/Farshid/OneDrive - Michigan State University/courses/foundations of data science/project/working directory/state-divorce-rates-90-95-00-22.xlsx'
    excel_data = pd.ExcelFile(file_path)

    # Load the data from the sheet
    df = excel_data.parse('Sheet1')

    # Set the 'States' column as the index for easier plotting
    df.set_index('States', inplace=True)

    # Convert the data to numeric, forcing errors to NaN
    df = df.apply(pd.to_numeric, errors='coerce')

    # Transpose the data to make years the index and states as columns
    df_transposed = df.T

    # Drop any columns that are completely NaN
    df_transposed.dropna(how='all', axis=1, inplace=True)

    # Initialize state selection with no states pre-selected
    all_states = df_transposed.columns.tolist()
    selected_states_divorce = st.multiselect("Select or Deselect States (Divorce Rates)", all_states, default=[], key='divorce_select')

    # Add buttons to select all or no states for divorce rates
    if st.button("Select All States (Divorce Rates)", key='select_all_divorce'):
        selected_states_divorce = all_states
    if st.button("Deselect All States (Divorce Rates)", key='deselect_all_divorce'):
        selected_states_divorce = []

    # If no states are selected, show a message
    if len(selected_states_divorce) == 0:
        st.write("No states selected. Please select at least one state to view the divorce rate graph.")
    else:
        # Filter the data based on selected states
        df_filtered = df_transposed[selected_states_divorce]

        # Plotting with Plotly
        fig = px.line(df_filtered, x=df_filtered.index, y=df_filtered.columns, labels={'x': 'Year', 'value': 'Divorce Rate', 'variable': 'State'}, title='Divorce Rates Over Time')

        # Show the plot in Streamlit
        st.plotly_chart(fig)

        
def plot_marriage_rates():
        # Plot-specific code is placed entirely within this block for Option A
        st.write("### Marriage Rates Over Time (1990-2022)")
        # Load the dataset (adjust path as needed)
        file_path = r'C:/Users/Farshid/OneDrive - Michigan State University/courses/foundations of data science/project/working directory/state-marriage-rates-90-95-00-22.xlsx'
        excel_data = pd.ExcelFile(file_path)

        # Load the data from the sheet
        df = excel_data.parse('Sheet2')

        # Set the 'States' column as the index for easier plotting
        df.set_index('States', inplace=True)

        # Convert the data to numeric, forcing errors to NaN
        df = df.apply(pd.to_numeric, errors='coerce')

        # Transpose the data to make years the index and states as columns
        df_transposed = df.T

        # Drop any columns that are completely NaN
        df_transposed.dropna(how='all', axis=1, inplace=True)

        # Initialize state selection with no states pre-selected
        all_states = df_transposed.columns.tolist()
        selected_states_marriage = st.multiselect("Select or Deselect States (Marriage Rates)", all_states, default=[], key='marriage_select')

        # Add buttons to select all or no states for marriage rates
        if st.button("Select All States (Marriage Rates)", key='select_all_marriage'):
            selected_states_marriage = all_states
        if st.button("Deselect All States (Marriage Rates)", key='deselect_all_marriage'):
            selected_states_marriage = []

        # If no states are selected, show a message
        if len(selected_states_marriage) == 0:
            st.write("No states selected. Please select at least one state to view the marriage rate graph.")
        else:
            # Filter the data based on selected states
            df_filtered = df_transposed[selected_states_marriage]

            # Plotting with Plotly
            fig = px.line(df_filtered, x=df_filtered.index, y=df_filtered.columns, labels={'x': 'Year', 'value': 'Marriage Rate', 'variable': 'State'}, title='Marriage Rates Over Time')

            # Show the plot in Streamlit
            st.plotly_chart(fig)


def plot_marriage_heat_map():
        # Plot-specific code is placed entirely within this block for Option A
        st.write("### Marriage Rates Heatmap (1990-2022)")

        # Load the dataset
        file_path = r'C:/Users/Farshid/OneDrive - Michigan State University/courses/foundations of data science/project/working directory/state-marriage-rates-90-95-00-22.xlsx'
        excel_data = pd.ExcelFile(file_path)

        # Load the data from the sheet
        df = excel_data.parse('Sheet2')

        # Set the 'States' column as the index for easier plotting
        df.set_index('States', inplace=True)

        # Convert the data to numeric, forcing errors to NaN
        df = df.apply(pd.to_numeric, errors='coerce')

        # Sort the columns (years) in ascending order
        df = df[sorted(df.columns)]

        # Initialize state selection with no states pre-selected
        all_states = df.index.tolist()  # Use index for state selection
        selected_states_heatmap = st.multiselect("Select or Deselect States (Marriage Rates Heatmap)", all_states, default=[], key='heatmap_select')

        # Add buttons to select all or no states for the heatmap
        if st.button("Select All States (Heatmap)", key='select_all_heatmap'):
            selected_states_heatmap = all_states
        if st.button("Deselect All States (Heatmap)", key='deselect_all_heatmap'):
            selected_states_heatmap = []

        # If no states are selected, show a message
        if len(selected_states_heatmap) == 0:
            st.write("No states selected. Please select at least one state to view the heatmap.")
        else:
            # Filter the data based on selected states
            df_filtered = df.loc[selected_states_heatmap]

            # Plotting with Plotly
            fig = px.imshow(df_filtered, 
                            labels=dict(x="Year", y="State", color="Marriage Rate"), 
                            x=df_filtered.columns, 
                            y=df_filtered.index, 
                            color_continuous_scale="YlGnBu", 
                            aspect="auto", 
                            title="Marriage Rates Heatmap (1990-2022)")

            # Show the interactive plot in Streamlit
            st.plotly_chart(fig)


def plot_divorce_heat_map():
        # Plot-specific code for Divorce Rates Heatmap
        st.write("### Divorce Rates Heatmap (1990-2022)")

        # Load the dataset (Divorce Rates)
        file_path = r'C:/Users/Farshid/OneDrive - Michigan State University/courses/foundations of data science/project/working directory/state-divorce-rates-90-95-00-22.xlsx'
        excel_data = pd.ExcelFile(file_path)

        # Load the data from the sheet
        df = excel_data.parse('Sheet1')

        # Set the 'States' column as the index for easier plotting
        df.set_index('States', inplace=True)

        # Convert the data to numeric, forcing errors to NaN
        df = df.apply(pd.to_numeric, errors='coerce')

        # Sort the columns (years) in ascending order
        df = df[sorted(df.columns)]

        # Initialize state selection with no states pre-selected
        all_states = df.index.tolist()  # Use index for state selection
        selected_states_heatmap = st.multiselect("Select or Deselect States (Divorce Rates Heatmap)", all_states, default=[], key='divorce_heatmap_select')

        # Add buttons to select all or no states for the heatmap
        if st.button("Select All States (Heatmap)", key='select_all_divorce_heatmap'):
            selected_states_heatmap = all_states
        if st.button("Deselect All States (Heatmap)", key='deselect_all_divorce_heatmap'):
            selected_states_heatmap = []

        # If no states are selected, show a message
        if len(selected_states_heatmap) == 0:
            st.write("No states selected. Please select at least one state to view the heatmap.")
        else:
            # Filter the data based on selected states
            df_filtered = df.loc[selected_states_heatmap]

            # Plotting with Plotly
            fig = px.imshow(df_filtered, 
                            labels=dict(x="Year", y="State", color="Divorce Rate"), 
                            x=df_filtered.columns, 
                            y=df_filtered.index, 
                            color_continuous_scale="YlGnBu", 
                            aspect="auto", 
                            title="Divorce Rates Heatmap (1990-2022)")

            # Show the interactive plot in Streamlit
            st.plotly_chart(fig)



def plot_marriage_heat_map_year():
        # A dictionary to map full state names to their two-letter abbreviations
        state_abbrev = {
            'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
            'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
            'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
            'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
            'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
            'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
            'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
            'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
            'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
            'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
            'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
        }

        # Load the dataset
        file_path = r'C:/Users/Farshid/OneDrive - Michigan State University/courses/foundations of data science/project/working directory/state-marriage-rates-90-95-00-22.xlsx'
        excel_data = pd.ExcelFile(file_path)

        # Load the data from the sheet
        df = excel_data.parse('Sheet2')

        # Set the 'States' column as the index for easier plotting
        df.set_index('States', inplace=True)

        # Convert the data to numeric, forcing errors to NaN
        df = df.apply(pd.to_numeric, errors='coerce')

        # Initialize the Streamlit app with a title
        st.title("Marriage Rates by State")

        # Add a dropdown for year selection
        year = st.selectbox("Select a Year", df.columns.tolist(), index=len(df.columns)-1)

        # Reset index to get the States column back, and map full state names to abbreviations
        df.reset_index(inplace=True)
        df['State_Abbrev'] = df['States'].map(state_abbrev)

        # Check if there are any unmapped states (optional for debugging)
        unmapped_states = df[df['State_Abbrev'].isna()]
        if not unmapped_states.empty:
            st.write("The following states were not mapped:", unmapped_states)

        # Plotting the choropleth map using Plotly Express
        fig = px.choropleth(df,
                            locations='State_Abbrev',  # Use state abbreviations for the locations
                            locationmode='USA-states',  # Location mode (states of the USA)
                            color=year,  # Column containing data for the selected year
                            hover_name='States',  # Data to show on hover
                            color_continuous_scale='Viridis',  # Color scale for the heatmap
                            scope='usa',  # Restrict the map to the USA
                            labels={year: f"Marriage Rate in {year}"},  # Label for the color bar
                            title=f'Marriage Rates by State in {year}')  # Title of the map

        # Update the layout for better visualization
        fig.update_layout(
            geo=dict(
                scope='usa',  # Focus on the USA
                projection_type='albers usa',  # Type of projection
                showlakes=True,  # Show lakes
                lakecolor='rgb(255, 255, 255)'  # Color for the lakes
            )
        )

        # Display the interactive plot in Streamlit
        st.plotly_chart(fig)


def plot_divorce_heat_map_year():
        # A dictionary to map full state names to their two-letter abbreviations
        state_abbrev = {
            'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
            'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
            'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
            'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
            'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
            'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
            'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
            'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
            'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
            'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
            'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
        }

        # Load the dataset (Divorce Rates)
        file_path = r'C:/Users/Farshid/OneDrive - Michigan State University/courses/foundations of data science/project/working directory/state-divorce-rates-90-95-00-22.xlsx'
        excel_data = pd.ExcelFile(file_path)

        # Load the data from the sheet
        df = excel_data.parse('Sheet1')

        # Set the 'States' column as the index for easier plotting
        df.set_index('States', inplace=True)

        # Convert the data to numeric, forcing errors to NaN
        df = df.apply(pd.to_numeric, errors='coerce')

        # Initialize the Streamlit app with a title
        st.title("Divorce Rates by State")

        # Add a dropdown for year selection with a unique key
        year = st.selectbox("Select a Year", df.columns.tolist(), index=len(df.columns)-1, key='divorce_year_select')

        # Reset index to get the States column back, and map full state names to abbreviations
        df.reset_index(inplace=True)
        df['State_Abbrev'] = df['States'].map(state_abbrev)

        # Check if there are any unmapped states (optional for debugging)
        unmapped_states = df[df['State_Abbrev'].isna()]
        if not unmapped_states.empty:
            st.write("The following states were not mapped:", unmapped_states)

        # Plotting the choropleth map using Plotly Express
        fig = px.choropleth(df,
                            locations='State_Abbrev',  # Use state abbreviations for the locations
                            locationmode='USA-states',  # Location mode (states of the USA)
                            color=year,  # Column containing data for the selected year
                            hover_name='States',  # Data to show on hover
                            color_continuous_scale='Viridis',  # Color scale for the heatmap
                            scope='usa',  # Restrict the map to the USA
                            labels={year: f"Divorce Rate in {year}"},  # Label for the color bar
                            title=f'Divorce Rates by State in {year}')  # Title of the map

        # Update the layout for better visualization
        fig.update_layout(
            geo=dict(
                scope='usa',  # Focus on the USA
                projection_type='albers usa',  # Type of projection
                showlakes=True,  # Show lakes
                lakecolor='rgb(255, 255, 255)'  # Color for the lakes
            )
        )

        # Display the interactive plot in Streamlit
        st.plotly_chart(fig)

def plot_gdp():
        # Load the dataset
        file_path = 'filtered_all_industry_gdp.csv'  # Adjust the path if necessary
        data = pd.read_csv(file_path)

        # Reshape the dataset to have a "Year" and "GDP" column (long format)
        gdp_long = data.melt(id_vars=['GeoName'], value_vars=[str(year) for year in range(1997, 2021)], 
                            var_name='Year', value_name='GDP')

        # Convert 'Year' to numeric type
        gdp_long['Year'] = pd.to_numeric(gdp_long['Year'])

        # Initialize the Streamlit app with a title
        st.title("GDP Over Time for Selected States (All Industry)")

        # Get a list of all states (GeoName)
        all_states = gdp_long['GeoName'].unique()

        # Add a multiselect widget for state selection
        selected_states_gdp = st.multiselect("Select or Deselect States (GDP)", all_states, default=[], key='gdp_select')

        # Add buttons to select all or no states for GDP plot
        if st.button("Select All States (GDP)", key='select_all_gdp'):
            selected_states_gdp = all_states
        if st.button("Deselect All States (GDP)", key='deselect_all_gdp'):
            selected_states_gdp = []

        # If no states are selected, show a message
        if len(selected_states_gdp) == 0:
            st.write("No states selected. Please select at least one state to view the GDP graph.")
        else:
            # Filter the data based on selected states
            df_filtered = gdp_long[gdp_long['GeoName'].isin(selected_states_gdp)]

            # Plotting with Plotly
            fig = px.line(df_filtered, x='Year', y='GDP', color='GeoName', 
                        labels={'GeoName': 'State', 'GDP': 'GDP (Millions of Current Dollars)', 'Year': 'Year'},
                        title='GDP Over Time for Selected States (All Industry)')

            # Show the interactive plot in Streamlit
            st.plotly_chart(fig)

def plot_unemployment():
        # Load the dataset
        file_path = 'Unemployment in America Per US State.csv'  # Adjust the path if necessary
        data = pd.read_csv(file_path)

        # Filter necessary columns: 'State/Area', 'Year', 'Month', and 'Percent (%) of Labor Force Unemployed in State/Area'
        data_filtered = data[['State/Area', 'Year', 'Month', 'Percent (%) of Labor Force Unemployed in State/Area']]

        # Group by 'State/Area' and 'Year', then calculate the mean unemployment rate for each year (averaging all 12 months)
        avg_unemployment_per_year = data_filtered.groupby(['State/Area', 'Year'])['Percent (%) of Labor Force Unemployed in State/Area'].mean().reset_index()

        # Initialize the Streamlit app with a title
        st.title("Average Unemployment Percent Over Time for Selected States")

        # Get a list of all states
        all_states = avg_unemployment_per_year['State/Area'].unique()

        # Add a multiselect widget for state selection
        selected_states_unemployment = st.multiselect("Select or Deselect States (Unemployment Rate)", all_states, default=[], key='unemployment_select')

        # Add buttons to select all or no states for the unemployment rate plot
        if st.button("Select All States (Unemployment Rate)", key='select_all_unemployment'):
            selected_states_unemployment = all_states
        if st.button("Deselect All States (Unemployment Rate)", key='deselect_all_unemployment'):
            selected_states_unemployment = []

        # If no states are selected, show a message
        if len(selected_states_unemployment) == 0:
            st.write("No states selected. Please select at least one state to view the unemployment rate graph.")
        else:
            # Filter the data based on selected states
            df_filtered = avg_unemployment_per_year[avg_unemployment_per_year['State/Area'].isin(selected_states_unemployment)]

            # Plotting with Plotly
            fig = px.line(df_filtered, x='Year', y='Percent (%) of Labor Force Unemployed in State/Area', color='State/Area',
                        labels={'State/Area': 'State', 'Percent (%) of Labor Force Unemployed in State/Area': 'Unemployment Percent (%)', 'Year': 'Year'},
                        title='Average Unemployment Percent Over Time for Selected States (Averaged by Year)')

            # Show the interactive plot in Streamlit
            st.plotly_chart(fig)

def plot_gdp_vs_marriage():
    # Load both datasets
    gdp_data = pd.read_csv(r'filtered_all_industry_gdp -since 2000.csv')
    marriage_data = pd.read_csv(r'state-marriage-rates-90-95-00-22.csv')

    # Remove unnecessary columns that might be 'Unnamed'
    gdp_data = gdp_data.loc[:, ~gdp_data.columns.str.contains('^Unnamed')]
    marriage_data = marriage_data.loc[:, ~marriage_data.columns.str.contains('^Unnamed')]

    # Reshape the GDP data (melt from wide to long format)
    gdp_data_melted = gdp_data.melt(id_vars=['State'], var_name='Year', value_name='GDP')

    # Reshape the Marriage Rate data (melt from wide to long format)
    marriage_data_melted = marriage_data.melt(id_vars=['State'], var_name='Year', value_name='MarriageRate')

    # Convert Year columns to numeric to ensure proper merging
    gdp_data_melted['Year'] = pd.to_numeric(gdp_data_melted['Year'], errors='coerce')
    marriage_data_melted['Year'] = pd.to_numeric(marriage_data_melted['Year'], errors='coerce')

    # Drop any rows with invalid years
    gdp_data_melted = gdp_data_melted.dropna(subset=['Year'])
    marriage_data_melted = marriage_data_melted.dropna(subset=['Year'])

    # Convert GDP and MarriageRate columns to numeric, coercing errors
    gdp_data_melted['GDP'] = pd.to_numeric(gdp_data_melted['GDP'], errors='coerce')
    marriage_data_melted['MarriageRate'] = pd.to_numeric(marriage_data_melted['MarriageRate'], errors='coerce')

    # Drop rows with NaN values in GDP or MarriageRate columns
    gdp_data_melted = gdp_data_melted.dropna(subset=['GDP'])
    marriage_data_melted = marriage_data_melted.dropna(subset=['MarriageRate'])

    # Merge datasets on 'State' and 'Year'
    merged_data = pd.merge(gdp_data_melted, marriage_data_melted, on=['State', 'Year'], how='inner')

    # Initialize the Streamlit app with a title
    st.title("GDP vs. Marriage Rate")

    # Get a list of all states
    all_states = merged_data['State'].unique()

    # Add a multiselect widget for state selection (deselected by default)
    selected_states = st.multiselect("Select or Deselect States", all_states, default=[], key='state_select')

    # Add buttons to select all or no states for GDP and Marriage Rate plot
    if st.button("Select All States", key='select_all_states'):
        selected_states = all_states
    if st.button("Deselect All States", key='deselect_all_states'):
        selected_states = []

    # Add a slider for year selection
    min_year = int(merged_data['Year'].min())
    max_year = int(merged_data['Year'].max())
    selected_year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year), key='year_slider')

    # Filter the data based on selected states and year range
    filtered_data = merged_data[
        (merged_data['State'].isin(selected_states)) & 
        (merged_data['Year'] >= selected_year_range[0]) & 
        (merged_data['Year'] <= selected_year_range[1])
    ]

    # If no states are selected, show a message
    if len(selected_states) == 0:
        st.write("No states selected. Please select at least one state to view the scatter plot.")
    else:
        # Calculate correlation between GDP and Marriage Rate
        correlation = filtered_data['GDP'].corr(filtered_data['MarriageRate'])
        st.write(f"Correlation between GDP and Marriage Rate: {correlation:.2f}")

        # Plotting with Plotly (simple linear plot, no log scale)
        fig = px.scatter(
            filtered_data, 
            x='GDP', 
            y='MarriageRate', 
            color='State', 
            hover_data=['Year'],  # Add 'Year' to hover tooltip
            labels={
                'GDP': 'GDP (Millions of Current Dollars)', 
                'MarriageRate': 'Marriage Rate', 
                'State': 'State'
            },
            title=f'GDP vs. Marriage Rate (Years {selected_year_range[0]}-{selected_year_range[1]})'
        )

        # Show the scatter plot in Streamlit
        st.plotly_chart(fig)




def plot_gdp_vs_divorce():

        # Load both datasets
        gdp_data = pd.read_csv(r'filtered_all_industry_gdp -since 2000.csv')
        divorce_data = pd.read_csv(r'state-divorce-rates-90-95-00-22.csv')

        # Remove unnecessary columns that might be 'Unnamed'
        gdp_data = gdp_data.loc[:, ~gdp_data.columns.str.contains('^Unnamed')]
        divorce_data = divorce_data.loc[:, ~divorce_data.columns.str.contains('^Unnamed')]

        # Reshape the GDP data (melt from wide to long format)
        gdp_data_melted = gdp_data.melt(id_vars=['State'], var_name='Year', value_name='GDP')

        # Reshape the Divorce Rate data (melt from wide to long format)
        divorce_data_melted = divorce_data.melt(id_vars=['State'], var_name='Year', value_name='DivorceRate')

        # Convert Year columns to numeric to ensure proper merging
        gdp_data_melted['Year'] = pd.to_numeric(gdp_data_melted['Year'], errors='coerce')
        divorce_data_melted['Year'] = pd.to_numeric(divorce_data_melted['Year'], errors='coerce')

        # Drop any rows with invalid years
        gdp_data_melted = gdp_data_melted.dropna(subset=['Year'])
        divorce_data_melted = divorce_data_melted.dropna(subset=['Year'])

        # Convert GDP and DivorceRate columns to numeric, coercing errors
        gdp_data_melted['GDP'] = pd.to_numeric(gdp_data_melted['GDP'], errors='coerce')
        divorce_data_melted['DivorceRate'] = pd.to_numeric(divorce_data_melted['DivorceRate'], errors='coerce')

        # Drop rows with NaN values in GDP or DivorceRate columns
        gdp_data_melted = gdp_data_melted.dropna(subset=['GDP'])
        divorce_data_melted = divorce_data_melted.dropna(subset=['DivorceRate'])

        # Merge datasets on 'State' and 'Year'
        merged_data = pd.merge(gdp_data_melted, divorce_data_melted, on=['State', 'Year'], how='inner')

        # Initialize the Streamlit app with a title
        st.title("GDP vs. Divorce Rate")

        # Get a list of all states
        all_states = merged_data['State'].unique()

        # Add a multiselect widget for state selection with a unique key
        selected_states = st.multiselect(
            "Select or Deselect States", all_states, default=[], key='gdp_divorce_state_select'
        )

        # Add buttons to select/deselect all states with unique keys
        if st.button("Select All States", key='gdp_divorce_select_all_states'):
            selected_states = all_states
        if st.button("Deselect All States", key='gdp_divorce_deselect_all_states'):
            selected_states = []

        # Add a slider for year selection with a unique key
        min_year = int(merged_data['Year'].min())
        max_year = int(merged_data['Year'].max())
        selected_year_range = st.slider(
            "Select Year Range", min_year, max_year, (min_year, max_year), key='gdp_divorce_year_slider'
        )

        # Filter the data based on selected states and year range
        filtered_data = merged_data[
            (merged_data['State'].isin(selected_states)) &
            (merged_data['Year'] >= selected_year_range[0]) &
            (merged_data['Year'] <= selected_year_range[1])
        ]

        # If no states are selected, show a message
        if len(selected_states) == 0:
            st.write("No states selected. Please select at least one state to view the scatter plot.")
        else:
            # Calculate correlation between GDP and Divorce Rate
            correlation = filtered_data['GDP'].corr(filtered_data['DivorceRate'])
            st.write(f"Correlation between GDP and Divorce Rate: {correlation:.2f}")

            # Perform linear regression
            X = filtered_data['GDP']
            y = filtered_data['DivorceRate']
            X = sm.add_constant(X)  # Add constant term for intercept

            model = sm.OLS(y, X).fit()  # Fit regression model
            filtered_data['RegressionLine'] = model.predict(X)  # Predict values

            # Plot with Plotly
            fig = px.scatter(
                filtered_data, 
                x='GDP', 
                y='DivorceRate', 
                color='State', 
                hover_data=['Year'],  # Add 'Year' to hover tooltip
                labels={
                    'GDP': 'GDP (Millions of Current Dollars)', 
                    'DivorceRate': 'Divorce Rate', 
                    'State': 'State'
                },
                title=f'GDP vs. Divorce Rate (Years {selected_year_range[0]}-{selected_year_range[1]})'
            )

            # Add regression line to the plot
            fig.add_traces(px.line(
                filtered_data, x='GDP', y='RegressionLine', color_discrete_sequence=['red']
            ).data)

            # Show the scatter plot in Streamlit
            st.plotly_chart(fig)




     
def plot_marriage_vs_divorce():
    # Load both marriage and divorce datasets
    marriage_data = pd.read_csv(r'state-marriage-rates-90-95-00-22.csv')
    divorce_data = pd.read_csv(r'state-divorce-rates-90-95-00-22.csv')

    # Remove unnecessary columns that might be 'Unnamed'
    marriage_data = marriage_data.loc[:, ~marriage_data.columns.str.contains('^Unnamed')]
    divorce_data = divorce_data.loc[:, ~divorce_data.columns.str.contains('^Unnamed')]

    # Reshape the Marriage Rate data (melt from wide to long format)
    marriage_data_melted = marriage_data.melt(id_vars=['State'], var_name='Year', value_name='MarriageRate')

    # Reshape the Divorce Rate data (melt from wide to long format)
    divorce_data_melted = divorce_data.melt(id_vars=['State'], var_name='Year', value_name='DivorceRate')

    # Convert Year columns to numeric to ensure proper merging
    marriage_data_melted['Year'] = pd.to_numeric(marriage_data_melted['Year'], errors='coerce')
    divorce_data_melted['Year'] = pd.to_numeric(divorce_data_melted['Year'], errors='coerce')

    # Drop any rows with invalid years
    marriage_data_melted = marriage_data_melted.dropna(subset=['Year'])
    divorce_data_melted = divorce_data_melted.dropna(subset=['Year'])

    # Convert MarriageRate and DivorceRate columns to numeric, coercing errors
    marriage_data_melted['MarriageRate'] = pd.to_numeric(marriage_data_melted['MarriageRate'], errors='coerce')
    divorce_data_melted['DivorceRate'] = pd.to_numeric(divorce_data_melted['DivorceRate'], errors='coerce')

    # Drop rows with NaN values in MarriageRate or DivorceRate columns
    marriage_data_melted = marriage_data_melted.dropna(subset=['MarriageRate'])
    divorce_data_melted = divorce_data_melted.dropna(subset=['DivorceRate'])

    # Merge datasets on 'State' and 'Year'
    merged_data = pd.merge(marriage_data_melted, divorce_data_melted, on=['State', 'Year'], how='inner')

    # Initialize the Streamlit app with a title
    st.title("Marriage Rate vs. Divorce Rate")

    # Get a list of all states
    all_states = merged_data['State'].unique()

    # Add a multiselect widget for state selection (deselected by default)
    selected_states = st.multiselect("Select or Deselect States", all_states, default=[], key='marriage_divorce_state_select')

    # Add buttons to select all or no states for Marriage and Divorce Rate plot
    if st.button("Select All States", key='marriage_divorce_select_all_states'):
        selected_states = all_states
    if st.button("Deselect All States", key='marriage_divorce_deselect_all_states'):
        selected_states = []

    # Add a slider for year selection
    min_year = int(merged_data['Year'].min())
    max_year = int(merged_data['Year'].max())
    selected_year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year), key='marriage_divorce_year_slider')

    # Filter the data based on selected states and year range
    filtered_data = merged_data[
        (merged_data['State'].isin(selected_states)) & 
        (merged_data['Year'] >= selected_year_range[0]) & 
        (merged_data['Year'] <= selected_year_range[1])
    ]

    # If no states are selected, show a message
    if len(selected_states) == 0:
        st.write("No states selected. Please select at least one state to view the scatter plot.")
    else:
        # Calculate correlation between Marriage Rate and Divorce Rate
        correlation = filtered_data['MarriageRate'].corr(filtered_data['DivorceRate'])
        st.write(f"Correlation between Marriage Rate and Divorce Rate: {correlation:.2f}")

        # Plotting with Plotly (scatter plot with hover data)
        fig = px.scatter(
            filtered_data, 
            x='MarriageRate', 
            y='DivorceRate', 
            color='State', 
            hover_data=['Year'],  # Add 'Year' to hover tooltip
            labels={
                'MarriageRate': 'Marriage Rate', 
                'DivorceRate': 'Divorce Rate', 
                'State': 'State'
            },
            title=f'Marriage Rate vs. Divorce Rate (Years {selected_year_range[0]}-{selected_year_range[1]})'
        )

        # Show the scatter plot in Streamlit
        st.plotly_chart(fig)



def plot_norm_divorce_vs_marriage():
        # Load both marriage and divorce datasets
        marriage_data = pd.read_csv(r'state-marriage-rates-90-95-00-22.csv')
        divorce_data = pd.read_csv(r'state-divorce-rates-90-95-00-22.csv')

        # Remove unnecessary columns that might be 'Unnamed'
        marriage_data = marriage_data.loc[:, ~marriage_data.columns.str.contains('^Unnamed')]
        divorce_data = divorce_data.loc[:, ~divorce_data.columns.str.contains('^Unnamed')]

        # Reshape the Marriage Rate data (melt from wide to long format)
        marriage_data_melted = marriage_data.melt(id_vars=['State'], var_name='Year', value_name='MarriageRate')

        # Reshape the Divorce Rate data (melt from wide to long format)
        divorce_data_melted = divorce_data.melt(id_vars=['State'], var_name='Year', value_name='DivorceRate')

        # Convert Year columns to numeric to ensure proper merging
        marriage_data_melted['Year'] = pd.to_numeric(marriage_data_melted['Year'], errors='coerce')
        divorce_data_melted['Year'] = pd.to_numeric(divorce_data_melted['Year'], errors='coerce')

        # Drop any rows with invalid years
        marriage_data_melted = marriage_data_melted.dropna(subset=['Year'])
        divorce_data_melted = divorce_data_melted.dropna(subset=['Year'])

        # Convert MarriageRate and DivorceRate columns to numeric, coercing errors
        marriage_data_melted['MarriageRate'] = pd.to_numeric(marriage_data_melted['MarriageRate'], errors='coerce')
        divorce_data_melted['DivorceRate'] = pd.to_numeric(divorce_data_melted['DivorceRate'], errors='coerce')

        # Drop rows with NaN values in MarriageRate or DivorceRate columns
        marriage_data_melted = marriage_data_melted.dropna(subset=['MarriageRate'])
        divorce_data_melted = divorce_data_melted.dropna(subset=['DivorceRate'])

        # Merge datasets on 'State' and 'Year'
        merged_data = pd.merge(marriage_data_melted, divorce_data_melted, on=['State', 'Year'], how='inner')

        # Normalize DivorceRate by MarriageRate
        merged_data['NormalizedDivorceRate'] = merged_data['DivorceRate'] / merged_data['MarriageRate']

        # Initialize the Streamlit app with a title
        st.title("Normalized Divorce Rate by Marriage Rate Over Time")

        # Get a list of all states
        all_states = merged_data['State'].unique()

        # Add a multiselect widget for state selection (deselected by default)
        selected_states = st.multiselect("Select or Deselect States", all_states, default=[], key='normalized_divorce_state_select')

        # Add buttons to select all or no states for the plot
        if st.button("Select All States", key='normalized_divorce_select_all_states'):
            selected_states = all_states
        if st.button("Deselect All States", key='normalized_divorce_deselect_all_states'):
            selected_states = []

        # Add a slider for year selection
        min_year = int(merged_data['Year'].min())
        max_year = int(merged_data['Year'].max())
        selected_year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year), key='normalized_divorce_year_slider')

        # Filter the data based on selected states and year range
        filtered_data = merged_data[(merged_data['State'].isin(selected_states)) & 
                                    (merged_data['Year'] >= selected_year_range[0]) & 
                                    (merged_data['Year'] <= selected_year_range[1])]

        # If no states are selected, show a message
        if len(selected_states) == 0:
            st.write("No states selected. Please select at least one state to view the plot.")
        else:
            # Plotting with Plotly
            fig = px.line(filtered_data, x='Year', y='NormalizedDivorceRate', color='State',
                        labels={'NormalizedDivorceRate': 'Normalized Divorce Rate', 'Year': 'Year', 'State': 'State'},
                        title=f'Normalized Divorce Rate by Marriage Rate (Years {selected_year_range[0]}-{selected_year_range[1]})')

            # Show the line plot in Streamlit
            st.plotly_chart(fig)

def plot_norm_marriage_vs_divorce():
    # Load both marriage and divorce datasets
    marriage_data = pd.read_csv(r'state-marriage-rates-90-95-00-22.csv')
    divorce_data = pd.read_csv(r'state-divorce-rates-90-95-00-22.csv')

    # Remove unnecessary columns that might be 'Unnamed'
    marriage_data = marriage_data.loc[:, ~marriage_data.columns.str.contains('^Unnamed')]
    divorce_data = divorce_data.loc[:, ~divorce_data.columns.str.contains('^Unnamed')]

    # Reshape the Marriage Rate data (melt from wide to long format)
    marriage_data_melted = marriage_data.melt(id_vars=['State'], var_name='Year', value_name='MarriageRate')

    # Reshape the Divorce Rate data (melt from wide to long format)
    divorce_data_melted = divorce_data.melt(id_vars=['State'], var_name='Year', value_name='DivorceRate')

    # Convert Year columns to numeric to ensure proper merging
    marriage_data_melted['Year'] = pd.to_numeric(marriage_data_melted['Year'], errors='coerce')
    divorce_data_melted['Year'] = pd.to_numeric(divorce_data_melted['Year'], errors='coerce')

    # Drop any rows with invalid years
    marriage_data_melted = marriage_data_melted.dropna(subset=['Year'])
    divorce_data_melted = divorce_data_melted.dropna(subset=['Year'])

    # Convert MarriageRate and DivorceRate columns to numeric, coercing errors
    marriage_data_melted['MarriageRate'] = pd.to_numeric(marriage_data_melted['MarriageRate'], errors='coerce')
    divorce_data_melted['DivorceRate'] = pd.to_numeric(divorce_data_melted['DivorceRate'], errors='coerce')

    # Drop rows with NaN values in MarriageRate or DivorceRate columns
    marriage_data_melted = marriage_data_melted.dropna(subset=['MarriageRate'])
    divorce_data_melted = divorce_data_melted.dropna(subset=['DivorceRate'])

    # Merge datasets on 'State' and 'Year'
    merged_data = pd.merge(marriage_data_melted, divorce_data_melted, on=['State', 'Year'], how='inner')

    # Normalize MarriageRate by DivorceRate
    merged_data['NormalizedMarriageRate'] = merged_data['MarriageRate'] / merged_data['DivorceRate']

    # Initialize the Streamlit app with a title
    st.title("Normalized Marriage Rate by Divorce Rate Over Time")

    # Get a list of all states
    all_states = merged_data['State'].unique()

    # Add a multiselect widget for state selection (deselected by default)
    selected_states = st.multiselect("Select or Deselect States", all_states, default=[], key='normalized_marriage_state_select')

    # Add buttons to select all or no states for the plot
    if st.button("Select All States", key='normalized_marriage_select_all_states'):
        selected_states = all_states
    if st.button("Deselect All States", key='normalized_marriage_deselect_all_states'):
        selected_states = []

    # Add a slider for year selection
    min_year = int(merged_data['Year'].min())
    max_year = int(merged_data['Year'].max())
    selected_year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year), key='normalized_marriage_year_slider')

    # Filter the data based on selected states and year range
    filtered_data = merged_data[
        (merged_data['State'].isin(selected_states)) & 
        (merged_data['Year'] >= selected_year_range[0]) & 
        (merged_data['Year'] <= selected_year_range[1])
    ]

    # If no states are selected, show a message
    if len(selected_states) == 0:
        st.write("No states selected. Please select at least one state to view the plot.")
    else:
        # Plotting with Plotly
        fig = px.line(
            filtered_data, 
            x='Year', 
            y='NormalizedMarriageRate', 
            color='State',
            hover_data=['Year'],  # Add 'Year' to hover tooltip
            labels={
                'NormalizedMarriageRate': 'Normalized Marriage Rate', 
                'Year': 'Year', 
                'State': 'State'
            },
            title=f'Normalized Marriage Rate by Divorce Rate (Years {selected_year_range[0]}-{selected_year_range[1]})'
        )

        # Show the line plot in Streamlit
        st.plotly_chart(fig)



def plot_unemp_vs_marriage():
    # Load both datasets
    marriage_data = pd.read_csv(r'state-marriage-rates-90-95-00-22.csv')
    unemployment_data = pd.read_csv(r'Unemployment in America Per US State.csv')

    # Remove unnecessary columns that might be 'Unnamed'
    marriage_data = marriage_data.loc[:, ~marriage_data.columns.str.contains('^Unnamed')]
    unemployment_data = unemployment_data.loc[:, ~unemployment_data.columns.str.contains('^Unnamed')]

    # Reshape the Marriage Rate data (melt from wide to long format)
    marriage_data_melted = marriage_data.melt(id_vars=['State'], var_name='Year', value_name='MarriageRate')

    # Reshape the Unemployment Rate data (wide to long format)
    unemployment_data_melted = unemployment_data.melt(id_vars=['State/Area', 'Year'], var_name='Month', value_name='UnemploymentRate')

    # Convert UnemploymentRate to numeric, coercing errors to NaN
    unemployment_data_melted['UnemploymentRate'] = pd.to_numeric(unemployment_data_melted['UnemploymentRate'], errors='coerce')

    # Convert MarriageRate to numeric, coercing errors to NaN
    marriage_data_melted['MarriageRate'] = pd.to_numeric(marriage_data_melted['MarriageRate'], errors='coerce')

    # Group unemployment data by State and Year to get the average annual unemployment rate, ignoring NaN values
    unemployment_data_annual = unemployment_data_melted.groupby(['State/Area', 'Year'])['UnemploymentRate'].mean().reset_index()

    # Ensure the year columns are numeric for proper merging
    marriage_data_melted['Year'] = pd.to_numeric(marriage_data_melted['Year'], errors='coerce')
    unemployment_data_annual['Year'] = pd.to_numeric(unemployment_data_annual['Year'], errors='coerce')

    # Rename 'State/Area' in unemployment data to 'State' for merging consistency
    unemployment_data_annual.rename(columns={'State/Area': 'State'}, inplace=True)

    # Merge the datasets on 'State' and 'Year'
    merged_data = pd.merge(marriage_data_melted, unemployment_data_annual, on=['State', 'Year'], how='inner')

    # Drop rows with NaN values in either MarriageRate or UnemploymentRate
    merged_data = merged_data.dropna(subset=['MarriageRate', 'UnemploymentRate'])

    # Initialize the Streamlit app with a title
    st.title("Marriage Rate vs. Unemployment Rate")

    # Get a list of all states
    all_states = merged_data['State'].unique()

    # Add a multiselect widget for state selection (deselected by default)
    selected_states = st.multiselect("Select or Deselect States", all_states, default=[], key='marriage_unemployment_state_select')

    # Add buttons to select all or no states for the plot
    if st.button("Select All States", key='marriage_unemployment_select_all_states'):
        selected_states = all_states
    if st.button("Deselect All States", key='marriage_unemployment_deselect_all_states'):
        selected_states = []

    # Add a slider for year selection
    min_year = int(merged_data['Year'].min())
    max_year = int(merged_data['Year'].max())
    selected_year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year), key='marriage_unemployment_year_slider')

    # Filter the data based on selected states and year range
    filtered_data = merged_data[
        (merged_data['State'].isin(selected_states)) & 
        (merged_data['Year'] >= selected_year_range[0]) & 
        (merged_data['Year'] <= selected_year_range[1])
    ]

    # If no states are selected, show a message
    if len(selected_states) == 0:
        st.write("No states selected. Please select at least one state to view the plot.")
    else:
        # Calculate correlation between Marriage Rate and Unemployment Rate
        correlation = filtered_data['MarriageRate'].corr(filtered_data['UnemploymentRate'])
        st.write(f"Correlation between Marriage Rate and Unemployment Rate: {correlation:.2f}")

        # Plotting with Plotly (simple linear plot)
        fig = px.scatter(
            filtered_data, 
            x='MarriageRate', 
            y='UnemploymentRate', 
            color='State',
            hover_data=['Year'],  # Add 'Year' to hover tooltip
            labels={
                'MarriageRate': 'Marriage Rate', 
                'UnemploymentRate': 'Unemployment Rate', 
                'State': 'State'
            },
            title=f'Marriage Rate vs. Unemployment Rate (Years {selected_year_range[0]}-{selected_year_range[1]})'
        )

        # Show the scatter plot in Streamlit
        st.plotly_chart(fig)


def plot_unemp_vs_divorce():

        # Load both datasets
        divorce_data = pd.read_csv(r'state-divorce-rates-90-95-00-22.csv')
        unemployment_data = pd.read_csv(r'Unemployment in America Per US State.csv')

        # Remove unnecessary columns that might be 'Unnamed'
        divorce_data = divorce_data.loc[:, ~divorce_data.columns.str.contains('^Unnamed')]
        unemployment_data = unemployment_data.loc[:, ~unemployment_data.columns.str.contains('^Unnamed')]

        # Reshape the Divorce Rate data (melt from wide to long format)
        divorce_data_melted = divorce_data.melt(id_vars=['State'], var_name='Year', value_name='DivorceRate')

        # Reshape the Unemployment Rate data (wide to long format)
        unemployment_data_melted = unemployment_data.melt(id_vars=['State/Area', 'Year'], var_name='Month', value_name='UnemploymentRate')

        # Convert to numeric, coercing errors to NaN
        unemployment_data_melted['UnemploymentRate'] = pd.to_numeric(unemployment_data_melted['UnemploymentRate'], errors='coerce')
        divorce_data_melted['DivorceRate'] = pd.to_numeric(divorce_data_melted['DivorceRate'], errors='coerce')

        # Group unemployment data by State and Year to get the average annual unemployment rate
        unemployment_data_annual = unemployment_data_melted.groupby(['State/Area', 'Year'])['UnemploymentRate'].mean().reset_index()

        # Ensure year columns are numeric
        divorce_data_melted['Year'] = pd.to_numeric(divorce_data_melted['Year'], errors='coerce')
        unemployment_data_annual['Year'] = pd.to_numeric(unemployment_data_annual['Year'], errors='coerce')

        # Rename 'State/Area' in unemployment data to 'State'
        unemployment_data_annual.rename(columns={'State/Area': 'State'}, inplace=True)

        # Merge datasets on 'State' and 'Year'
        merged_data = pd.merge(divorce_data_melted, unemployment_data_annual, on=['State', 'Year'], how='inner')

        # Drop rows with NaN values
        merged_data = merged_data.dropna(subset=['DivorceRate', 'UnemploymentRate'])

        # Initialize Streamlit app
        st.title("Divorce Rate vs. Unemployment Rate")

        # Get list of all states
        all_states = merged_data['State'].unique()

        # Multiselect widget for state selection with unique key
        selected_states = st.multiselect(
            "Select or Deselect States", all_states, default=[], key='divorce_unemployment_state_select'
        )

        # Buttons to select/deselect all states with unique keys
        if st.button("Select All States", key='select_all_states_button'):
            selected_states = all_states
        if st.button("Deselect All States", key='deselect_all_states_button'):
            selected_states = []

        # Slider for year selection with unique key
        min_year = int(merged_data['Year'].min())
        max_year = int(merged_data['Year'].max())
        selected_year_range = st.slider(
            "Select Year Range", min_year, max_year, (min_year, max_year), key='divorce_unemployment_year_slider'
        )

        # Filter data based on state and year selection
        filtered_data = merged_data[
            (merged_data['State'].isin(selected_states)) &
            (merged_data['Year'] >= selected_year_range[0]) &
            (merged_data['Year'] <= selected_year_range[1])
        ]

        # If no states are selected, show a message
        if len(selected_states) == 0:
            st.write("No states selected. Please select at least one state to view the plot.")
        else:
            # Calculate correlation
            correlation = filtered_data['DivorceRate'].corr(filtered_data['UnemploymentRate'])
            st.write(f"Correlation between Divorce Rate and Unemployment Rate: {correlation:.2f}")

            # Perform linear regression
            X = filtered_data['DivorceRate']
            y = filtered_data['UnemploymentRate']
            X = sm.add_constant(X)  # Add constant term for intercept

            model = sm.OLS(y, X).fit()  # Fit regression model
            filtered_data['RegressionLine'] = model.predict(X)  # Predict values

            # Plot with Plotly
            fig = px.scatter(
                filtered_data, 
                x='DivorceRate', 
                y='UnemploymentRate', 
                color='State',
                hover_data=['Year'],  # Add 'Year' to hover tooltip
                labels={
                    'DivorceRate': 'Divorce Rate', 
                    'UnemploymentRate': 'Unemployment Rate'
                },
                title=f'Divorce Rate vs. Unemployment Rate (Years {selected_year_range[0]}-{selected_year_range[1]})'
            )

            # Add regression line to the plot
            fig.add_traces(px.line(
                filtered_data, x='DivorceRate', y='RegressionLine', color_discrete_sequence=['red']
            ).data)

            # Show plot in Streamlit
            st.plotly_chart(fig)





def plot_imputed_divorce():

        # Load the dataset
        file_path = r'state-divorce-rates-90-95-00-22.xlsx'
        excel_data = pd.ExcelFile(file_path)

        # Load the data from the sheet
        df = excel_data.parse('Sheet1')

        # Set the 'States' column as the index for easier plotting
        df.set_index('States', inplace=True)

        # Convert the data to numeric, forcing errors to NaN
        df = df.apply(pd.to_numeric, errors='coerce')

        # Impute missing values by filling with column mean
        df.fillna(df.mean(), inplace=True)

        # Sort the columns (years) in ascending order
        df = df[sorted(df.columns)]

        # Initialize the Streamlit app with a title
        st.title(" Divorce Rates Heatmap (1990-2022)")

        # Get a list of all states
        all_states = df.index.tolist()  # Use index for state selection

        # Add multiselect widget for selecting states (no years)
        selected_states = st.multiselect("Select or Deselect States", all_states, default=[], key='state_select')

        # Add buttons to select all or no states
        if st.button("Select All States", key='select_all_states'):
            selected_states = all_states
        if st.button("Deselect All States", key='deselect_all_states'):
            selected_states = []

        # Filter the data based on selected states
        df_filtered = df.loc[selected_states]

        # If no states are selected, show a message
        if len(selected_states) == 0:
            st.write("No states selected. Please select at least one state to view the heatmap.")
        else:
            # Plotting with Plotly
            fig = px.imshow(df_filtered, 
                            labels=dict(x="Year", y="State", color="Divorce Rate"), 
                            x=df_filtered.columns, 
                            y=df_filtered.index, 
                            color_continuous_scale="YlGnBu", 
                            aspect="auto", 
                            title="Divorce Rates Heatmap (1990-2022)")

            # Show the interactive heatmap in Streamlit
            st.plotly_chart(fig)



def plot_imputed_marriage():
        # Load the dataset
        file_path = r'state-marriage-rates-90-95-00-22.xlsx'
        excel_data = pd.ExcelFile(file_path)

        # Load the data from the sheet
        df = excel_data.parse('Sheet2')

        # Set the 'States' column as the index for easier plotting
        df.set_index('States', inplace=True)

        # Convert the data to numeric, forcing errors to NaN
        df = df.apply(pd.to_numeric, errors='coerce')

        # Impute missing values by filling with column mean
        df.fillna(df.mean(), inplace=True)

        # Sort the columns (years) in ascending order
        df = df[sorted(df.columns)]

        # Initialize the Streamlit app with a title
        st.title(" Marriage Rates Heatmap (1990-2022)")

        # Get a list of all states
        all_states = df.index.tolist()  # Use index for state selection

        # Add multiselect widget for selecting states with a unique key
        selected_states = st.multiselect("Select or Deselect States", all_states, default=[], key='unique_state_select_marriage')

        # Add buttons to select all or no states
        if st.button("Select All States", key='select_all_states_marriage'):
            selected_states = all_states
        if st.button("Deselect All States", key='deselect_all_states_marriage'):
            selected_states = []

        # Filter the data based on selected states
        df_filtered = df.loc[selected_states]

        # If no states are selected, show a message
        if len(selected_states) == 0:
            st.write("No states selected. Please select at least one state to view the heatmap.")
        else:
            # Plotting with Plotly
            fig = px.imshow(df_filtered, 
                            labels=dict(x="Year", y="State", color="Marriage Rate"), 
                            x=df_filtered.columns, 
                            y=df_filtered.index, 
                            color_continuous_scale="YlGnBu", 
                            aspect="auto", 
                            title="Marriage Rates Heatmap (1990-2022)")

            # Show the interactive heatmap in Streamlit
            st.plotly_chart(fig)

def plot_miss_marriage():

        # Load the dataset
        file_path = r'C:/Users/Farshid/OneDrive - Michigan State University/courses/foundations of data science/project/working directory/state-marriage-rates-90-95-00-22.xlsx'
        excel_data = pd.ExcelFile(file_path)

        # Load the data from the sheet
        df = excel_data.parse('Sheet2')

        # Set the 'States' column as the index for easier plotting
        df.set_index('States', inplace=True)

        # Convert the data to numeric, forcing errors to NaN
        df = df.apply(pd.to_numeric, errors='coerce')

        # Transpose the data to make years the index and states as columns
        df_transposed = df.T

        # Create a boolean DataFrame indicating where the missing values are located (True = missing, False = not missing)
        missing_values_df = df_transposed.isnull()

        # Initialize the Streamlit app with a title
        st.title(" Missing Values Heatmap (Marriage Rates 1990-2022)")

        # Plot the missing values as a heatmap using Plotly
        fig = px.imshow(missing_values_df, 
                        labels=dict(x="State", y="Year", color="Missing"), 
                        x=missing_values_df.columns, 
                        y=missing_values_df.index, 
                        color_continuous_scale="Blues", 
                        aspect="auto", 
                        title="Missing Values in Marriage Rates (1990-2022)")

        # Show the interactive heatmap in Streamlit
        st.plotly_chart(fig)

        # Optionally, show the percentage of missing values per state
        st.write("### Percentage of Missing Values Per State")
        missing_percentages = missing_values_df.mean() * 100
        st.bar_chart(missing_percentages)

def plot_miss_divorce():

        # Load the dataset
        file_path = r'C:/Users/Farshid/OneDrive - Michigan State University/courses/foundations of data science/project/working directory/state-divorce-rates-90-95-00-22.xlsx'
        excel_data = pd.ExcelFile(file_path)

        # Load the data from the sheet
        df = excel_data.parse('Sheet1')

        # Set the 'States' column as the index for easier plotting
        df.set_index('States', inplace=True)

        # Convert the data to numeric, forcing errors to NaN
        df = df.apply(pd.to_numeric, errors='coerce')

        # Transpose the data to make years the index and states as columns
        df_transposed = df.T

        # Create a boolean DataFrame indicating where the missing values are located (True = missing, False = not missing)
        missing_values_df = df_transposed.isnull()

        # Initialize the Streamlit app with a title
        st.title(" Missing Values Heatmap (Divorce Rates 1990-2022)")

        # Plot the missing values as a heatmap using Plotly
        fig = px.imshow(missing_values_df, 
                        labels=dict(x="State", y="Year", color="Missing"), 
                        x=missing_values_df.columns, 
                        y=missing_values_df.index, 
                        color_continuous_scale="Blues", 
                        aspect="auto", 
                        title="Missing Values in Divorce Rates (1990-2022)")

        # Show the interactive heatmap in Streamlit
        st.plotly_chart(fig)

        # Optionally, show the percentage of missing values per state
        st.write("### Percentage of Missing Values Per State")
        missing_percentages = missing_values_df.mean() * 100
        st.bar_chart(missing_percentages)
