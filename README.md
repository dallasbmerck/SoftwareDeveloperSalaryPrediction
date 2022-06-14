# SoftwareDeveloperSalaryPrediction
- Author: Dallas Merck
- Link to web application: https://share.streamlit.io/dallasbmerck/c964capstone/app.py

## Development Environment:
- Jupyter Notebook 6.4.8
- Pandas
- Scikit-learn
- Numpy
- Matplotlib
- Pyplot
- PyCharm 2022.1
- Streamlit

## Description:
- The software developer salary prediction application is a machine learning application that takes input regarding country of residence, education level, and years of experience to calculate recommended base salary.
- Data used to train and test the ML model was sourced from Stack Overflow Developer Survey 2021.
- The dataset was cleansed to remove all unnecessary columns that could not be used to make salary predictions. Additionally all null entries were removed.
- To improve accuracy regarding country of residence, a function was written to split data by country and export to CSV to be assigned to new data frames.
- Each country dataset was improved by applying interquartile range functions to remove salary outliers.
- Once each country was appropriately cleansed, a new function was written to recombine all data into a new CSV and eventually a new data frame.
- A multitude of regression analysis algorithms were tested to ensure the highest accuracy of the prediction model.
- Random forest regression was the highest accuracy model and was chose for the final web application.
- Jupyter Notebook was "pickled" into a .pkl file for transfer to PyCharm.
- Once in PyCharm, Streamlit was imported to create the web app. 
- Finally, the project was added to a github repository where it could be used by Strealit Share to host the website.
