import pandas as pd
import plotly.express as px
import streamlit as st
import sys
sys.path.append(r'C:/Users/kassaeif/OneDrive - Michgan State University/courses/foundations of data science/project/working directory')
from plot_functions import plot_marriage_rates
from plot_functions import plot_divorce_rates
from plot_functions import plot_marriage_heat_map
from plot_functions import plot_divorce_heat_map
from plot_functions import plot_marriage_heat_map_year
from plot_functions import plot_divorce_heat_map_year
from plot_functions import plot_gdp
from plot_functions import plot_unemployment
from plot_functions import plot_gdp_vs_marriage
from plot_functions import plot_gdp_vs_divorce
from plot_functions import plot_marriage_vs_divorce
from plot_functions import plot_norm_marriage_vs_divorce
from plot_functions import plot_norm_divorce_vs_marriage
from plot_functions import plot_unemp_vs_marriage
from plot_functions import plot_unemp_vs_divorce
from plot_functions import plot_imputed_divorce
from plot_functions import plot_imputed_marriage
from plot_functions import plot_miss_marriage
from plot_functions import plot_miss_divorce

# Sidebar menus
st.sidebar.header("Foundations of Data Science Midterm Project")

# First dropdown menu in the sidebar for main sections (default to "Introduction")
menu_1 = st.sidebar.selectbox(
    "Select a section",
    ["Introduction", "Dataset overview", "Data Analysis", "Conclusion"],
    key="menu_1",
    index=0  # This sets "Introduction" as the default selection
)

# Second dropdown menu in the sidebar for additional options
menu_2 = st.sidebar.selectbox(
    "Select an interactive graph",
    ["Raw Data","Missing Data", "Imputation", "Correlation", "Regression"],
    key="menu_2"
)

# Initialize session state for tracking the last selected menu
if "last_selected" not in st.session_state:
    st.session_state.last_selected = "menu_1"  # Default to menu_1 (Introduction) on load

# Logic to detect changes in menu selection
if st.session_state.get("prev_menu_1") != menu_1:
    st.session_state.last_selected = "menu_1"
    st.session_state.prev_menu_1 = menu_1  # Update the previous value for menu_1

elif st.session_state.get("prev_menu_2") != menu_2:
    st.session_state.last_selected = "menu_2"
    st.session_state.prev_menu_2 = menu_2  # Update the previous value for menu_2

# Display content based on the most recent selection
if st.session_state.last_selected == "menu_1":
    # Content for menu_1
    if menu_1 == "Introduction":
        st.title("Marriage and Divorce Rates in the United States Over Time")
        st.image("https://jokesoftheday.net/jokes-archive/2020/03/29/Married-or-Divorced.jpg", caption="Downloaded from google")
        st.write("Introduction")
        st.write("""
        Marriage and divorce are integral aspects of social and family structures, often influenced by various economic factors. While marriage traditionally symbolizes stability, companionship, and societal cohesion, divorce can reflect shifts in personal and socio-economic circumstances. One of the most notable influences on marriage and divorce trends is the economy, with indicators like Gross Domestic Product (GDP) and unemployment rates playing a key role.
        GDP, which reflects the overall economic health of a country, can influence marriage and divorce rates in multiple ways. In periods of economic growth, people may feel more financially secure, encouraging decisions like marriage. Conversely, economic downturns, marked by falling GDP, can increase stress within households, potentially leading to a rise in divorce rates.
        Unemployment, another critical economic factor, is directly linked to financial stability. Higher unemployment rates often correlate with delayed marriages, as individuals may prioritize job security before making long-term commitments. Moreover, financial strain from unemployment can lead to tension in relationships, increasing the likelihood of divorce.
        In summary, marriage and divorce rates are not only personal choices but also mirror the broader economic conditions. Understanding their connection with GDP and unemployment provides valuable insights into societal trends and the impact of economic stability on family dynamics.
        """)
        

    elif menu_1 == "Dataset overview":
        st.title("Dataset overview")
        st.write("""
        The datasets in this research provide state-level statistics across the United States, focusing on economic output, social trends, and employment over time. The key parameters include state, year, marriage and divorce rates, unemployment rate, and GDP. The GDP dataset spans from 1997 to 2020, detailing the annual economic output of various states, helping track economic growth trends. The marriage and divorce data covers multiple years, including 1990, 1995, 2000, and 2022, showing marriage and divorce rates per 1,000 population for each state, which can help analyze shifts in societal trends over time. The unemployment dataset provides detailed labor force statistics, including employment, unemployment, and their percentages, with monthly data for multiple years. Together, these datasets offer insights into how states have evolved socially and economically, allowing users to explore patterns such as correlations between economic performance and marriage or divorce rates, or how unemployment rates shift with economic changes. The structure consists mainly of categorical data (state names) and numerical data (rates, GDP values, and counts), making them suitable for trend analysis and visualizations over time.
        """)

    elif menu_1 == "Data Analysis":
        st.title("Data Analysis")
        st.image(r"C:\Users\Farshid\OneDrive - Michigan State University\courses\foundations of data science\project\working directory\pic1.webp", caption="AI generated by chatGPT")
        st.write("""Since the datasets contain only categorical data (e.g., state names) and numerical data (e.g., GDP, marriage and divorce rates, unemployment rates), no encoding was required for analysis. To handle missing data, the mean value of numerical columns was used for imputation, as the amount of missing data was minimal and manageable. This ensured the datasets remained complete without significantly altering their distribution. Additionally, some columns were dropped during preprocessing because they were either irrelevant to the analysis or contained more than 90% missing values, making them impractical to retain. Since the unemployment dataset was reported monthly, it was averaged over the year to be used here. This cleaning process helped streamline the datasets, focusing only on the relevant parameters—state, year, GDP, marriage and divorce rates, and unemployment rates—while maintaining data quality and consistency for further analysis.""")

    elif menu_1 == "Conclusion":
        st.title("Conclusion")
        st.write("""
        The analysis of marriage, divorce, GDP, and unemployment trends across U.S. states reveals several interesting patterns. Both marriage rates and divorce rates have declined over the years, reflecting changing societal behaviors. However, when the divorce rate is normalized by the marriage rate, the ratio remains relatively constant over time, suggesting that while fewer people may be marrying, the proportion of marriages that end in divorce has stayed stable.

The GDP of the states has shown a steady increase over the years, indicating economic growth across the country. In contrast, the unemployment rate has experienced fluctuations. Notably, the unemployment rate peaked in 2010 due to the aftermath of the 2008 financial crisis, and again in 2020 as a result of the COVID-19 pandemic, both periods of economic downturn that disrupted employment across the nation.

The analysis also found correlations between GDP, unemployment, and divorce rates. In many states, as GDP increased, divorce rates decreased, suggesting that financial stability might reduce marital instability. Conversely, when unemployment rates increased, divorce rates tended to rise as well, possibly due to the financial and emotional stress caused by job loss. Furthermore, the marriage rate and divorce rate showed a positive correlation, indicating that higher numbers of marriages naturally lead to more divorces, even though the overall trend for both has been downward.

These insights highlight the complex interplay between economic conditions and social behaviors over time. Understanding these relationships can help policymakers and social researchers identify areas where support systems are needed, particularly during economic downturns, to mitigate the impact of financial stress on marriages. 

The most interesting observation I found was the correlation between divorce rates, GDP, and unemployment. As GDP increased, divorce rates decreased, suggesting that financial stability supports healthier relationships. In contrast, higher unemployment rates led to higher divorce rates, likely due to the stress caused by financial insecurity. These patterns highlight how both economic growth and downturns influence personal decisions. Economic hardship, such as the 2008 financial crisis and COVID-19 pandemic, not only disrupts employment but also affects marital stability. Understanding these relationships can help policymakers develop support systems to reduce the social impact of economic fluctuations on families.
        """)

elif st.session_state.last_selected == "menu_2":
    if menu_2 == "Raw Data":
        st.write("### Raw Data Overview")
        st.write("""
        This section provides an exploration of the raw data used in this project. 
        You can view trends in marriage and divorce rates, GDP, and unemployment data 
        through various heatmaps and state-level visualizations. These graphs help us 
        understand the underlying distributions and missing data patterns before applying 
        advanced techniques like imputation or regression.
        """)
        plot_marriage_rates()
        plot_divorce_rates()
        plot_marriage_heat_map()
        plot_divorce_heat_map()
        plot_marriage_heat_map_year()
        plot_divorce_heat_map_year()
        plot_gdp()
        plot_unemployment()

    elif menu_2 == "Missing Data":
        st.write("### Missing Data Overview")
        st.write("""  Missing data is a common issue in datasets and can significantly affect analysis outcomes 
        and model performance. Identifying and understanding patterns in missing data allows us 
        to make informed decisions about how to handle them. In this section, we explore the extent 
        of missing data in marriage and divorce datasets and discuss techniques like imputation 
        to minimize their impact on analysis. Addressing missing data ensures more reliable results 
        and helps maintain the integrity of statistical models.
        """)
        plot_miss_marriage()
        plot_miss_divorce()

    elif menu_2 == "Imputation":
        st.write("### Imputation Techniques")
        st.write("""
        In this section, we address missing data in marriage and divorce datasets using 
        imputation techniques. Handling missing data is essential for ensuring the accuracy 
        of the analysis. Explore how the imputed values align with observed trends and 
        improve the reliability of statistical models and visualizations.
        """)
        plot_imputed_marriage()
        plot_imputed_divorce()
        

    elif menu_2 == "Correlation":
        st.write("### Correlation Analysis")
        st.write("""
        This section explores the relationships between key variables, including marriage 
        and divorce rates, GDP, and unemployment. By examining correlations, we aim to 
        uncover meaningful insights into how economic factors influence social trends. 
        Visualizing these correlations can help us understand the strength and direction 
        of these associations.
        """)
        plot_marriage_vs_divorce()
        plot_gdp_vs_marriage()
        plot_unemp_vs_marriage()
        plot_norm_marriage_vs_divorce()
        plot_norm_divorce_vs_marriage()
        

    elif menu_2 == "Regression":
        st.write("### Regression Analysis")
        st.write("""
        This section focuses on regression models to quantify the impact of economic factors 
        on marriage and divorce rates. Using GDP and unemployment data, we build predictive 
        models to better understand the relationships between these variables. Regression 
        analysis helps us explore causality and predict trends under varying economic conditions.
        """)
        plot_gdp_vs_divorce()
        plot_unemp_vs_divorce()
