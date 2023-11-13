import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

url = 'https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/midterm/adult_data.csv'
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
st.markdown(''' The interactive information given bellow is based on the data previously described and a summary table provided 
by the US census webpage. There, the post-tax median income estimate and margin of error were provided for certain groups for the 
years 2021 and 2022. This dataset is table B-1 at https://www.census.gov/data/tables/2023/demo/income-poverty/p60-279.html. 
We used the median income from 2022. 
''')



#*********************************************************************************************************
#CODE FOR MAIN INTERACTION -------------------------------------------------------------------------------
#*********************************************************************************************************




# TEXT INPUT -------------------------------------------------------------------------------------
st.markdown('#### Upload your info here:')
person_age = st.text_input('Age:')
st.markdown(''':gray[&emsp;Please enter an integer.] ''')
person_sex = st.text_input('Sex/Gender:')
st.markdown(''':gray[&emsp;Please enter woman, man or none.] ''')
person_education = st.text_input('Education level:')
st.markdown(''':gray[&emsp;Please enter 'high school', 'some college', 'Bachelors', 'Masters', or 'Doctorate'.] ''')
person_country = st.text_input('Country of origin:')
st.markdown(''':gray[&emsp;Please enter US, Canada, Asia, South America or Europe.] ''')
person_industry = st.text_input('Work sector:')
st.markdown(''':gray[&emsp;Please enter 'self employed', 'incorporated self employed', 'private sector', 'state government' or &emsp;'federal goverment'.] ''')
person_marital = st.text_input('Marital status:')
st.markdown(''':gray[&emsp;Please enter married, divorced, separated, widowed or never married.] ''')
kids = st.text_input('Do you have kids?')
st.markdown(''':gray[&emsp;Please enter yes or no.] ''')
person_income = st.text_input('Anual income:')
st.markdown(''':gray[&emsp;Please enter your post-tax anual income without any symbol.] ''')

st.markdown(''':red[Please complete every box to see the rest.] ''')
st.markdown(''':red[Note that if you don't use the specific words provided, the information won't be displayed.] ''')





#*********************************************************************************************************
#CODE TO GET STANDARD INFO OUT OF THE DATA ----------------------------------------------------------------
#*********************************************************************************************************



#census with bool income dataset

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# fnlwgt is final weight, which is a weight of population percentage representation
# they used 3 sets of controls. These are: A single cell estimate of the population 16+
# for each state. Controls for Hispanic Origin by age and sex. Controls by Race, age
# and sex. The term estimate refers to population totals derived from Current Population Survey by creating
# "weighted tallies" of any specified socio-economic characteristics of the population.
# People with similar demographic characteristics should have similar weights.


#Cleaning data and summing different attributes
df1 = df_census.copy()
df1 = df1.dropna()

#Function for summing an attribute in a pre-defined array
def sum_groups(datarow, column_to_sum, sum_data):
  if datarow['age'] < 25 and datarow['sex']=='Female':
    sum_data[0]+= datarow[column_to_sum]
  if datarow['age'] >= 25 and datarow['sex']=='Female':
    if datarow['age'] < 45:
      sum_data[1]+= datarow[column_to_sum]
    elif datarow['age'] < 65:
      sum_data[2]+= datarow[column_to_sum]
    elif datarow['age'] >= 65:
      sum_data[3]+= datarow[column_to_sum]
  if datarow['age'] < 25 and datarow['sex']=='Male':
    sum_data[4]+= datarow[column_to_sum]
  if datarow['age'] >= 25 and datarow['sex']=='Male':
    if datarow['age'] < 45:
      sum_data[5]+= datarow[column_to_sum]
    elif datarow['age'] < 65:
      sum_data[6]+= datarow[column_to_sum]
    elif datarow['age'] >= 65:
      sum_data[7]+= datarow[column_to_sum]

  if datarow['mariatl'] == 'Divorced':
    sum_data[8]+= datarow[column_to_sum]
  if datarow['mariatl'] == 'Never-married':
    sum_data[9]+= datarow[column_to_sum]
  if datarow['mariatl'] == 'Married':
    sum_data[10]+= datarow[column_to_sum]
  if datarow['mariatl'] == 'Separated':
    sum_data[11]+= datarow[column_to_sum]
  if datarow['mariatl'] == 'Widowed':
    sum_data[12]+= datarow[column_to_sum]

  if datarow['education'] == 'HS-grad':
    sum_data[13]+= datarow[column_to_sum]
  if datarow['education'] == 'Some-college':
    sum_data[14]+= datarow[column_to_sum]
  if datarow['education'] == 'Bachelors':
    sum_data[15]+= datarow[column_to_sum]
  if datarow['education'] == 'Masters':
    sum_data[16]+= datarow[column_to_sum]
  if datarow['education'] == 'Doctorate':
    sum_data[17]+= datarow[column_to_sum]

  if datarow['workclass'] == 'State-gov':
    sum_data[18]+= datarow[column_to_sum]
  if datarow['workclass'] == 'Federal-gov':
    sum_data[19]+= datarow[column_to_sum]
  if datarow['workclass'] == 'Private':
    sum_data[20]+= datarow[column_to_sum]
  if datarow['workclass'] == 'Self-emp-not-inc':
    sum_data[21]+= datarow[column_to_sum]
  if datarow['workclass'] == 'Self-emp-inc':
    sum_data[22]+= datarow[column_to_sum]

  if datarow['countr'] == 'United_States':
    sum_data[23]+= datarow[column_to_sum]
  if datarow['countr'] == 'South_America':
    sum_data[24]+= datarow[column_to_sum]
  if datarow['countr'] == 'Canada':
    sum_data[25]+= datarow[column_to_sum]
  if datarow['countr'] == 'Europe':
    sum_data[26]+= datarow[column_to_sum]
  if datarow['countr'] == 'Asia':
    sum_data[27]+= datarow[column_to_sum]
  return

#Function to count the amount of incidence of each category
def count(datarow, sum_data):
  if datarow['age'] < 25 and datarow['sex']=='Female':
    sum_data[0]+= 1
  if datarow['age'] >= 25 and datarow['sex']=='Female':
    if datarow['age'] < 45:
      sum_data[1]+= 1
    elif datarow['age'] < 65:
      sum_data[2]+= 1
    elif datarow['age'] >= 65:
      sum_data[3]+= 1
  if datarow['age'] < 25 and datarow['sex']=='Male':
    sum_data[4]+= 1
  if datarow['age'] >= 25 and datarow['sex']=='Male':
    if datarow['age'] < 45:
      sum_data[5]+= 1
    elif datarow['age'] < 65:
      sum_data[6]+= 1
    elif datarow['age'] >= 65:
      sum_data[7]+= 1

  if datarow['mariatl'] == 'Divorced':
    sum_data[8]+= 1
  if datarow['mariatl'] == 'Never-married':
    sum_data[9]+= 1
  if datarow['mariatl'] == 'Married':
    sum_data[10]+= 1
  if datarow['mariatl'] == 'Separated':
    sum_data[11]+= 1
  if datarow['mariatl'] == 'Widowed':
    sum_data[12]+= 1

  if datarow['education'] == 'HS-grad':
    sum_data[13]+= 1
  if datarow['education'] == 'Some-college':
    sum_data[14]+= 1
  if datarow['education'] == 'Bachelors':
    sum_data[15]+= 1
  if datarow['education'] == 'Masters':
    sum_data[16]+= 1
  if datarow['education'] == 'Doctorate':
    sum_data[17]+= 1

  if datarow['workclass'] == 'State-gov':
    sum_data[18]+= 1
  if datarow['workclass'] == 'Federal-gov':
    sum_data[19]+= 1
  if datarow['workclass'] == 'Private':
    sum_data[20]+= 1
  if datarow['workclass'] == 'Self-emp-not-inc':
    sum_data[21]+= 1
  if datarow['workclass'] == 'Self-emp-inc':
    sum_data[22]+= 1

  if datarow['countr'] == 'United_States':
    sum_data[23]+= 1
  if datarow['countr'] == 'South_America':
    sum_data[24]+= 1
  if datarow['countr'] == 'Canada':
    sum_data[25]+= 1
  if datarow['countr'] == 'Europe':
    sum_data[26]+= 1
  if datarow['countr'] == 'Asia':
    sum_data[27]+= 1
  return

#Changing income to 0 if <=50K and 1 if >=50K
# Define a mapping dictionary to make data more manegable
# To get unique values in a column one should use: * unique_values = df1['mariatl'].unique() *
string_to_float_income = {'<=50K': 0, '>50K': 1}
country_to_regions = {'United-States': 'United_States', 'Cambodia': 'Asia',
                   'England': 'Europe', 'Puerto-Rico': 'United_States',
                   'Germany': 'Europe','Outlying-US(Guam-USVI-etc)': 'United_States',
                   'India': 'Asia', 'Japan': 'Asia', 'Greece': 'Europe', 'China': 'Asia',
                   'Cuba': 'South_America', 'Iran': 'Asia', 'Honduras': 'South_America',
                   'Philippines': 'Asia', 'Italy': 'Europe', 'Poland': 'Europe',
                   'Jamaica': 'South_America', 'Vietnam': 'Asia','Mexico': 'South_America',
                   'Portugal': 'Europe', 'Ireland': 'Europe', 'France': 'Europe',
                   'Dominican-Republic': 'South_America', 'Laos': 'Asia', 'Ecuador': 'South_America',
                   'Taiwan': 'Asia', 'Haiti': 'South_America', 'Columbia': 'South_America',
                   'Hungary': 'Europe', 'Guatemala': 'South_America', 'Nicaragua': 'South_America',
                   'Scotland': 'Europe', 'Thailand': 'Asia', 'Yugoslavia': 'Europe',
                   'El-Salvador': 'South_America', 'Trinadad&Tobago': 'South_America',
                   'Peru': 'South_America', 'Hong': 'Asia', 'Holand-Netherlands': 'Europe' }
marital_married = {'Married-civ-spouse':'Married', 'Married-spouse-absent':'Married', 'Married-AF-spouse':'Married'}

# Replace string values with corresponding values
df1['income'] = df1['income'].replace(string_to_float_income)
df1['countr'] = df1['countr'].replace(country_to_regions)
df1['mariatl'] = df1['mariatl'].replace(marital_married)

#Sum of fnlwgt for different types of attributes
groups = ['f_under25', 'f_25to45', 'f_45to65', 'f_over65', 'm_under25',
          'm_25to45', 'm_45to65', 'm_over65', 'Divorced', 'Never-married', 'Married',
          'Separated', 'Widowed', 'HS-grad', 'Some-college', 'Bachelors', 'Masters',
          'Doctorate','State-gov', 'Federal-gov',  'Private', 'Self-emp-not-inc', 'Self-emp-inc',
          'United_States', 'South_America', 'Canada', 'Europe', 'Asia']
num = len(groups)    #Number of attributes being studied; it will be used through out the rest of the code
sum_of_people = np.zeros(num)   #how many people earns above 50k for each attribute
sum_of_gains_over = np.zeros(num)     #how much was gain for people in the groups that earned over 50k
sum_of_gains_under = np.zeros(num)    #how much was gain for people in the groups that earned under 50k
sum_of_loss_over = np.zeros(num)     #how much was loss for people in the groups that earned over 50k
sum_of_loss_under = np.zeros(num)    #how much was loss for people in the groups that earned under 50k

sum_all_people = np.zeros(num)   #all the fnlwgt for each category, regardless weather or not they earned over 50K
sum_all_counts = np.zeros(num)     #the number of counts for each category
sum_all_over = np.zeros(num)     #the count of people who earned over 50K for each category

for index, row in df1.iterrows():
  sum_groups(row, 'fnlwgt', sum_all_people)
  sum_groups(row, 'income', sum_all_over)
  count(row, sum_all_counts)
  if row['income']:
    #print('\n\nFinal weight:\n', row['fnlwgt'])
    # Sum the values in column B
    sum_groups(row, 'fnlwgt', sum_of_people)
    sum_groups(row, 'capital-loss', sum_of_loss_over)
    sum_groups(row, 'capital-gain', sum_of_gains_over)
  else:
    sum_groups(row, 'capital-loss', sum_of_loss_under)
    sum_groups(row, 'capital-gain', sum_of_gains_under)

#Making ratios

ratio_people = np.zeros(num)
ratio_gain_over = np.zeros(num)
ratio_gain_under = np.zeros(num)
ratio_loss_over = np.zeros(num)
ratio_loss_under = np.zeros(num)
ratio_counts = np.zeros(num)

for i in range(num):
  if sum_all_people[i] == 0:
    print('There was no person in the group ', groups[i], 'who earned over 50K in this dataframe')
    ratio_people[i] = 0
    ratio_gain_over[i] = 0
    ratio_gain_under[i] = 0
    ratio_loss_over[i] = 0
    ratio_loss_under[i] = 0
  else:
    ratio_people[i] = sum_of_people[i]/sum_all_people[i] *100
    ratio_gain_over[i] = sum_of_gains_over[i]/sum_all_people[i] *100
    ratio_gain_under[i] = sum_of_gains_under[i]/sum_all_people[i] *100
    ratio_loss_over[i] = sum_of_loss_over[i]/sum_all_people[i] *100
    ratio_loss_under[i] = sum_of_loss_under[i]/sum_all_people[i] *100
    ratio_counts[i] = sum_all_over[i]/sum_all_counts[i] *100








#*********************************************************************************************************
#CODE FOR WEB-APP IMPLEMENTATION --------------------------------------------------------------------------
#*********************************************************************************************************



url = 'https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/midterm/Post-tax%20household%20income%20summary_transverse.csv'
df_summary = pd.read_csv(url)



# We want to get the median income for people with this individual's characteristics
# We'll display a graph with just one row, and in each column will be a trait with the median income either
#   red or green depending whether or not it's above their income.
# We will also show the percentage with all those attributes who earned over $50,000, and the gains in a violin plot
# Here onwards, the median_ arrays correspond to information extracted from the census dataset, and the order of info
#   is age, education, country-of-origin and sex/marital, corresponding to indeces in person_info of 1, 2, 3, and 4/5.

person_age = int(person_age)
person_income = float(person_income)
person_info = [person_income, person_age, person_education, person_country, person_sex, person_marital, person_industry]


median_keys = []
median_info = []
median_colors = []

#Determining the age group
if person_info[1] < 25:
  median_keys.append('15 to 24 years')
elif person_info[1] >= 25:
  if person_info[1] < 35:
    median_keys.append('25 to 34 years')
  if person_info[1] >= 35 and person_info[1] < 45:
    median_keys.append('35 to 44 years')
  if person_info[1] >= 45 and person_info[1] < 65:
    if person_info[1]  < 55:
      median_keys.append('45 to 54 years')
    elif person_info[1]  >= 55:
      median_keys.append('55 to 64 years')
  elif person_info[1]  >= 65:
    median_keys.append('65 years and older')

#Determining the education level
if person_info[2] == 'high school':
  median_keys.append('High school, no college')
  person_info[2] = 'HS-grad'
else:
  if person_info[2] == 'some college':
    median_keys.append('Some college')
    person_info[2] = "Some-college"
  else:
    if person_info[2] == 'Bachelors':
      median_keys.append("Bachelor's degree or higher")
    if person_info[2] == 'Masters':
      median_keys.append("Bachelor's degree or higher")
    if person_info[2] == 'Doctorate':
      median_keys.append("Bachelor's degree or higher")

#Determining the country of origin
if person_info[3] == 'US':
  median_keys.append('Native-born')
  person_info[3] = 'United_States'
else:
  median_keys.append('Foreign-born')
  if person_info[3] == 'South America':
    person_info[3] = 'South_America'

#Determining the sex/gender
if person_info[4] == 'woman':
  person_info[4] = 'Female'
  if person_info[5] == 'married':
    median_keys.append('Married-couple')
  else:
    if kids == 'yes':
      median_keys.append('Female householder, no spouse present')
    elif kids == 'no':
      median_keys.append('Female householder')
else:
  if person_info[4] == 'man':
    person_info[4] = 'Male'
    if person_info[5] == 'married':
      median_keys.append('Married-couple')
    else:
      if kids == 'yes':
        median_keys.append('Male householder, no spouse present')
      elif kids == 'no':
        median_keys.append('Male householder')
  elif person_info[4] == 'none':
      if kids == 'yes':
        median_keys.append('Family households')
      elif kids == 'no':
        median_keys.append('Nonfamily households')


#GETTING MEDIAN INCOME FOR SOME CHARACTERISTICS ----------------------------------------------------------------
for i in range(len(median_keys)):
  median_info.append(df_summary.loc[4,median_keys[i]])
  median_info[i] = median_info[i].replace(',', '')
  median_info[i] = float(median_info[i])
  if median_info[i] >= person_info[0]:
    median_colors.append('green')
  else:
    median_colors.append('red')

#Replacing strings to match key words in complete census dataframe
if person_info[6] == 'self employed':
  person_info[6] = 'Self-emp-not-inc'
if person_info[6] == 'incorporated self employed':
  person_info[6] = 'Self-emp-inc'
if person_info[6] == 'private sector':
  person_info[6] = 'Private'
if person_info[6] == 'state government':
  person_info[6] = 'State-gov'
if person_info[6] == 'federal goverment':
  person_info[6] = 'Federal-gov'

if person_info[5]== 'divorced':
  person_info[5] = 'Divorced'
if person_info[5]== 'never married':
  person_info[5] = 'Never-married'
if person_info[5]== 'married':
  person_info[5] = 'Married'
if person_info[5]== 'separated':
  person_info[5] = 'Separated'
if person_info[5]== 'widowed':
  person_info[5] = 'Widowed'



#PERCENTAGE AND GAINS/LOSSES FOR DISPLAY ------------------------------------------------------------------
#Getting the percentage
sum_all = 0
sum_highearners = 0
for index, row in df1.iterrows():
  if row['age'] >= person_info[1]-5 and row['age'] <= person_info[1]+5:
    if row['education'] == person_info[2]:
      if row['workclass'] == person_info[6]:
        if row['mariatl'] == person_info[5]:
          if row['countr'] == person_info[3]:
            if row['sex'] == person_info[4]:
              sum_all += row['fnlwgt']
              if row['income']:
                sum_highearners += row['fnlwgt']
try:
  percentage_highearners = sum_highearners/sum_all
except ZeroDivisionError:
  st.write("**There was no one in the dataset that matched your exact description. If there is data display in the graph, this corresponds to your previous selection.**")
  percentage_highearners = "unknown"
  
#Creating dataset of the gains/losses for people with these atributes as a function of index_forX
key_words = ['income', 'age', 'education', 'countr', 'sex', 'mariatl', 'workclass']
corresponding_index = [0, 1, 2, 3, 4, 5, 6]


#MULTI-SELECTION BOX -----------------------------------------------------------------------------
index_forX = st.selectbox(
    'Pick the value for the x-axis:',
    [ 'age', 'education', 'country', 'sex', 'marital', 'workclass'])
selected_cond = st.multiselect(
    'Pick up to 5 characteristics to match:',
    [ 'age', 'education', 'country', 'sex', 'marital', 'workclass'])
st.markdown(''':gray[&emsp;NOTE: if you select age as the first attribute, we will show people +-5 years your age, if it's at any other position, it will show only the people that have exactly your age.] ''')
include_zeros = st.selectbox('Do you want to include points in the data for 0 capital gain?', 
                             ['yes', 'no']) 
# ------------------------------------------------------------------------------------------------

if index_forX == 'age':  
  index_forX = 1
if index_forX == 'education': 
  index_forX = 2
if index_forX == 'country': 
  index_forX = 3
if index_forX == 'sex': 
  index_forX = 4
if index_forX == 'marital': 
  index_forX = 5
if index_forX == 'workclass': 
  index_forX = 6

if include_zeros == 'yes':
  include_zeros = 1
else:
  include_zeros = 0

new_keys = []
indeces = []
for i in range(len(selected_cond)):
  for j in range(len(key_words)):
    if selected_cond[i] == key_words[j]:
      indeces.append(corresponding_index[j])
      new_keys.append(key_words[j])

if new_keys[0] == 'age':
  if len(new_keys)== 1:
    conditions = ((df1[new_keys[0]] >= person_info[indeces[0]]-5) & (df1[new_keys[0]] <= person_info[indeces[0]]+5) &
                  (include_zeros or df1['capital-gain']) )
  elif len(new_keys)== 2:
    conditions = (
      (df1[new_keys[0]] >= person_info[indeces[0]]-5) & (df1[new_keys[0]] <= person_info[indeces[0]]+5) & 
      (df1[new_keys[1]] == person_info[indeces[1]])&
                  (include_zeros or df1['capital-gain']) )
  elif len(new_keys)== 3:
    conditions = (
      (df1[new_keys[0]] >= person_info[indeces[0]]-5) & (df1[new_keys[0]] <= person_info[indeces[0]]+5) & 
      (df1[new_keys[1]] == person_info[indeces[1]]) &
      (df1[new_keys[2]] == person_info[indeces[2]])&
                  (include_zeros or df1['capital-gain']))
  elif len(new_keys)== 4:
    conditions = (
      (df1[new_keys[0]] >= person_info[indeces[0]]-5) & (df1[new_keys[0]] <= person_info[indeces[0]]+5) & 
      (df1[new_keys[1]] == person_info[indeces[1]]) &
      (df1[new_keys[2]] == person_info[indeces[2]]) &
      (df1[new_keys[3]] == person_info[indeces[3]])&
                  (include_zeros or df1['capital-gain']))
  elif len(new_keys)== 5:
    conditions = (
      (df1[new_keys[0]] >= person_info[indeces[0]]-5) & (df1[new_keys[0]] <= person_info[indeces[0]]+5) & 
      (df1[new_keys[1]] == person_info[indeces[1]]) &
      (df1[new_keys[2]] == person_info[indeces[2]]) &
      (df1[new_keys[3]] == person_info[indeces[3]]) &
      (df1[new_keys[4]] == person_info[indeces[4]])&
                  (include_zeros or df1['capital-gain'])
    )
else:
  if len(new_keys)== 1:
    conditions = ((df1[new_keys[0]] == person_info[indeces[0]])&
                  (include_zeros or df1['capital-gain']))
  elif len(new_keys)== 2:
    conditions = (
      (df1[new_keys[0]] == person_info[indeces[0]]) & 
      (df1[new_keys[1]] == person_info[indeces[1]]) &
                  (include_zeros or df1['capital-gain']))
  elif len(new_keys)== 3:
    conditions = (
      (df1[new_keys[0]] == person_info[indeces[0]]) & 
      (df1[new_keys[1]] == person_info[indeces[1]]) &
      (df1[new_keys[2]] == person_info[indeces[2]])&
                  (include_zeros or df1['capital-gain']))
  elif len(new_keys)== 4:
    conditions = (
      (df1[new_keys[0]] == person_info[indeces[0]]) & 
      (df1[new_keys[1]] == person_info[indeces[1]]) &
      (df1[new_keys[2]] == person_info[indeces[2]]) &
      (df1[new_keys[3]] == person_info[indeces[3]])&
                  (include_zeros or df1['capital-gain']))
  elif len(new_keys)== 5:
    conditions = (
      (df1[new_keys[0]] == person_info[indeces[0]]) & 
      (df1[new_keys[1]] == person_info[indeces[1]]) &
      (df1[new_keys[2]] == person_info[indeces[2]]) &
      (df1[new_keys[3]] == person_info[indeces[3]]) &
      (df1[new_keys[4]] == person_info[indeces[4]]) &
                  (include_zeros or df1['capital-gain'])
    )

# Create a duplicate DataFrame with selected conditions
selected_df = df1[conditions].copy()


#PLOTTING AND DISPLAY ----------------------------------------------------------------

if isinstance(percentage_highearners, str):
  st.write("Percentage of over-earners:", percentage_highearners)
else:
  st.write("Percentage of over-earners:", percentage_highearners*100)
st.write("Amount of people with specified characteristics:", sum_all)
#st.write(selected_df[key_words[index_forX]])
#st.write(selected_df['capital-gain'])
name = "Capital gains for people with the same: " + selected_cond[0]
for i in range(1, len(selected_cond)):
  n = ', ' + selected_cond[i] 
  name += n
st.markdown(f"""  #### <span style="color:green">{name}</span>  """,  unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=[20,15])
selected_df.plot.scatter(x=key_words[index_forX],
      y='capital-gain', c='olivedrab', ax = ax)
plt.show()
st.pyplot(fig)




name = "Median income for people with similar characteristics to you"
st.markdown(f"""  #### <span style="color:green">{name}</span>  """,  unsafe_allow_html=True)
def color_coding(row):
    return ['background-color:red'] * len(
        row) if row['Median income'] >= person_info[0] else ['background-color:green'] * len(row)
table = {'Group':median_keys, 'Median income':median_info }
df_table = pd.DataFrame(table)
st.dataframe(df_table.style.apply(color_coding, axis=1), column_config= {
  "widgets": st.column_config.Column( help = '''Color red: your earnings are under the median for this population\n 
        Color green: your earnings are over the median for this population''')
})


