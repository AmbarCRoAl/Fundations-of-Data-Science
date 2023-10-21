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
            "Working class and education", 
            "Region of origin",   
            "Marital status"
        ]
    )

if sd == "Age and gender":
        st.markdown("<h1 style='text-align: left; color: darkolivegreen;'> Age and gender</h1>", unsafe_allow_html=True) 
        st.subheader("The percentage of people earning over \$50,000 peaks around 45 years old, men have double the chance to earn over that, and the gains and losses for man are also almost doubled.")
        col1, col2 = st.columns(2)
        col1.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/age_sex1.png')
        col2.write("On the left graph we can see the percentage of people who earns over \$50,000 per year (over-earners) by age and gender. The percentage is approximately the same for both woman and man 25 years old or younger, but the genders quickly diverge for people between 25 and 45, with woman having only around 13% while for man it's around 30%.")
        col2.write("For both genders we see a peak around 45 years, and in general the percentage for over-earner man is about 3 times higher than for woman.")
        st.write("Another factor to look at when considering differences in income is the reported capital gains and capital losses. The graphs below show the distributed gains and losses for both over-earners and under-earners.")
        col1, col2 = st.columns(2)
        col1.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/age_sex2.png')
        col2.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/age_sex3.png')
        st.write("We see that the capital gains increase by age for man, while for woman they peak around 45 years old. They are significantly higher for over-earner man compared to over-earner woman, yet roughly the same for under-earners.")
        st.write("The capital losses are directly correlated to the gains. We see that for man and over-earner woman, the groups who reported more gains also reported more losses, but this trend does not hold for under-earner woman. Although they have roughly the lowest capital gains, they have the highest capital losses, only supassed by over-earner man between 25-65 years old.")


elif sd == "Working class and education":
        st.markdown("<h1 style='text-align: left; color: darkolivegreen;'> Working class and education</h1>", unsafe_allow_html=True) 
        st.subheader("The level of education determines your capital gains and losses in almost an identical way as the working class you're part of.")
        st.write("One would guess that the level of education and the working sector of an individual are independent traits, and contribute to that individual's income level in different ways. During this study we have found that this is not true, instead, these attriutes seem to determine people's capital gains and losses in almost an identical manner.")
        st.write("If we place them in the orders:")
        st.markdown(" * Highschool diploma followed by, some college, Bachellors, Masters and PhD degrees")
        st.markdown(" * State goverment followed by, federal goverment, private sector, self employment (not incorporation), and self employed with incorporation")
        st.write("We will see lines that follow almost an identical trend.")
        st.write("Bellow I present such graphs. Notice that these graphs have **two y-axes.** This is because the capital gains and losses for groups who earned above \$50,000 per year (over-earners) compared to those who earn under \$50,000 per year (under-earners) are drastically higher, in some cases orders of magnitudes.")
        st.write("The legends of the graphs are next to the corresponding axis it is scalled under. Here, the left axes correspond to the capital gains/losses of over-earners, and the right axis to the gains/losses of under-earners.")
        st.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/educ_sect1.png')
        st.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/educ_sect2.png')
        st.write("From these plots we can make the following conclusions:")
        st.markdown(" * In the previously mentioned order, there is steady increase of capital gains for over-earners, but amost steady decrease for under-earners, only masters and private sector staying on top of the other categories.")
        st.markdown(" * The capital losses of over-earners are lowest for: people who work on the private sector (followed by the state government), and those who have only a high school diploma. Other categories are increasing from left to right.")
        st.markdown(" * On the other hand, the capital losses of under-earners are lowest when: they have a doctorate degree, or incorporated self employed people.")
        st.markdown(" * Capital losses for under-earners seems to slowly decreased in the previously mentioned order.")
  
elif sd == "Region of origin":
        st.markdown("<h1 style='text-align: left; color: darkolivegreen;'> Country of origin</h1>", unsafe_allow_html=True) 
        st.subheader("Canada is the region with the highest amount of high earners, followed by Asia and then the US, while South America is the one at the bottom.")
        col1, col2 = st.columns([4.5,5.5])
        col1.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/country1.png')
        col2.write("On the graph to the left we are presenting the percentage of population from each region (country or continent) who earn over \$50,000 per year (over-earners).")
        col2.write("We observe that the percentage of over earners is highest in Canada, followed by Asia, Europe, United States and the lowest being South America.") 
        col1, col2 = st.columns(2)        
        col1.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/country2.png')
        col2.write("The highest distributed gains for over and under-earners were for people from Asia and Europe respectively, while the second lowest losses were for those in Canada and Europe for over and under-earners respectively.")
        col2.write("South America had the lowest values in every aspect except losses of over-earners for which Canada had slightly less. ")
        col2.write("Note that this graph has **two y-axes**. This is because the distributed capital gains and losses are one order of magnitude different, so only scaling them to different axes would make it possible to view.")
        st.write("The legends of the graphs are next to the corresponding axis it is scalled under. Here, the left axes correspond to the capital gains/losses of over-earners, and the right axis to the gains/losses of under-earners.")
        st.write("We want to pint out that the here observed values are **NOT** representations of the whole continents of Asia, South America nor Europe. The data was reduced to these regions to make it more maneageable, but we do not have data for all the countries in these continents.")
        st.write("It is most likely that the countries with available data for this study are those with the highest GDP, since such detailed data may be more difficult to obtain from less developed countries.")

elif sd == "Marital status":
        st.markdown("<h1 style='text-align: left; color: darkolivegreen;'> Marital status</h1>", unsafe_allow_html=True) 
        st.subheader("Married people tend to earn more, but when the income is bellow $50k, widows have higher capital gains.")
        st.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/marital1.png')
        col1, col2 = st.columns([4.5,5.5])
        col1.image('https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/marital2.png')
        

elif sd == "--------------":
        st.markdown(" ")
