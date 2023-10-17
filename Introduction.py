import streamlit as st
import seaborn as sns


col1, col2 = st.columns([1,2]) #Creates 2 columns where the one in the middle is double the size that the other
col1.markdown('# App for census information on income') #The hash makes it a title

col2.image('https://www.census.gov/content/dam/Census/library/visualizations/2018/comm/acs-5yr-mhi-all-counties.jpg')
with st.expander('More information'):
  st.write('Extraction was done by Barry Becker from the 1994 Census database.') 
  st.write('It was extracted from https://archive.ics.uci.edu/dataset/20/census+income')
  st.write('The attributes are: age,	workclass,	fnlwgt,	education,	education-num,	mariatl,	occupation,	relationship,	race,	sex,	capital-gain,	capital-loss,	hours-per-week,	countr,	income.')
  st.write('The last attribute (income) only tells you weather or not that individual earns more than $50,000 per year, it does not give the absolute value of their income.')

st.write('Want to see where you stand among the US population?\nUpload your info here:')
person_age = st.text_input('Age:')
person_sex = st.text_input('Sex/Gender:')
person_education = st.text_input('Education level:')
person_industry = st.text_input('Work sector (industry, federal, etc):')
person_country = st.text_input('Country of origin:')
person_info = [person_age, person_sex, person_education, person_industry, person_country]
