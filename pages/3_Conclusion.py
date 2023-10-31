import streamlit as st


#*********************************************************************************************************
#CODE FOR GETTING STANDARD INFO OUT OF THE DATA ----------------------------------------------------------------
#*********************************************************************************************************


#Code for preliminary look at census and income dataset

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/adult_data.csv'
df_census = pd.read_csv(url)
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
  #print("\ngroup:", groups[i])
  #print('sum of people:', sum_of_people[i], 'and sum of all people:', sum_all_people[i])
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
