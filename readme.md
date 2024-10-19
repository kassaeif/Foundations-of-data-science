### **Project Overview**  
This project focuses on visualizing and analyzing U.S. marriage and divorce rates, as well as examining the relationships between economic factors such as GDP and unemployment with these social indicators. Using interactive visualizations built with **Streamlit** and datasets from various sources, users can explore trends across states from 1990 to 2022. Additionally, the app provides heatmaps and time-series plots to highlight missing data and trends. The inclusion of regression models allows users to explore correlations between metrics like GDP and marriage or divorce rates, contributing to deeper insights into economic and social dynamics. All the functions are defined in plot_functions.py. The app2.py recalls those functions and shows the plots and all other materials.

### **Features of the App**  
- **Marriage and Divorce Rate Visualization**: View trends across all U.S. states over time using line plots.  
- **Heatmaps**: Visualize marriage and divorce rates as well as missing data patterns with heatmaps.  
- **Economic Relationships**: Analyze correlations between GDP, unemployment, and marriage/divorce rates with scatter plots and regression lines.  
- **Interactive Filters**: Select states and time ranges for focused analyses through Streamlit’s widgets.  
- **Imputation of Missing Data**: Mean imputation is used to fill gaps in marriage and divorce rate datasets for better completeness.

---

### **Setup Instructions**  

1. **Install Required Packages**  
   Make sure you have Python installed. Install the required dependencies by running:  
   ```bash
   pip install -r requirements.txt
   ```

2. **Download Datasets**  
   Ensure the following datasets are placed in the root directory of the repository:  
   - `state-divorce-rates-90-95-00-22.xlsx`
   - `state-marriage-rates-90-95-00-22.csv`
   - `filtered_all_industry_gdp -since 2000.csv`
   - `Unemployment in America Per US State.csv`

3. **Run the Streamlit App**  
   Launch the app by running the following command in your terminal:  
   ```bash
   streamlit run <your-app-file-name>.py
   ```

---

### **How the App Works**  
- Use the **multiselect widgets** to select states of interest or analyze all states by clicking the provided buttons.
- Choose specific time ranges with the **slider** to filter data.
- View detailed **scatter plots** with regression lines to explore relationships between economic and social indicators.
- **Heatmaps** offer a visual summary of missing values and data distributions across states and years.
