import streamlit as st
import pickle
import numpy as np

# This file is used to display the prediction page which allows users to predict a salary based on country of residence,
# education level, and years of experience.

# Function to retrieve the pickle file (saved_steps.pkl) from Jupyter Notebook file titled 'salary_prediction.ipynb'.
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
        return data

# Load data.
data = load_model()

# Apply label encoders and load the random forest regression model.
rfr_loaded = data["model"]
country_after_LE = data["country_after_LE"]
education_after_LE = data["education_after_LE"]

# Function populates the prediction parameters in the prediction page using Streamlit.
def show_prediction_page():
    st.title("Software Developer Salary Prediction")

    st.write("""###### Please enter your country of residence, education level, and years of experience below.""")

    # Countries that user can pick from.
    countries = (
        'United States of America',
        'India',
        'Germany',
        'United Kingdom of Great Britain and Northern Ireland',
        'Canada',
        'France',
        'Brazil',
        'Spain',
        'Netherlands',
        'Australia',
        'Poland',
        'Italy',
        'Russian Federation',
        'Sweden'
    )

    # Education level that user can pick from.
    education = (
        "Less than Bachelor's Degree",
        "Bachelor's Degree",
        "Master's Degree",
        "Post Graduate Degree"
    )

    # Select box for the user to pick from countries above.
    country = st.selectbox('Country', countries)
    # Select box for the user to pick from education above.
    education_level = st.selectbox('Education Level', education)
    # Slider allows user to select years of experience from 0-10 years.
    experience = st.slider('Years of Experience', 0, 10, 1)

    # Button that when clicked, takes all user input, and uses the random forest regression algorithm to predict a salary.
    ok = st.button('Predict Salary')
    if ok:
        x = np.array([[country, education_level, experience]])
        x[:, 0] = country_after_LE.transform(x[:, 0])
        x[:, 1] = education_after_LE.transform(x[:, 1])
        x = x.astype(float)

        salary = rfr_loaded.predict(x)
        st.subheader(f'The estimated salary is ${salary[0]:.2f}')

    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')


    st.markdown('<p style="font-size: 12px">The salary predictions use a Random Forest Regression algorithm. '
                'The data used for the predictions has been sourced from Stack Overflow Developer Survey. '
                'Data has been thoroughly processed to ensure accurate predictions. A few of the countries in '
                'the training data do not have many entries for higher education, which may yield lower salaries '
                'than expected. These predictions do not include additional compensation such as stock or bonuses, '
                'and are only meant to reflect base salaries.', unsafe_allow_html=True)