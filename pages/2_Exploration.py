import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


st.title("Which attribute would you like to learn more about?")
sd = st.selectbox("Please select one:", #Drop Down Menu Name
        [
            "Age and gender",
            "Working sector and education", 
            "Country of origin",   
            "Marital Status"
        ]
    )

if sd == "Age and gender":
    st.write('# Age and gender')
    fig = graph_age_percentage()
    st.pyplot(fig)
    col1, col2 = st.columns(2)
    fig = graph_age_gains()
    col1.pyplot(fig)
    fig = graph_age_losses()
    col2.pyplot(fig)

elif sd == "Working sector and education":
    st.write('# Working sector and education')
    fig = graph_jobedu_gains()
    st.pyplot(fig)
    fig = graph_jobedu_losses()
    st.pyplot(fig)

elif sd == "Country of origin":
    st.write('# Country of origin')
    col1, col2 = st.columns(2)
    fig = graph_countr_percentage()
    col1.pyplot(fig)
    fig = graph_countr_gainloss()
    col2.pyplot(fig)

elif sd == "Marital status":
    st.write('# Marital status"')
    fig = graph_marital_gainloss()
    st.pyplot(fig)

