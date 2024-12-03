import pandas as pd
import plotly.express as px
import streamlit as st
import statsmodels.api as sm

def plot_divorce_rates():
    # Plot 2: Divorce Rates
    st.write("### Divorce Rates Over Time (1990-2022)")

    # Load the dataset (Divorce Rates)
    file_path = r'state-divorce-rates-90-95-00-22.xlsx'
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

        
        fig = px.line(df_filtered, x=df_filtered.index, y=df_filtered.columns, labels={'x': 'Year', 'value': 'Divorce Rate', 'variable': 'State'}, title='Divorce Rates Over Time')

        # Show the plot in Streamlit
        st.plotly_chart(fig)

        
def plot_marriage_rates():
        # Plot-specific code is placed entirely within this block for Option A
        st.write("### Marriage Rates Over Time (1990-2022)")
        # Load the dataset (adjust path as needed)
        file_path = r'state-marriage-rates-90-95-00-22.xlsx'
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

            
            fig = px.line(df_filtered, x=df_filtered.index, y=df_filtered.columns, labels={'x': 'Year', 'value': 'Marriage Rate', 'variable': 'State'}, title='Marriage Rates Over Time')

            # Show the plot in Streamlit
            st.plotly_chart(fig)


def plot_marriage_heat_map():
        # Plot-specific code is placed entirely within this block for Option A
        st.write("### Marriage Rates Heatmap (1990-2022)")

        # Load the dataset
        file_path = r'state-marriage-rates-90-95-00-22.xlsx'
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
        file_path = r'state-divorce-rates-90-95-00-22.xlsx'
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
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import streamlit as st
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
    file_path = r'state-marriage-rates-90-95-00-22.xlsx'
    excel_data = pd.ExcelFile(file_path)

    # Load the data from the sheet
    df = excel_data.parse('Sheet2')

    # Set the 'States' column as the index for easier plotting
    df.set_index('States', inplace=True)

    # Convert the data to numeric, forcing errors to NaN
    df = df.apply(pd.to_numeric, errors='coerce')

    # Initialize the Streamlit app with a title
    st.write("### Marriage Rates by State")

    # Add a dropdown for year selection
    year = st.selectbox("Select a Year", df.columns.tolist(), index=len(df.columns) - 1)

    # Reset index to get the States column back, and map full state names to abbreviations
    df.reset_index(inplace=True)
    df['State_Abbrev'] = df['States'].map(state_abbrev)

    # Check if there are any unmapped states (optional for debugging)
    unmapped_states = df[df['State_Abbrev'].isna()]
    if not unmapped_states.empty:
        st.write("The following states were not mapped:", unmapped_states)

    # Apply logarithmic transformation to the selected year's data
    df[f'{year}_log'] = df[year].apply(lambda x: np.log(x) if x > 0 else None)

    # Plotting the choropleth map using Plotly Express
    fig = px.choropleth(
        df,
        locations='State_Abbrev',  # Use state abbreviations for the locations
        locationmode='USA-states',  # Location mode (states of the USA)
        color=f'{year}_log',  # Log-transformed column for the selected year
        hover_name='States',  # Data to show on hover
        color_continuous_scale='Viridis',  # Color scale for the heatmap
        scope='usa',  # Restrict the map to the USA
        labels={f'{year}_log': f"Log(Marriage Rate) in {year}"},  # Label for the color bar
        title=f'Marriage Rates by State in {year} (Log Scale)'  # Title of the map
    )

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
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import streamlit as st
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
    file_path = r'state-divorce-rates-90-95-00-22.xlsx'
    excel_data = pd.ExcelFile(file_path)

    # Load the data from the sheet
    df = excel_data.parse('Sheet1')

    # Set the 'States' column as the index for easier plotting
    df.set_index('States', inplace=True)

    # Convert the data to numeric, forcing errors to NaN
    df = df.apply(pd.to_numeric, errors='coerce')

    # Initialize the Streamlit app with a title
    st.write("### Divorce Rates by State")

    # Add a dropdown for year selection with a unique key
    year = st.selectbox("Select a Year", df.columns.tolist(), index=len(df.columns) - 1, key='divorce_year_select')

    # Reset index to get the States column back, and map full state names to abbreviations
    df.reset_index(inplace=True)
    df['State_Abbrev'] = df['States'].map(state_abbrev)

    # Check if there are any unmapped states (optional for debugging)
    unmapped_states = df[df['State_Abbrev'].isna()]
    if not unmapped_states.empty:
        st.write("The following states were not mapped:", unmapped_states)

    # Apply logarithmic transformation to the selected year's data
    df[f'{year}_log'] = df[year].apply(lambda x: np.log(x) if x > 0 else None)

    # Plotting the choropleth map using Plotly Express
    fig = px.choropleth(
        df,
        locations='State_Abbrev',  # Use state abbreviations for the locations
        locationmode='USA-states',  # Location mode (states of the USA)
        color=f'{year}_log',  # Log-transformed column for the selected year
        hover_name='States',  # Data to show on hover
        color_continuous_scale='Viridis',  # Color scale for the heatmap
        scope='usa',  # Restrict the map to the USA
        labels={f'{year}_log': f"Log(Divorce Rate) in {year}"},  # Label for the color bar
        title=f'Divorce Rates by State in {year} (Log Scale)'  # Title of the map
    )

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
        st.write("### GDP Over Time for Selected States (All Industry)")

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
        st.write("### Average Unemployment Percent Over Time for Selected States")

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
    st.write("### GDP vs. Marriage Rate")

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
        st.write("### GDP vs. Divorce Rate")

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
    st.write("### Marriage Rate vs. Divorce Rate")

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
        st.write("### Normalized Divorce Rate by Marriage Rate Over Time")

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
    st.write("### Normalized Marriage Rate by Divorce Rate Over Time")

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
    st.write("### Marriage Rate vs. Unemployment Rate")

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
        st.write("### Divorce Rate vs. Unemployment Rate")

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
        st.write("### Divorce Rates Imputed Data Heatmap (1990-2022)")

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
        st.write("### Marriage Rates Imputed Data Heatmap (1990-2022)")

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
        file_path = r'state-marriage-rates-90-95-00-22.xlsx'
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
        st.write("### Missing Values Heatmap (Marriage Rates 1990-2022)")

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
        file_path = r'state-divorce-rates-90-95-00-22.xlsx'
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
        st.write("### Missing Values Heatmap (Divorce Rates 1990-2022)")

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


def plot_gdp_vs_divorce_with_ml():
    import pandas as pd
    import numpy as np
    import plotly.express as px
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.svm import SVR
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    import streamlit as st

    # Load datasets
    gdp_data = pd.read_csv(r'filtered_all_industry_gdp -since 2000.csv')
    divorce_data = pd.read_csv(r'state-divorce-rates-90-95-00-22.csv')

    # Remove unnecessary columns
    gdp_data = gdp_data.loc[:, ~gdp_data.columns.str.contains('^Unnamed')]
    divorce_data = divorce_data.loc[:, ~divorce_data.columns.str.contains('^Unnamed')]

    # Reshape the datasets
    gdp_data_melted = gdp_data.melt(id_vars=['State'], var_name='Year', value_name='GDP')
    divorce_data_melted = divorce_data.melt(id_vars=['State'], var_name='Year', value_name='DivorceRate')

    # Convert Year columns to numeric
    gdp_data_melted['Year'] = pd.to_numeric(gdp_data_melted['Year'], errors='coerce').astype(int)
    divorce_data_melted['Year'] = pd.to_numeric(divorce_data_melted['Year'], errors='coerce').astype(int)

    # Convert GDP and DivorceRate columns to numeric
    gdp_data_melted['GDP'] = pd.to_numeric(gdp_data_melted['GDP'], errors='coerce')
    divorce_data_melted['DivorceRate'] = pd.to_numeric(divorce_data_melted['DivorceRate'], errors='coerce')

    # Merge datasets
    merged_data = pd.merge(gdp_data_melted, divorce_data_melted, on=['State', 'Year'], how='inner')
    merged_data = merged_data.dropna(subset=['GDP', 'DivorceRate'])

    # Streamlit interface
    st.write("### GDP vs. Divorce Rate with Scaling")

    # Single State Selection
    all_states = merged_data['State'].unique()
    selected_state = st.selectbox("Select a State", options=all_states, key="gdp_state_selector")
    min_year = int(merged_data['Year'].min())
    max_year = int(merged_data['Year'].max())
    selected_year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year), key="gdp_year_slider")

    filtered_data = merged_data[
        (merged_data['State'] == selected_state) &
        (merged_data['Year'] >= selected_year_range[0]) &
        (merged_data['Year'] <= selected_year_range[1])
    ]

    if filtered_data.empty:
        st.write("No data available for the selected criteria.")
        return

    # Prepare data for ML
    X = filtered_data[['GDP']]
    y = filtered_data['DivorceRate']

    if X.empty or y.empty:
        st.write("No valid data available for modeling.")
        return

    # Scaling the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Select machine learning model
    model_choice = st.selectbox(
        "Select Machine Learning Model",
        ["Linear Regression", "Random Forest", "Support Vector Regression"],
        key="gdp_ml_model_selector"
    )

    if model_choice == "Linear Regression":
        model = LinearRegression()
    elif model_choice == "Random Forest":
        model = RandomForestRegressor(random_state=42)
    elif model_choice == "Support Vector Regression":
        model = SVR(kernel='rbf')
    else:
        st.write("Invalid Model Choice")
        return

    # Train the model
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Display metrics
    st.write("### Model Performance Metrics")
    st.write(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred):.2f}")
    st.write(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred):.2f}")
    st.write(f"R² Score: {r2_score(y_test, y_pred):.2f}")

    # Scatter plot with regression line
    st.write("### Scatter Plot")
    filtered_data['Predicted'] = model.predict(scaler.transform(filtered_data[['GDP']]))
    fig = px.scatter(
        filtered_data, 
        x='GDP', 
        y='DivorceRate', 
        color='State',
        hover_data=['Year'],
        title="GDP vs Divorce Rate with Predictions"
    )
    fig.add_traces(px.line(
        filtered_data, x='GDP', y='Predicted', color_discrete_sequence=['red']
    ).data)
    st.plotly_chart(fig)



def plot_divorce_vs_unemployment_with_ml():
    import pandas as pd
    import numpy as np
    import plotly.express as px
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.svm import SVR
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    import streamlit as st

    # Load datasets
    divorce_data = pd.read_csv(r'state-divorce-rates-90-95-00-22.csv')
    unemployment_data = pd.read_csv(r'Unemployment in America Per US State.csv')

    # Remove unnecessary columns
    divorce_data = divorce_data.loc[:, ~divorce_data.columns.str.contains('^Unnamed')]
    unemployment_data = unemployment_data.loc[:, ~unemployment_data.columns.str.contains('^Unnamed')]

    # Reshape the datasets
    divorce_data_melted = divorce_data.melt(id_vars=['State'], var_name='Year', value_name='DivorceRate')
    unemployment_data_melted = unemployment_data.melt(
        id_vars=['State/Area', 'Year'], var_name='Month', value_name='UnemploymentRate'
    )

    # Convert to numeric and group unemployment data
    divorce_data_melted['DivorceRate'] = pd.to_numeric(divorce_data_melted['DivorceRate'], errors='coerce')
    unemployment_data_melted['UnemploymentRate'] = pd.to_numeric(unemployment_data_melted['UnemploymentRate'], errors='coerce')
    unemployment_data_annual = unemployment_data_melted.groupby(['State/Area', 'Year'])['UnemploymentRate'].mean().reset_index()

    # Ensure Year is numeric
    divorce_data_melted['Year'] = pd.to_numeric(divorce_data_melted['Year'], errors='coerce').astype(int)
    unemployment_data_annual['Year'] = pd.to_numeric(unemployment_data_annual['Year'], errors='coerce').astype(int)

    # Rename columns for merging
    unemployment_data_annual.rename(columns={'State/Area': 'State'}, inplace=True)

    # Merge datasets
    merged_data = pd.merge(divorce_data_melted, unemployment_data_annual, on=['State', 'Year'], how='inner')
    merged_data = merged_data.dropna(subset=['DivorceRate', 'UnemploymentRate'])

    # Streamlit interface
    st.write("### Divorce Rate vs. Unemployment Rate with Scaling")

    # Single State Selection
    all_states = merged_data['State'].unique()
    selected_state = st.selectbox("Select a State", options=all_states, key="state_selector")
    min_year = int(merged_data['Year'].min())
    max_year = int(merged_data['Year'].max())
    selected_year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year), key="year_slider")

    filtered_data = merged_data[
        (merged_data['State'] == selected_state) &
        (merged_data['Year'] >= selected_year_range[0]) &
        (merged_data['Year'] <= selected_year_range[1])
    ]

    if filtered_data.empty:
        st.write("No data available for the selected criteria.")
        return

    # Prepare data for ML
    X = filtered_data.drop(columns=['UnemploymentRate', 'State', 'Year'], errors='ignore')
    y = filtered_data['UnemploymentRate']

    if X.empty or y.empty:
        st.write("No valid data available for modeling.")
        return

    # Scaling the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Select machine learning model
    model_choice = st.selectbox(
        "Select Machine Learning Model",
        ["Linear Regression", "Random Forest", "Support Vector Regression"],
        key="ml_model_selector"
    )

    if model_choice == "Linear Regression":
        model = LinearRegression()
    elif model_choice == "Random Forest":
        model = RandomForestRegressor(random_state=42)
    elif model_choice == "Support Vector Regression":
        model = SVR(kernel='rbf')
    else:
        st.write("Invalid Model Choice")
        return

    # Train the model
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Display metrics
    st.write("### Model Performance Metrics")
    st.write(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred):.2f}")
    st.write(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred):.2f}")
    st.write(f"R² Score: {r2_score(y_test, y_pred):.2f}")

    # Scatter plot with regression line
    st.write("### Scatter Plot")
    filtered_data['Predicted'] = model.predict(X_scaled)
    fig = px.scatter(
        filtered_data, 
        x='DivorceRate', 
        y='UnemploymentRate', 
        color='State',
        hover_data=['Year'],
        title="Divorce Rate vs Unemployment Rate with Predictions"
    )
    fig.add_traces(px.line(
        filtered_data, x='DivorceRate', y='Predicted', color_discrete_sequence=['red']
    ).data)
    st.plotly_chart(fig)




def forecast_gdp_with_arima_rf():
    import pandas as pd
    import numpy as np
    import streamlit as st
    import plotly.express as px
    import warnings
    from statsmodels.tsa.arima.model import ARIMA
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.preprocessing import StandardScaler
    from statsmodels.tsa.stattools import adfuller

    warnings.filterwarnings("ignore")  # To ignore warnings from statsmodels

    # Load GDP dataset
    gdp_data = pd.read_csv(r'filtered_all_industry_gdp -since 2000.csv')

    # Remove unnecessary columns
    gdp_data = gdp_data.loc[:, ~gdp_data.columns.str.contains('^Unnamed')]

    # Reshape GDP data (wide to long format)
    gdp_data_melted = gdp_data.melt(id_vars=['State'], var_name='Year', value_name='GDP')

    # Convert columns to numeric
    gdp_data_melted['Year'] = pd.to_numeric(gdp_data_melted['Year'], errors='coerce')
    gdp_data_melted['GDP'] = pd.to_numeric(gdp_data_melted['GDP'], errors='coerce')

    # Drop NaN values
    gdp_data_melted = gdp_data_melted.dropna()

    # Sort data by State and Year
    gdp_data_melted = gdp_data_melted.sort_values(by=['State', 'Year'])

    # Streamlit interface
    st.write("### Forecast GDP for 2021-2024 using ARIMA and RF Models")

    # Allow user to select states
    all_states = gdp_data_melted['State'].unique()
    selected_states = st.multiselect(
        "Select States", 
        all_states, 
        default=[], 
        key="unique_gdp_state_selector"
    )

    # Allow user to select forecasting method
    forecasting_methods = st.multiselect(
        "Select Forecasting Method(s)", 
        options=["ARIMA", "Random Forest (RF)", "Both"], 
        default=[],
        key="unique_forecast_gdp_method_selector"
    )

    if len(selected_states) == 0:
        st.write("Please select at least one state to view the forecast.")
        return

    if len(forecasting_methods) == 0:
        st.write("Please select at least one forecasting method.")
        return

    # Filter data for selected states
    filtered_data = gdp_data_melted[gdp_data_melted['State'].isin(selected_states)]

    # Forecasting for each state using selected methods
    forecast_results = []
    skipped_states = []

    for state in selected_states:
        st.subheader(f"Processing State: {state}")
        state_data = filtered_data[filtered_data['State'] == state]
        # Use data up to the latest available year for training
        max_year = state_data['Year'].max()
        training_data = state_data[state_data['Year'] <= max_year]['GDP'].values

        forecasted_years = [2021, 2022, 2023, 2024]

        # Check if we have enough data
        if len(training_data) < 10:
            st.warning(f"Not enough data for state: {state}. Skipping...")
            skipped_states.append(state)
            continue  # Skip to the next state

        # Proceed with models for states with sufficient data
        # Test for stationarity
        result = adfuller(training_data)
        if result[1] > 0.05:
            # Data is non-stationary, apply differencing
            data_to_use = np.diff(training_data)
            differenced = True
            d = 1
        else:
            differenced = False
            d = 0
            data_to_use = training_data

        # Scaling
        scaler = StandardScaler()
        scaled_values = scaler.fit_transform(data_to_use.reshape(-1, 1)).flatten()

        n_obs = len(scaled_values)

        # Initialize forecast arrays
        arima_forecast = [np.nan] * 4
        rf_forecast = [np.nan] * 4

        success = False  # Flag to check if at least one model succeeded

        if "ARIMA" in forecasting_methods or "Both" in forecasting_methods:
            try:
                # Manually set ARIMA parameters
                p = 1  # Autoregressive order
                q = 0  # Moving average order

                arima_model = ARIMA(scaled_values, order=(p, d, q)).fit()
                arima_forecast_scaled = arima_model.forecast(steps=4)
                arima_forecast_transformed = scaler.inverse_transform(arima_forecast_scaled.reshape(-1, 1)).flatten()

                # Reverse differencing if applied
                if differenced:
                    last_value = training_data[-1]
                    arima_forecast = np.cumsum(arima_forecast_transformed) + last_value
                else:
                    arima_forecast = arima_forecast_transformed
                success = True
            except Exception as e:
                st.warning(f"ARIMA model failed for state: {state} due to error: {e}. Skipping ARIMA forecast...")

        if "Random Forest (RF)" in forecasting_methods or "Both" in forecasting_methods:
            # Create lagged features
            n_lags = min(4, n_obs - 1)
            if n_lags < 1:
                st.warning(f"Not enough data to create lagged features for RF model for state: {state}. Skipping RF forecast...")
            else:
                df_rf = pd.DataFrame({'Value': scaled_values})
                for lag in range(1, n_lags + 1):
                    df_rf[f'lag_{lag}'] = df_rf['Value'].shift(lag)
                df_rf.dropna(inplace=True)
                if len(df_rf) == 0:
                    st.warning(f"Not enough data after creating lagged features for RF model for state: {state}. Skipping RF forecast...")
                else:
                    X = df_rf[[f'lag_{lag}' for lag in range(1, n_lags + 1)]]
                    y = df_rf['Value']
                    try:
                        rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
                        rf_model.fit(X, y)

                        # Initialize list to hold future predictions
                        rf_forecast_scaled = []
                        last_features = X.iloc[-1].values.tolist()

                        for _ in range(4):  # Predict next 4 values
                            predicted_value = rf_model.predict([last_features])[0]
                            rf_forecast_scaled.append(predicted_value)
                            # Update last_features
                            if n_lags > 1:
                                last_features = last_features[1:] + [predicted_value]
                            else:
                                last_features = [predicted_value]

                        rf_forecast_transformed = scaler.inverse_transform(np.array(rf_forecast_scaled).reshape(-1, 1)).flatten()

                        # Reverse differencing if applied
                        if differenced:
                            last_value = training_data[-1]
                            rf_forecast = np.cumsum(rf_forecast_transformed) + last_value
                        else:
                            rf_forecast = rf_forecast_transformed
                        success = True
                    except Exception as e:
                        st.warning(f"RF model failed for state: {state} due to error: {e}. Skipping RF forecast...")

        if not success:
            st.warning(f"Both models failed for state: {state}. Skipping...")
            skipped_states.append(state)
            continue

        # Create DataFrame for forecasts
        forecast_df = pd.DataFrame({
            'State': [state] * 4,
            'Year': forecasted_years,
            'ARIMA_Forecast': arima_forecast,
            'RF_Forecast': rf_forecast
        })
        forecast_results.append(forecast_df)

    # Combine all forecast results into a single DataFrame
    if forecast_results:
        forecast_df = pd.concat(forecast_results)

        # Combine actual and forecasted data for plotting
        actual_data = filtered_data[['State', 'Year', 'GDP']].rename(columns={'GDP': 'Value'})
        actual_data['Type'] = 'Actual'

        combined_data = [actual_data]

        if "ARIMA" in forecasting_methods or "Both" in forecasting_methods:
            arima_data = forecast_df[['State', 'Year', 'ARIMA_Forecast']].rename(columns={'ARIMA_Forecast': 'Value'})
            arima_data = arima_data.dropna()
            arima_data['Type'] = 'ARIMA Forecast'
            combined_data.append(arima_data)

        if "Random Forest (RF)" in forecasting_methods or "Both" in forecasting_methods:
            rf_data = forecast_df[['State', 'Year', 'RF_Forecast']].rename(columns={'RF_Forecast': 'Value'})
            rf_data = rf_data.dropna()
            rf_data['Type'] = 'RF Forecast'
            combined_data.append(rf_data)

        combined_data = pd.concat(combined_data)

        # Drop NaN values
        combined_data = combined_data.dropna()

        # Plot the results
        fig = px.line(
            combined_data,
            x='Year',
            y='Value',
            color='State',
            line_dash='Type',
            title="GDP Forecast (2021-2024) for Selected States using ARIMA and RF Models",
            labels={'Value': 'GDP (Millions of Current Dollars)'}
        )
        st.plotly_chart(fig)

        # Display the list of states that were skipped
        if skipped_states:
            st.write("**Note:** The following states were skipped due to insufficient data or modeling issues:")
            st.write(", ".join(skipped_states))
    else:
        st.write("No forecasts were generated due to insufficient data or modeling issues.")







def forecast_unemployment_with_arima_rf():
    import pandas as pd
    import numpy as np
    import streamlit as st
    import plotly.express as px
    import warnings
    from statsmodels.tsa.arima.model import ARIMA
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.preprocessing import StandardScaler
    from statsmodels.tsa.stattools import adfuller

    warnings.filterwarnings("ignore")  # To ignore warnings from statsmodels

    # Load unemployment dataset
    unemployment_data = pd.read_csv(r'Unemployment in America Per US State.csv')

    # Remove unnecessary columns
    unemployment_data = unemployment_data.loc[:, ~unemployment_data.columns.str.contains('^Unnamed')]

    # Reshape unemployment data (wide to long format)
    unemployment_data_melted = unemployment_data.melt(
        id_vars=['State/Area', 'Year'],
        var_name='Month',
        value_name='UnemploymentRate'
    )

    # Convert columns to numeric
    unemployment_data_melted['UnemploymentRate'] = pd.to_numeric(unemployment_data_melted['UnemploymentRate'], errors='coerce')
    unemployment_data_melted['Year'] = pd.to_numeric(unemployment_data_melted['Year'], errors='coerce')

    # Calculate annual average unemployment rate for each state
    unemployment_annual = unemployment_data_melted.groupby(['State/Area', 'Year'])['UnemploymentRate'].mean().reset_index()
    unemployment_annual.rename(columns={'State/Area': 'State'}, inplace=True)

    # Drop NaN values
    unemployment_annual = unemployment_annual.dropna()

    # Sort data by State and Year
    unemployment_annual = unemployment_annual.sort_values(by=['State', 'Year'])

    # Streamlit interface
    st.write("### Forecast Unemployment Rate for 2023-2026 using ARIMA and RF Models")

    # Allow user to select states
    all_states = unemployment_annual['State'].unique()
    selected_states = st.multiselect("Select States", all_states, default=[], key="unemployment_state_selector")

    # Allow user to select forecasting method
    forecasting_methods = st.multiselect(
        "Select Forecasting Method(s)",
        options=["ARIMA", "Random Forest (RF)", "Both"],
        default=[],
        key="forecast_unemployment_method_selector"
    )

    if len(selected_states) == 0:
        st.write("Please select at least one state to view the forecast.")
        return

    if len(forecasting_methods) == 0:
        st.write("Please select at least one forecasting method.")
        return

    # Filter data for selected states
    filtered_data = unemployment_annual[unemployment_annual['State'].isin(selected_states)]

    # Forecasting for each state using selected methods
    forecast_results = []
    skipped_states = []

    for state in selected_states:
        st.subheader(f"Processing State: {state}")
        state_data = filtered_data[filtered_data['State'] == state]
        # Use data up to the latest available year for training
        max_year = state_data['Year'].max()
        training_data = state_data[state_data['Year'] <= max_year]['UnemploymentRate'].values

        forecasted_years = [2023, 2024, 2025, 2026]

        # Check if we have enough data
        if len(training_data) < 10:
            st.warning(f"Not enough data for state: {state}. Skipping...")
            skipped_states.append(state)
            continue  # Skip to the next state

        # Proceed with models for states with sufficient data
        # Test for stationarity
        result = adfuller(training_data)
        if result[1] > 0.05:
            # Data is non-stationary, apply differencing
            data_to_use = np.diff(training_data)
            differenced = True
            d = 1
        else:
            differenced = False
            d = 0
            data_to_use = training_data

        # Scaling
        scaler = StandardScaler()
        scaled_values = scaler.fit_transform(data_to_use.reshape(-1, 1)).flatten()

        n_obs = len(scaled_values)

        # Initialize forecast arrays
        arima_forecast = [np.nan] * 4
        rf_forecast = [np.nan] * 4

        success = False  # Flag to check if at least one model succeeded

        if "ARIMA" in forecasting_methods or "Both" in forecasting_methods:
            try:
                # Manually set ARIMA parameters
                p = 1  # Autoregressive order
                q = 0  # Moving average order

                arima_model = ARIMA(scaled_values, order=(p, d, q)).fit()
                arima_forecast_scaled = arima_model.forecast(steps=4)
                arima_forecast_transformed = scaler.inverse_transform(arima_forecast_scaled.reshape(-1, 1)).flatten()

                # Reverse differencing if applied
                if differenced:
                    last_value = training_data[-1]
                    arima_forecast = np.cumsum(arima_forecast_transformed) + last_value
                else:
                    arima_forecast = arima_forecast_transformed
                success = True
            except Exception as e:
                st.warning(f"ARIMA model failed for state: {state} due to error: {e}. Skipping ARIMA forecast...")

        if "Random Forest (RF)" in forecasting_methods or "Both" in forecasting_methods:
            # Create lagged features
            n_lags = min(4, n_obs - 1)
            if n_lags < 1:
                st.warning(f"Not enough data to create lagged features for RF model for state: {state}. Skipping RF forecast...")
            else:
                df_rf = pd.DataFrame({'Value': scaled_values})
                for lag in range(1, n_lags + 1):
                    df_rf[f'lag_{lag}'] = df_rf['Value'].shift(lag)
                df_rf.dropna(inplace=True)
                if len(df_rf) == 0:
                    st.warning(f"Not enough data after creating lagged features for RF model for state: {state}. Skipping RF forecast...")
                else:
                    X = df_rf[[f'lag_{lag}' for lag in range(1, n_lags + 1)]]
                    y = df_rf['Value']
                    try:
                        rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
                        rf_model.fit(X, y)

                        # Initialize list to hold future predictions
                        rf_forecast_scaled = []
                        last_features = X.iloc[-1].values.tolist()

                        for _ in range(4):  # Predict next 4 values
                            predicted_value = rf_model.predict([last_features])[0]
                            rf_forecast_scaled.append(predicted_value)
                            # Update last_features
                            if n_lags > 1:
                                last_features = last_features[1:] + [predicted_value]
                            else:
                                last_features = [predicted_value]

                        rf_forecast_transformed = scaler.inverse_transform(np.array(rf_forecast_scaled).reshape(-1, 1)).flatten()

                        # Reverse differencing if applied
                        if differenced:
                            last_value = training_data[-1]
                            rf_forecast = np.cumsum(rf_forecast_transformed) + last_value
                        else:
                            rf_forecast = rf_forecast_transformed
                        success = True
                    except Exception as e:
                        st.warning(f"RF model failed for state: {state} due to error: {e}. Skipping RF forecast...")

        if not success:
            st.warning(f"Both models failed for state: {state}. Skipping...")
            skipped_states.append(state)
            continue

        # Create DataFrame for forecasts
        forecast_df = pd.DataFrame({
            'State': [state] * 4,
            'Year': forecasted_years,
            'ARIMA_Forecast': arima_forecast,
            'RF_Forecast': rf_forecast
        })
        forecast_results.append(forecast_df)

    # Combine all forecast results into a single DataFrame
    if forecast_results:
        forecast_df = pd.concat(forecast_results)

        # Combine actual and forecasted data for plotting
        actual_data = filtered_data[['State', 'Year', 'UnemploymentRate']].rename(columns={'UnemploymentRate': 'Value'})
        actual_data['Type'] = 'Actual'

        combined_data = [actual_data]

        if "ARIMA" in forecasting_methods or "Both" in forecasting_methods:
            arima_data = forecast_df[['State', 'Year', 'ARIMA_Forecast']].rename(columns={'ARIMA_Forecast': 'Value'})
            arima_data = arima_data.dropna()
            arima_data['Type'] = 'ARIMA Forecast'
            combined_data.append(arima_data)

        if "Random Forest (RF)" in forecasting_methods or "Both" in forecasting_methods:
            rf_data = forecast_df[['State', 'Year', 'RF_Forecast']].rename(columns={'RF_Forecast': 'Value'})
            rf_data = rf_data.dropna()
            rf_data['Type'] = 'RF Forecast'
            combined_data.append(rf_data)

        combined_data = pd.concat(combined_data)

        # Drop NaN values
        combined_data = combined_data.dropna()

        # Plot the results
        fig = px.line(
            combined_data,
            x='Year',
            y='Value',
            color='State',
            line_dash='Type',
            title="Unemployment Rate Forecast (2023-2026) for Selected States using ARIMA and RF Models",
            labels={'Value': 'Unemployment Rate (%)'}
        )
        st.plotly_chart(fig)

        # Display the list of states that were skipped
        if skipped_states:
            st.write("**Note:** The following states were skipped due to insufficient data or modeling issues:")
            st.write(", ".join(skipped_states))
    else:
        st.write("No forecasts were generated due to insufficient data or modeling issues.")









def forecast_marriage_divorce_rate_with_arima_rf():
    import pandas as pd
    import numpy as np
    import streamlit as st
    import plotly.express as px
    import warnings
    from statsmodels.tsa.arima.model import ARIMA
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.preprocessing import StandardScaler
    from statsmodels.tsa.stattools import adfuller

    warnings.filterwarnings("ignore")  # To ignore warnings from statsmodels

    # File paths for marriage and divorce rates
    marriage_file_path = r'state-marriage-rates-90-95-00-22.xlsx'
    divorce_file_path = r'state-divorce-rates-90-95-00-22.xlsx'

    st.write("### Forecast Marriage and Divorce Rates (2023-2026)")

    # Load and preprocess marriage rate data
    marriage_data = pd.read_excel(marriage_file_path, sheet_name='Sheet2')
    marriage_data.set_index('States', inplace=True)
    marriage_data = marriage_data.apply(pd.to_numeric, errors='coerce')
    marriage_data_transposed = marriage_data.T
    marriage_data_transposed.index = marriage_data_transposed.index.astype(int)
    marriage_data_transposed.dropna(how='all', axis=1, inplace=True)
    marriage_data_transposed.sort_index(inplace=True)

    # Load and preprocess divorce rate data
    divorce_data = pd.read_excel(divorce_file_path, sheet_name='Sheet1')
    divorce_data.set_index('States', inplace=True)
    divorce_data = divorce_data.apply(pd.to_numeric, errors='coerce')
    divorce_data_transposed = divorce_data.T
    divorce_data_transposed.index = divorce_data_transposed.index.astype(int)
    divorce_data_transposed.dropna(how='all', axis=1, inplace=True)
    divorce_data_transposed.sort_index(inplace=True)

    # Allow the user to select states and the target variable
    all_states = sorted(list(set(marriage_data_transposed.columns).union(divorce_data_transposed.columns)))

    selected_states = st.multiselect(
        "Select States for Forecasting",
        all_states,
        default=[]
    )

    target_variable = st.radio(
        "Select Target Variable",
        options=["Marriage Rates", "Divorce Rates"],
        index=0,
        key="forecast_target_selector"
    )

    # Add model selection
    model_type = st.radio(
        "Select Forecasting Model",
        options=["ARIMA", "Random Forest", "Both"],
        index=0,
        key="forecast_model_selector"
    )

    if len(selected_states) == 0:
        st.write("No states selected. Please select at least one state to view the forecast.")
        return

    # Select appropriate dataset based on the target variable
    if target_variable == "Marriage Rates":
        target_data = marriage_data_transposed
        title_prefix = "Marriage Rates"
    else:
        target_data = divorce_data_transposed
        title_prefix = "Divorce Rates"

    # Update forecast years to start from 2022
    forecast_years = [2023, 2024, 2025, 2026]
    forecast_results = []

    # Keep track of states that couldn't be processed
    skipped_states = []

    # Forecast for each state using the selected model
    for state in selected_states:
        st.subheader(f"Processing State: {state}")

        # Get state data and handle missing values
        if state in target_data.columns:
            state_series = target_data[state].dropna()
        else:
            st.warning(f"No data available for state: {state}. Skipping...")
            continue

        if len(state_series) < 10:  # Ensure at least 10 data points for forecasting
            st.warning(f"Not enough data for state: {state}. Skipping...")
            skipped_states.append(state)
            continue  # Skip to next state

        # Focus on the last 15 years for training
        state_series = state_series[-15:] if len(state_series) > 15 else state_series

        # Reset index to ensure continuous time steps
        state_series = state_series.reset_index()
        state_series.columns = ['Year', 'Value']

        # Test for stationarity
        result = adfuller(state_series['Value'])
        if result[1] > 0.05:
            differenced = True
            d = 1  # Degree of differencing
            data_to_use = state_series['Value'].diff().dropna().values
        else:
            differenced = False
            d = 0
            data_to_use = state_series['Value'].values

        # Scaling
        scaler = StandardScaler()
        scaled_values = scaler.fit_transform(data_to_use.reshape(-1, 1)).flatten()

        n_obs = len(scaled_values)

        success = False  # Flag to check if at least one model succeeded

        # ARIMA Model
        if model_type in ["ARIMA", "Both"]:
            try:
                # Manually set ARIMA parameters
                p = 1  # Autoregressive order
                q = 0  # Moving average order

                arima_model = ARIMA(scaled_values, order=(p, d, q)).fit()
                arima_forecast_scaled = arima_model.forecast(steps=4)
                arima_forecast = scaler.inverse_transform(arima_forecast_scaled.reshape(-1, 1)).flatten()

                # Reverse differencing if applied
                if differenced:
                    last_value = state_series['Value'].iloc[-1]
                    arima_forecast = np.cumsum(arima_forecast) + last_value

                forecast_results.append(pd.DataFrame({
                    'Year': forecast_years,
                    'Value': arima_forecast,
                    'State': state,
                    'Model': 'ARIMA'
                }))
                success = True
            except Exception as e:
                st.warning(f"ARIMA model failed for state: {state} due to error: {e}. Skipping ARIMA forecast...")

        # Random Forest Model
        if model_type in ["Random Forest", "Both"]:
            # Create lagged features
            n_lags = min(4, n_obs - 1)  # Ensure we have enough data
            if n_lags < 1:
                st.warning(f"Not enough data to create lagged features for state: {state}. Skipping Random Forest forecast...")
            else:
                df_rf = pd.DataFrame({'Value': scaled_values})
                for lag in range(1, n_lags + 1):
                    df_rf[f'lag_{lag}'] = df_rf['Value'].shift(lag)
                df_rf.dropna(inplace=True)
                if len(df_rf) == 0:
                    st.warning(f"Not enough data after creating lagged features for state: {state}. Skipping Random Forest forecast...")
                else:
                    X = df_rf[[f'lag_{lag}' for lag in range(1, n_lags + 1)]]
                    y = df_rf['Value']
                    try:
                        # Fit Random Forest
                        rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
                        rf_model.fit(X, y)

                        # Initialize list to hold future predictions
                        rf_forecast_scaled = []
                        last_features = X.iloc[-1].values.tolist()

                        for _ in range(4):  # Predict next 4 values
                            predicted_value = rf_model.predict([last_features])[0]
                            rf_forecast_scaled.append(predicted_value)
                            # Update last_features
                            if n_lags > 1:
                                last_features = last_features[1:] + [predicted_value]
                            else:
                                last_features = [predicted_value]

                        rf_forecast = scaler.inverse_transform(np.array(rf_forecast_scaled).reshape(-1, 1)).flatten()

                        # Reverse differencing if applied
                        if differenced:
                            last_value = state_series['Value'].iloc[-1]
                            rf_forecast = np.cumsum(rf_forecast) + last_value

                        forecast_results.append(pd.DataFrame({
                            'Year': forecast_years,
                            'Value': rf_forecast,
                            'State': state,
                            'Model': 'Random Forest'
                        }))
                        success = True
                    except Exception as e:
                        st.warning(f"Random Forest model failed for state: {state} due to error: {e}. Skipping Random Forest forecast...")

        if not success:
            st.warning(f"All models failed for state: {state}. Skipping...")
            skipped_states.append(state)
            continue

    # Combine forecast results into a single DataFrame
    if forecast_results:
        forecast_df = pd.concat(forecast_results)

        # Combine actual data and forecasted data for plotting
        historical_data = target_data[selected_states].reset_index().melt(
            id_vars='index',
            var_name='State',
            value_name='Value'
        ).rename(columns={'index': 'Year'})
        historical_data['Type'] = 'Actual'
        forecast_df['Type'] = 'Forecast'
        combined_data = pd.concat([historical_data, forecast_df])

        # Ensure Year is numeric for sorting and plotting
        combined_data['Year'] = pd.to_numeric(combined_data['Year'], errors='coerce')

        # Adjust 'Model' for historical data
        combined_data['Model'] = combined_data['Model'].fillna('Historical')

        # Plot the results in a single plot
        fig = px.line(
            combined_data,
            x='Year',
            y='Value',
            color='State',
            line_dash='Type',
            symbol='Model',
            title=f"{title_prefix} Forecast (2023-2026) with Historical Data for Selected States",
            labels={'Value': f'{title_prefix} (%)'}
        )
        st.plotly_chart(fig, use_container_width=True)

        # Display the list of states that were skipped
        if skipped_states:
            st.write("**Note:** The following states were skipped due to insufficient data or modeling issues:")
            st.write(", ".join(skipped_states))
    else:
        st.write("No forecasts were generated due to insufficient data or modeling issues.")






def analyze_marriage_divorce_with_filters():
    st.write("### Analyze Marriage and Divorce Rates by GDP and Unemployment (3D Scatter)")

    # File paths for datasets
    marriage_file_path = r'state-marriage-rates-90-95-00-22.xlsx'
    divorce_file_path = r'state-divorce-rates-90-95-00-22.xlsx'
    gdp_file_path = r'filtered_all_industry_gdp -since 2000.csv'
    unemployment_file_path = r'Unemployment in America Per US State.csv'

    # Load and preprocess marriage rate data
    marriage_data = pd.read_excel(marriage_file_path, sheet_name='Sheet2')  
    marriage_data.set_index('States', inplace=True)
    marriage_data = marriage_data.apply(pd.to_numeric, errors='coerce')
    marriage_data_transposed = marriage_data.T
    marriage_data_transposed.index = marriage_data_transposed.index.astype(int)
    marriage_data_transposed.dropna(how='all', axis=1, inplace=True)

    # Load and preprocess divorce rate data
    divorce_data = pd.read_excel(divorce_file_path, sheet_name='Sheet1')  
    divorce_data.set_index('States', inplace=True)
    divorce_data = divorce_data.apply(pd.to_numeric, errors='coerce')
    divorce_data_transposed = divorce_data.T
    divorce_data_transposed.index = divorce_data_transposed.index.astype(int)
    divorce_data_transposed.dropna(how='all', axis=1, inplace=True)

    # Load and preprocess GDP data
    gdp_data = pd.read_csv(gdp_file_path)
    gdp_data = gdp_data.melt(id_vars=['State'], var_name='Year', value_name='GDP')
    gdp_data['Year'] = pd.to_numeric(gdp_data['Year'], errors='coerce')
    gdp_data['GDP'] = pd.to_numeric(gdp_data['GDP'], errors='coerce')

    # Load and preprocess unemployment data
    unemployment_data = pd.read_csv(unemployment_file_path)
    unemployment_data = unemployment_data.melt(id_vars=['State/Area', 'Year'], var_name='Month', value_name='UnemploymentRate')
    unemployment_data['UnemploymentRate'] = pd.to_numeric(unemployment_data['UnemploymentRate'], errors='coerce')
    unemployment_data = unemployment_data.groupby(['State/Area', 'Year'])['UnemploymentRate'].mean().reset_index()
    unemployment_data.rename(columns={'State/Area': 'State'}, inplace=True)

    # Merge GDP and unemployment datasets
    combined_data = pd.merge(gdp_data, unemployment_data, on=['State', 'Year'], how='inner')

    # Initialize state selection
    all_states = sorted(list(set(marriage_data_transposed.columns).intersection(divorce_data_transposed.columns)))
    selected_state = st.selectbox("Select a State", all_states, key="state_selector_3d")

    if not selected_state:
        st.write("Please select a state to proceed.")
        return

    # Filter GDP and unemployment for the selected state
    state_gdp_data = combined_data[combined_data['State'] == selected_state]
    gdp_range = st.slider("Select GDP Range", 
                          float(state_gdp_data['GDP'].min()), 
                          float(state_gdp_data['GDP'].max()), 
                          (float(state_gdp_data['GDP'].min()), float(state_gdp_data['GDP'].max())),
                          key="gdp_slider_3d")
    unemployment_range = st.slider("Select Unemployment Rate Range",
                                   float(state_gdp_data['UnemploymentRate'].min()), 
                                   float(state_gdp_data['UnemploymentRate'].max()), 
                                   (float(state_gdp_data['UnemploymentRate'].min()), float(state_gdp_data['UnemploymentRate'].max())),
                                   key="unemployment_slider_3d")

    # Filter data based on the selected ranges
    filtered_data = state_gdp_data[
        (state_gdp_data['GDP'] >= gdp_range[0]) & 
        (state_gdp_data['GDP'] <= gdp_range[1]) & 
        (state_gdp_data['UnemploymentRate'] >= unemployment_range[0]) & 
        (state_gdp_data['UnemploymentRate'] <= unemployment_range[1])
    ]

    if filtered_data.empty:
        st.write(f"No data available for {selected_state} in the selected GDP and Unemployment range.")
        return

    # Select target variable: Marriage or Divorce rates
    target_variable = st.radio(
        "Select Target Variable",
        options=["Marriage Rates", "Divorce Rates"],
        index=0,
        key="target_variable_selector_3d"
    )

    # Get corresponding rate data
    if target_variable == "Marriage Rates":
        target_data = marriage_data_transposed[[selected_state]].reset_index().rename(columns={selected_state: 'Rate'})
        title = "Marriage Rates Over Time"
    else:
        target_data = divorce_data_transposed[[selected_state]].reset_index().rename(columns={selected_state: 'Rate'})
        title = "Divorce Rates Over Time"

    target_data['Year'] = target_data['index']
    target_data.drop(columns=['index'], inplace=True)

    # Combine filtered GDP/Unemployment with target variable
    final_data = pd.merge(target_data, filtered_data, on='Year', how='inner')

    # Plot results as a 3D scatter plot
    fig = px.scatter_3d(
        final_data,
        x="Rate",
        y="UnemploymentRate",
        z="GDP",
        color="Year",
        hover_data=["Year", "GDP", "UnemploymentRate"],
        title=f"{title} vs GDP and Unemployment in {selected_state}",
        labels={
            "Rate": target_variable,
            "UnemploymentRate": "Unemployment Rate (%)",
            "GDP": "GDP (Millions of Current Dollars)"
        }
    )

    st.plotly_chart(fig, use_container_width=True)









































