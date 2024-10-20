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
    "Select an interactive graph (Change the item to see graphs)",
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
        The datasets are taken from three different sources that are kaggle, The U.S. Bureau of Economic Analysis, and The National Center for Health Statistics. Here are the links to the references:""")
        st.markdown('[Marriage & Divorce Statistics](https://www.cdc.gov/nchs/nvss/marriage-divorce.htm?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnchs%2Fmardiv.htm)',unsafe_allow_html=True)
        st.markdown('[GDP per US state](https://apps.bea.gov/iTable/?isuri=1&reqid=151&step=1)',unsafe_allow_html=True)
        st.markdown('[Unemployment in America per US State](https://www.kaggle.com/datasets/justin2028/unemployment-in-america-per-us-state?resource=download)',unsafe_allow_html=True)

    elif menu_1 == "Data Analysis":
        st.title("Data Analysis")
        st.image(r"pic1.webp", caption="AI generated by chatGPT")
        st.write("""Since the datasets contain only categorical data (e.g., state names) and numerical data (e.g., GDP, marriage and divorce rates, unemployment rates), no encoding was required for analysis. To handle missing data, the mean value of numerical columns was used for imputation, as the amount of missing data was minimal and manageable. This ensured the datasets remained complete without significantly altering their distribution. Additionally, some columns were dropped during preprocessing because they were either irrelevant to the analysis or contained more than 50% missing values, making them impractical to retain. Since the unemployment dataset was reported monthly, it was averaged over the year to be used here. This cleaning process helped streamline the datasets, focusing only on the relevant parameters—state, year, GDP, marriage and divorce rates, and unemployment rates—while maintaining data quality and consistency for further analysis.""")

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
        advanced techniques like imputation or regression. Descriptions are written below each graph.
        """)
        plot_marriage_rates()
        st.write("This graph visualizes the marriage rates across U.S. states over time, highlighting trends or changes in marriage patterns. It offers a clear view of state-level variations, making it easy to compare how marriage rates evolve geographically.")
        plot_divorce_rates()
        st.write("This graph displays divorce rates over time across different U.S. states. It allows users to analyze trends, compare states, and identify periods with noticeable changes in divorce rates, revealing social patterns or policy impacts.")
        plot_marriage_heat_map()
        st.write("This heat map visualizes marriage rates across states, with colors representing intensity levels. It provides a quick overview of geographical patterns and helps users identify clusters of states with high or low marriage rates.")
        plot_divorce_heat_map()
        st.write("This heat map shows divorce rates across states, using color intensity to indicate rate levels. It allows users to spot regional patterns and compare divorce rates between states quickly, revealing potential cultural or policy influences.")
        plot_marriage_heat_map_year()
        st.write("This heat map focuses on marriage rates for specific years, helping users explore how marriage rates change over time. The yearly focus makes it easier to spot temporal shifts and key moments in state-level marriage patterns.")
        plot_divorce_heat_map_year()
        st.write("This heat map provides a detailed view of divorce rates for specific years. It helps users examine trends over time, comparing how divorce rates shift year by year across states, revealing social changes or policy effects.")
        plot_gdp()
        st.write("This graph plots the Gross Domestic Product (GDP) data across states, offering insights into economic performance. It helps users analyze trends, detect periods of growth or decline, and explore how GDP varies regionally or by sector.")
        plot_unemployment()
        st.write("This graph visualizes unemployment rates across U.S. states over time, highlighting trends and regional differences. It offers a valuable perspective on how unemployment varies, allowing users to track economic challenges or improvements across states. It can be obsereved that the unemployment rate has reached a peak value in 2010 and 2020 due to 2008 financial crisis and COVID respectively.")

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
        st.write("These graphs visualize missing data patterns in marriage and divorce rates across U.S. states and years, helping to identify whether data gaps are random or concentrated in specific regions or periods. Observations from these plots reveal potential data collection issues, especially if entire years or states are missing, suggesting structural gaps. In handling the missing data, I applied mean imputation, where missing values are replaced with the mean of available data for the corresponding state or year. This method is suitable when the missingness is not systematic and ensures the dataset remains complete for analysis and visualization. It should be noted that all data in one column has been dropped whenever more than 50% of the data in one column is missing.")

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
        st.write("These two plots visualize the marriage and divorce rates after applying imputation techniques to fill missing values. These graphs help assess how the imputed data aligns with observed trends, ensuring completeness without introducing bias. The imputation method used is mean imputation, where missing values are replaced with the mean of the corresponding state or year. This technique assumes the data is missing at random and preserves the overall distribution of the dataset. While mean imputation is simple and ensures no gaps, it may smooth out variability, potentially masking local or temporal fluctuations in the actual data trends. This technique was used since the number of missing values in the dataset was not high.")
        

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
        st.write("This plot compares marriage and divorce rates across U.S. states over time, highlighting the relationship between the two metrics. Observations may reveal whether higher marriage rates correlate with higher or lower divorce rates. Patterns such as an increase in divorces following spikes in marriages can reflect societal behaviors or economic influences. Certain states might show stable relationships, while others may have fluctuating trends. The plot offers insights into whether regions with strong marriage rates also experience higher divorce rates or if stable marriages are the norm in particular areas.")
        plot_gdp_vs_marriage()
        st.write("This graph examines the relationship between GDP and marriage rates, helping to identify whether economic performance influences marriage patterns. A positive correlation might indicate that higher economic growth encourages marriage, while downturns could show declining marriage rates. The plot allows for cross-state comparisons to determine if wealthier regions have higher marriage rates. Observations may also reveal time-specific trends, such as marriage rates responding to economic recessions or booms, providing insights into how financial stability or uncertainty affects social decisions like marriage.")
        plot_unemp_vs_marriage()
        st.write("This plot analyzes the connection between unemployment rates and marriage rates across states. It helps identify whether rising unemployment correlates with declining marriage rates, suggesting that financial insecurity might discourage marriage. Conversely, it may reveal periods or regions where unemployment did not significantly impact marriage rates. This analysis offers insights into how economic conditions, such as job losses or recovery periods, influence social behavior and long-term commitments like marriage. Regional variations may further highlight areas where social dynamics or policies affect the relationship between unemployment and marriage rates.")
        plot_norm_marriage_vs_divorce()
        st.write("This graph displays the normalized values of marriage and divorce rates to highlight relative trends more clearly, eliminating the effects of scale differences between the two metrics. Observations might reveal synchronization between marriage and divorce trends or detect shifts in one metric that do not correspond to changes in the other. The normalization makes it easier to spot underlying patterns, such as whether increases in marriages are followed by proportional rises in divorces or if divorce trends move independently from marriage trends in certain states.")
        plot_norm_divorce_vs_marriage()
        st.write("This plot reverses the comparison by emphasizing the normalized divorce rates in relation to marriage rates. It offers a clearer view of how divorce trends behave relative to marriage rates across states or time periods. Observations may highlight whether changes in marriage rates influence divorce behavior or if divorce trends develop independently. This plot is particularly useful for identifying discrepancies, such as regions where high divorce rates persist despite declining marriages, providing insights into changing societal norms or specific state-level influences on marriage stability.")
        

    elif menu_2 == "Regression":
        st.write("### Regression Analysis")
        st.write("""
        This section focuses on regression models to quantify the impact of economic factors 
        on divorce rates. Using GDP and unemployment data, we can build predictive 
        models to better understand the relationships between these variables. Regression 
        analysis helps us explore causality and predict trends under varying economic conditions.
        These two graphs were chosen for regression from all graphs since better correlations were observed from them.
        """)
        plot_gdp_vs_divorce()
        st.write("This plot examines the relationship between GDP and divorce rates across U.S. states, revealing how economic performance might influence divorce trends. Observations may indicate whether higher GDP correlates with higher or lower divorce rates. A negative correlation might suggest that economic stability reduces divorces, while a positive correlation could imply that financial security enables individuals to leave unhappy marriages. A linear regression line can provide further insight into the strength and direction of the relationship. Cross-state comparisons can highlight regional differences, where certain areas exhibit stronger connections between economic health and divorce rates than others.")
        plot_unemp_vs_divorce()
        st.write("This plot explores the relationship between unemployment rates and divorce rates, offering insights into how economic insecurity impacts marital stability. Observations may show whether increased unemployment correlates with higher divorce rates, reflecting financial stress as a driver of separations. Alternatively, a negative correlation might indicate that divorce rates decline during economic hardship, as couples may choose to stay together for financial reasons. A regression line helps quantify the relationship and assess its statistical significance. State-level comparisons can reveal whether regional variations in unemployment have a consistent impact on divorce rates, contributing to a nuanced understanding of social behavior during economic downturns.")
