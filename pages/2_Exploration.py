import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


st.title("Which attribute would you like to learn more about?")
sd = st.selectbox("Please select one:", #Drop Down Menu Name
        [
            "--------------",
            "Age and gender",
            "Working sector and education", 
            "Region of origin",   
            "Marital status"
        ]
    )

if sd == "Age and gender":
        st.markdown("<h1 style='text-align: left; color: darkolivegreen;'> Age and gender</h1>", unsafe_allow_html=True) 
        st.subheader("The percentage of people earning over $50,000 peaks around 45 years old, men have double the chance to earn over that, and the gains and losses for man are also almost doubled.")
        col1, col2 = st.columns(2)
        col1.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/age_sex1.png')
        col1, col2 = st.columns(2)
        col1.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/age_sex2.png')
        col2.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/age_sex3.png')


elif sd == "Working sector and education":
        st.subheader("The level of education determines your capital gains and losses in almost an identical way as the working sector you go to.")
        st.markdown("<h1 style='text-align: left; color: darkolivegreen;'> Working sector and education</h1>", unsafe_allow_html=True) 
        st.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/educ_sect1.png')
        st.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/educ_sect2.png')


elif sd == "Region of origin":
        st.markdown("<h1 style='text-align: left; color: darkolivegreen;'> Country of origin</h1>", unsafe_allow_html=True) 
        st.subheader("Canada is the region with the highest amount of high earners, followed by Asia and then the US, while South America is the one at the bottom.")
        col1, col2 = st.columns([4.5,5.5])
        col1.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/country1.png')
        col2.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/country2.png')


elif sd == "Marital status":
        st.markdown("<h1 style='text-align: left; color: darkolivegreen;'> Marital status</h1>", unsafe_allow_html=True) 
        st.subheader("Married people tend to earn more, but when the income is bellow $50k, widows have higher capital gains.")
        st.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/marital1.png')
        col1, col2 = st.columns([4.5,5.5])
        col1.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/marital2.png')
        

elif sd == "--------------":
        st.markdown(" ")
