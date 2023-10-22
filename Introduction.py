import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

url = 'https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/adult_data.csv'
df_census = pd.read_csv(url)
# fnlwgt is final weight, which is a weight of population percentage representation
# they used 3 sets of controls. These are: A single cell estimate of the population 16+
# for each state. Controls for Hispanic Origin by age and sex. Controls by Race, age
# and sex. The term estimate refers to population totals derived from Current Population Survey by creating
# "weighted tallies" of any specified socio-economic characteristics of the population.
# People with similar demographic characteristics should have similar weights.


col1, col2 = st.columns([1,2]) #Creates 2 columns where the one in the middle is double the size that the other
col1.markdown("<h1 style='text-align: left; color: darkolivegreen;'> Correlation of people's attributes and their income</h1>", unsafe_allow_html=True) 

col2.image('https://www.census.gov/content/dam/Census/library/visualizations/2018/comm/acs-5yr-mhi-all-counties.jpg')
with st.expander('Information about dataset'):
  st.write('Extraction was done by Barry Becker from the 1994 Census database.') 
  st.write('It was extracted from https://archive.ics.uci.edu/dataset/20/census+income')
  st.write('The attributes are: age,	workclass,	fnlwgt,	education,	education-num,	mariatl,	occupation,	relationship,	race,	sex,	capital-gain,	capital-loss,	hours-per-week,	countr,	income.')
  st.write('The last attribute (income) only tells you weather or not that individual earns more than $50,000 per year, it does not give the absolute value of their income.')
  st.write('The attribute fnlwgt stands for final weight. The term estimate refers to population totals derived from Current Population Survey by creating "weighted tallies" of any specified socio-economic characteristics of the population. People with similar demographic characteristics should have similar weights.')

with st.expander('Raw dataset'):
  st.write('Showing only the first 20 rows')
  st.table(df_census.head(20))

st.divider()
st.subheader('Information about analysis')
st.write("Here we examined a dataset of over 32,500 people to determined how different attributes (such as your level of education, age, gender, country of origin and others) affected the chances of people to earn over $50,000 per year, and how much these groups of population reported as gain or loss in capital.")
st.write("Although 32 thousand is a lot of people, it is by no mean everyone. When selecting individuals for these dataset, it was noticed that different gorups were under or over represented, and so an attribute called 'final weight' was generated to compensate for this (More information in dataset information).")
st.write("For our analysis, we took the final weight attribute as the amount of people that row was representing. We summed over all the people in each category to normalized our studies.")
st.markdown("We mainly focused on 3 things: \n * Percentage of people who earned over $50,000 per year \n * Capital gains distributed in said population \n * Capital losses distributed in said population")
st.write("Since some groups may simply have more people than others (for example, there is more people from the US than any other country), plainly summing the capital gains or losses would be biased to the amount of people in that group. To come around this issue, we divided the gains by the sum of all people in that group, so the amounts presented in this study is total gains/losses per person.")


st.divider()
st.subheader('Want to see where you stand among the US population?')
st.write('Upload your info here:')
person_age = st.text_input('Age:')
st.markdown(''':gray[&emsp;Please enter an integer.] ''')
person_sex = st.text_input('Sex/Gender:')
person_education = st.text_input('Education level:')
person_industry = st.text_input('Work sector (industry, federal, etc):')
person_country = st.text_input('Country of origin:')
person_info = [person_age, person_sex, person_education, person_industry, person_country]



