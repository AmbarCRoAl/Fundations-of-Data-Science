import streamlit as st
import seaborn as sns

col1, col2 = st.columns([1,2]) #Creates 2 columns where the one in the middle is double the size that the other
col1.markdown('# App for census information') #The hash makes it a title

with st.expander('More information'):
  st.write('Extraction was done by Barry Becker from the 1994 Census database.') 
  st.write('It was extracted from https://archive.ics.uci.edu/dataset/20/census+income')
  st.write('The attributes are: age,	workclass,	fnlwgt,	education,	education-num,	mariatl,	occupation,	relationship,	race,	sex,	capital-gain,	capital-loss,	hours-per-week,	countr,	income.')
  st.write('The last attribute (income) only tells you weather or not that individual earns more than $50,000 per year, it does not give the absolute value of their income.')

if 'file' not in st.session_state:
  st.session_state['file'] = 'not done'
def file_uploaded():
  st.session_state['file']='done'
file_uploaded = col2.file_uploader('Upload the census file here', on_change=file_uploaded)
if  st.session_state['file'] == 'done':
  st.sucess('File uploaded sucessfully')
         
  df_census = file_uploaded
  gain_age = sns.jointplot(y='capital-gain', x='age', data=df_census, kind="reg", color="#7f1a1a")
  loss_age = sns.jointplot(y='capital-loss', x='age', data=df_census, kind="reg", color="#7f1a1a")
  fnlwgt_age = sns.jointplot(y='fnlwgt', x='age', data=df_census, kind="reg", color="#7f1a1a")
  hours_age = sns.jointplot(y='hours-per-week', x='age', data=df_census, kind="reg", color="#7f1a1a")
  hours_gain = sns.jointplot(y='hours-per-week', x='capital-gain', data=df_census, kind="reg", color="#7f1a1a")

  col2.markdown('Some exploratory graphs for the raw data')
  col2.image(gain_age)
  col2.image(loss_age)
  col2.image(fnlwgt_age)
  col2.image(hours_age)
  col2.image(hours_gain)
