import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# This file is used to create the 'explore' page in the salary prediction web app.

# Recycled from Jupyter Notebook 'salary_prediction.ipynb' to clean country data below a minimum record threshold.
def clean_countries(countries, minimum):
    country = {}
    for i in range(len(countries)):
        if countries.values[i] >= minimum:
            country[countries.index[i]] = countries.index[i]
        else:
            country[countries.index[i]] = 'Other'
    return country


# Recycled from Jupyter Notebook 'salary_prediction.ipynb' to convert work experience from string to float.
def clean_work_experience(e):
    if e == 'More than 50 years':
        return 50
    if e == 'Less than 1 year':
        return 0.5
    return float(e)


# Recycled from Jupyter Notebook 'salary_prediction.ipynb' to clean education data by decreasing the number of unique entries.
def clean_education_level(x):
    if 'Bachelor' in x:
        return "Bachelor's Degree"
    if 'Master' in x:
        return "Master's Degree"
    if 'Other doctoral' in x or 'Professional degree' in x:
        return "Post Graduate Degree"
    else:
        return "Less than Bachelor's Degree"


# New function to tidy up the graphical data on the explore page. Country names were too long and distorted graphs.
def clean_country_name(c):
    if 'United States' in c:
        return 'United States'
    if 'United Kingdom' in c:
        return 'United Kingdom'
    if 'Russian' in c:
        return 'Russia'
    return c


# Loads the for the  web app the use after applying cleaning parameters to the dataset.
# Makes use of Streamlit cache function to improve efficiency.
@st.cache
def load():
    df = pd.read_csv('survey_results_public.csv')
    df = df[['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedCompYearly']]
    df = df.rename({'ConvertedCompYearly': 'Salary'}, axis=1)
    df = df[df['Salary'].notnull()]
    df = df[df['Employment'] == 'Employed full-time']
    df = df.drop('Employment', axis=1)
    df = df.dropna()
    country_mapping = clean_countries(df.Country.value_counts(), 500)
    df['Country'] = df['Country'].map(country_mapping)
    df = df[df['Country'] != 'Other']
    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_work_experience)
    df = df[df['Salary'] >= 500]
    df = df[df['Salary'] <= 200000]
    df['EdLevel'] = df['EdLevel'].apply(clean_education_level)
    df['Country'] = df['Country'].apply(clean_country_name)

    return df


# Load the dataframe.
df = load()


# Function to display the exploration page data using streamlit and matplotlib.
def show_exploration_page():
    st.title('Software Developer Data Visualizations')

    st.write('')
    st.write('')

    data = df['Country'].value_counts()

    # Pie chart showing data distribution for each country.
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis('equal')

    st.write('Distribution of Developers by Country')

    st.pyplot(fig1)

    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.write('Mean Salary For Each Country')

    # Bar chart: mean salary by country.
    data = df.groupby(['Country'])['Salary'].mean().sort_values(ascending=True)
    st.bar_chart(data, height=500)

    st.write('')
    st.write('')

    st.write('Mean Salary Based On Years of Experience')

    # Line chart: mean salary by years of experience.
    data = df.groupby(['YearsCodePro'])['Salary'].mean().sort_values(ascending=True)
    st.line_chart(data)

    st.write('')
    st.write('')
    st.write('')
    st.write('')

    st.markdown('<p style="font-size: 12px">The data used the create the graphs above is from the Stack Overflow '
                'Developer Survey after it has been processed to remove unneeded data points.'
                '</p>', unsafe_allow_html=True)
