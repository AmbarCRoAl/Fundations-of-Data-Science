import streamlit as st
import seaborn as sns

Home.py # This is the file you run with "streamlit run"
  pages/
    Introduction.py # This is a page
    2_Exploration.py # This is another page
    3_Conclusion.py # So is this

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
file_uploaded = col2.file_uploader('Want to see where you stand among US population?\nUpload your info here:', on_change=file_uploaded)
if  st.session_state['file'] == 'done':
  col2.write('File uploaded sucessfully')

