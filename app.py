import streamlit as st
from prediction_page import show_prediction_page
from exploration_page import show_exploration_page

# This file is called in the terminal to run the salary prediction app using streamlit to display in a web app.

# Page variable is used in an if statement to allow users to select options from a sidebar and show the different pages.
page = st.sidebar.selectbox('Predict Salary or Explore Data', ('Predict Salary', 'Explore Data'))

if page == 'Predict Salary':
    show_prediction_page()
else:
    show_exploration_page()