
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px 

# Load the IMDB movies dataset
movies_df = pd.read_csv('imdb_top_1000.csv')
movies_gen_def = pd.read_csv('imdb_1000_genre.csv')

# Data cleaning for runtime and gross columns
movies_df['Runtime'] = movies_df['Runtime'].str.replace(' min', '').astype(int)
movies_df['Gross'] = movies_df['Gross'].str.replace(',', '').astype(float)

# Sidebar menu for navigation
menu = st.sidebar.selectbox(
    "Select a section",
    ["Introduction", "Data Visualization", "Model Performance", "Conclusion"]
)

# Introduction Section
if menu == "Introduction":
    st.title("Project Introduction")
    st.write("""
    Movies have been an essential part of global culture and entertainment for over a century, evolving from 
             silent films to the cinematic masterpieces of today. They serve as a reflection of society, 
             influencing and being influenced by culture, technology, and politics. With the growing popularity
              of streaming platforms and an ever-expanding film industry, the variety of genres, storytelling techniques,
              and visual effects has made movies one of the most consumed forms of media worldwide. Whether through
              blockbusters, indie films, or critically acclaimed productions, 
             movies continue to captivate audiences across the globe.

    This project leverages a dataset of the top 1,000 movies from IMDb, one of the most trusted movie rating 
             and review platforms. IMDb ranks movies based on user ratings, providing a comprehensive view of films that 
             have gained widespread recognition for their quality, direction, and performances. 
             The dataset includes various features, such as movie titles, release years, genres, IMDb ratings, and 
             financial data like gross revenue. By analyzing these elements, we can gain deeper insights into patterns 
             and trends in the film industry, such as what genres dominate the top rankings and how financial success 
             correlates with critical acclaim.

    Through this project, we'll explore key visualizations that offer insights into 
             the top 1,000 movies. We’ll examine the distribution of IMDb ratings, analyze relationships 
             between movie runtime and ratings, and look at the financial success of films through gross revenue figures. 
             By providing these analyses, this project aims to help both film enthusiasts and data scientists understand the 
             dynamics of the movie industry, from the creative aspects to the business side.
    """)
    st.image("https://th.bing.com/th/id/R.5dd08addca8c9922408123292e2a5c3d?rik=0yiygbqJl0cAqQ&riu=http%3a%2f%2ftheseventhart.org%2fwp-content%2fuploads%2f2012%2f06%2fGodfatherIII.jpg&ehk=Em%2bD%2be0p08GrSa6RgxantpppC%2bynuuB2d7326mu3OMI%3d&risl=&pid=ImgRaw&r=0", caption="Project Overview")


# Data Visualization Section
elif menu == "Data Visualization":
    st.title("Data Visualization")

    # Visualization 1: Distribution of IMDB Ratings
    st.write("### Distribution of IMDB Ratings")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(movies_df['IMDB_Rating'], bins=20, kde=True, ax=ax)
    ax.set_title('Distribution of IMDB Ratings')
    st.pyplot(fig)

    # Visualization 2: Top 10 Directors with Most Movies
    st.write("### Top 10 Directors with Most Movies")
    fig, ax = plt.subplots(figsize=(10, 6))
    top_directors = movies_df['Director'].value_counts().head(10)
    sns.barplot(x=top_directors.values, y=top_directors.index, ax=ax)
    ax.set_title('Top 10 Directors with Most Movies')
    st.pyplot(fig)

    # Visualization 3: Movie Runtime vs. IMDB Rating
    st.write("### Movie Runtime vs. IMDB Rating")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=movies_df['Runtime'], y=movies_df['IMDB_Rating'], hue=movies_df['Genre'], alpha=0.7, ax=ax)
    ax.set_title('Movie Runtime vs IMDB Rating')
    st.pyplot(fig)

    # Visualization 4: Gross Revenue vs. IMDB Rating
    st.write("### Gross Revenue vs. IMDB Rating")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=movies_df['Gross'], y=movies_df['IMDB_Rating'], hue=movies_df['Genre'], alpha=0.7, ax=ax)
    ax.set_title('Gross Revenue vs IMDB Rating (Log Scale)')
    ax.set_xscale('log')
    st.pyplot(fig)

    # Visualization 5: Count of Movies by Genre
    st.write("### Count of Movies by Genre")
    genres = movies_df['Genre'].str.split(', ', expand=True).stack().value_counts()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=genres.values, y=genres.index, ax=ax)
    ax.set_title('Count of Movies by Genre')
    st.pyplot(fig)

    # Visualization 6: IMDB Rating vs. Number of Votes
    st.write("### IMDB Rating vs. Number of Votes")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=movies_df['No_of_Votes'], y=movies_df['IMDB_Rating'], alpha=0.7, ax=ax)
    ax.set_title('IMDB Rating vs Number of Votes (Log Scale)')
    ax.set_xscale('log')
    st.pyplot(fig)

    # New Visualization 7: IMDB Rating vs. Meta Score
    st.write("### IMDB Rating vs. Meta Score")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='Meta_score', y='IMDB_Rating', data=movies_df, ax=ax)
    ax.set_title('IMDB Rating vs. Meta Score')
    ax.set_xlabel('Meta Score')
    ax.set_ylabel('IMDB Rating')
    ax.grid(True)
    st.pyplot(fig)

    # New Visualization 8: Top Directors by Number of Movies
    st.write("### Top Directors with Most Movies in Top 1000")
    fig, ax = plt.subplots(figsize=(10, 6))
    top_directors = movies_df['Director'].value_counts().head(10)
    top_directors.plot(kind='bar', ax=ax)
    ax.set_title('Top Directors with Most Movies in Top 1000')
    ax.set_xlabel('Director')
    ax.set_ylabel('Number of Movies')
    ax.set_xticklabels(top_directors.index, rotation=45)
    st.pyplot(fig)

    # New Visualization 9: Count of Movies by Genre
    st.write("### Count of Movies by Genre")
    genre_df = movies_df['Genre'].str.get_dummies(sep=', ')
    genre_counts = genre_df.sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    genre_counts.plot(kind='bar', ax=ax)
    ax.set_title('Count of Movies by Genre')
    ax.set_xlabel('Genre')
    ax.set_ylabel('Count')
    ax.set_xticklabels(genre_counts.index, rotation=45)
    st.pyplot(fig)

    # New Visualization 10: Total Gross Earnings by Year
    st.write("### Total Gross Earnings by Year")
    gross_by_year = movies_df.groupby('Released_Year')['Gross'].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    gross_by_year.plot(kind='line', ax=ax)
    ax.set_title('Total Gross Earnings by Year')
    ax.set_xlabel('Release Year')
    ax.set_ylabel('Total Gross Earnings (in dollars)')
    ax.grid(True)
    st.pyplot(fig)

    # New Visualization 11: Interactive Scatter Plot (Meta Score vs. IMDB Rating)
    st.write("### Interactive IMDB Rating vs. Meta Score")
    fig = px.scatter(movies_df, x='Meta_score', y='IMDB_Rating',
                     hover_data=['Series_Title', 'Released_Year'],
                     title="IMDB Rating vs. Meta Score",
                     labels={'Meta_score': 'Meta Score', 'IMDB_Rating': 'IMDB Rating'})
    st.plotly_chart(fig)

    # New Visualization 12: Interactive Pie Chart (Movie Certificates)
    st.write("### Interactive Pie Chart for Movie Certificates")
    certificate_counts = movies_df['Certificate'].value_counts().reset_index()
    certificate_counts.columns = ['Certificate', 'Count']
    fig = px.pie(certificate_counts, values='Count', names='Certificate',
                 title='Distribution of Movie Certificates',
                 hover_data=['Count'])
    st.plotly_chart(fig)


# Model Performance Section
elif menu == "Model Performance":
    st.title("Initial Data Analysis")

    st.write("""In this section of the app, we want to do the initial analysis on the dataset and how we handle the issues such as missing values and 
    other techniques that we did on te data.""")

# Display the first few rows of the dataset
    st.write("### Head of the Dataset")
    st.write("Below are the first 5 rows of the original dataset (IMDb Top 1000 Movies).")
    st.write(movies_df.head())

# Display the data types of each column in the dataset
    st.write("### Data Types of Each Column")
    st.write("Below are the data types for each column in the original dataset (IMDb Top 1000 Movies).")
    st.write(movies_df.dtypes)

    


    # Visualization 1: Heatmap of Missing Values
    st.write("### Heatmap of Missing Values")
    st.write("""Below figure shows the missing values in the original dataset (top 1000 IMDB movies). Based on the heatmap figure for missing values, we see that we have the missing 
    data.""")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(movies_df.isnull(), cbar=False, cmap="viridis", ax=ax)
    ax.set_title('Missing Values Heatmap For Original Dataset')
    st.pyplot(fig)
    
    # Visualization 2: Correlation Matrix
    st.write("### Correlation Matrix For Original Dataset")
    st.write("First we ahve to see what ")
    # Select numerical columns for correlation
    numerical_columns = ['IMDB_Rating', 'Runtime', 'Gross', 'Meta_score', 'No_of_Votes']
    corr_matrix = movies_df[numerical_columns].corr()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title('Correlation Matrix')
    st.pyplot(fig)

    # Creating a count plot to visualize the relationship between 'Genre_1' and 'Certificate'
    plt.figure(figsize=(10, 6))
    sns.countplot(data=movies_gen_def, x='Genre_1', hue='Certificate')

# Adding title and labels
    plt.title("Distribution of 'Genre_1' across different 'Certificate' categories")
    plt.xlabel("Primary Genre")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)
    st.write("### Handling missing values")
    st.write("""We have missing values in three columns based on the heatmap for missing values. Based on that figure, we have missing values in  Certificate, Meta_score, and Gross columns of the dataset.
             For this issue we have considered three methods to handle the missing values in the dataset in the mentioned columns.First, we will explain how we do the imoutation for numerical
             columns such as Meta_score and Gross.""")
    st.write("### Handling missingness in Meta score column")
    st.write("""For this issue we used median method for filling the missing values in the Meta_score column.""")






