
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


url = 'https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/midterm/adult_data.csv'
df_census = pd.read_csv(url)


st.title("Can income level be predicted from these characteristics?")
#GOAL: Determine weather a person is under or over earner based on their characteristics from the census data





#*********************************************************************************************************
#CODE TO GET STANDARD INFO OUT OF THE DATA ----------------------------------------------------------------
#*********************************************************************************************************

#Cleaning data -------------------------------------------------------------------

df1 = df_census.copy()
num_attributes = 8

# Define a mapping dictionary to reduce amount of distinct values to make data more manegable
# To get unique values in a column one should use: * unique_values = df1['mariatl'].unique() *
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
education_dict = {'Preschool': 1, '1st-4th': 2, '5th-6th': 3, '7th-8th': 4, '9th': 5, '10th': 6,
                  '11th': 7, '12th': 8, 'HS-grad': 9, 'Some-college': 10, 'Assoc-acdm': 11, 'Assoc-voc': 12,
                  'Bachelors': 13, 'Masters': 14, 'Prof-school': 15, 'Doctorate': 16}

# Replace string values with corresponding values
df1['countr'] = df1['countr'].replace(country_to_regions)
df1['mariatl'] = df1['mariatl'].replace(marital_married)

#Dropping unnecessary columns
df1 = df1.drop(['fnlwgt','education', 'occupation', 'relationship', 'capital-gain', 
                'capital-loss', 'hours-per-week'], axis=1)

string_to_int_dicts = []
# Create encoder from string to integer and make all data numerical 
for i in range(num_attributes-1):   #We skip the first column which is age
  label_encoder = LabelEncoder()
  integer_encoded = label_encoder.fit_transform(df1[df1.columns[i+1]])
  string_to_integer_dict = {label: index for index, label in enumerate(label_encoder.classes_)}
  df1[df1.columns[i+1]] = df1[df1.columns[i+1]].replace(string_to_integer_dict)
  string_to_int_dicts.append(string_to_integer_dict)
  



#Creating model and testing -------------------------------------------------------------------

X = df1.iloc[:, :7]
y = df1.iloc[:, -1]

start_state = 42     #integer of the amount of "shuffles" before splitting the data into train and test
test_fraction = 0.2     #float for test percentage from data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_fraction, random_state=start_state)     #function that splits X and y into random subsets of train and test with 20% for test

my_scaler = StandardScaler()     #standardize features by removing the mean and scaling to unit variance
my_scaler.fit(X_train)     # y_train isn't used here because the scaler's purpose is to transform the input features

X_train_scaled = my_scaler.transform(X_train)     #scaling the input features for the train set
X_test_scaled = my_scaler.transform(X_test)     #scaling the input features for the test set

my_classifier = GradientBoostingClassifier(random_state=0)
my_model = my_classifier.fit(X_train_scaled, y_train)
y_pred = my_model.predict(X_test_scaled)
# Calculate the accuracy score
score = accuracy_score(y_test, y_pred)




#*********************************************************************************************************
#CODE FOR WEB-APP IMPLEMENTATION --------------------------------------------------------------------------
#*********************************************************************************************************

st.markdown(''' 
We've made a model with the data previously explored, using an algorithm from sklearn called Gradient Boosting Classifier.
Here is the process: 
  * We "shuffled" the data and splitted it into training and testing arrays.
  * The model is given the training data, and after it has been trained, we meassure the level of accuracy by 
    giving the model the test data and counting the amount of correct predictions.
More information about the results can be found bellow. 
''')
st.write(f"Accuracy of the model: {score}", unsafe_allow_html=True)
    print("<h1 style='font-size: 18px;'> Accuracy of the model: </h1>", score)

# TEXT INPUT -------------------------------------------------------------------------------------
st.markdown('#### Upload your info here:')
person_age = st.slider('Age:', min_value = 1, max_value = 100)
person_sex = st.selectbox("Sex/gender:", 
        ["Male", "Female"])
person_education = st.selectbox("Education level:", 
        ['1st-4th', '5th-6th', '7th-8th', '9th', '10th', '11th', '12th', 'Assoc-acdm', 'Assoc-voc', 'Bachelors', 
         'Doctorate', 'HS-grad', 'Masters', 'Preschool', 'Prof-school', 'Some-college'])
person_country = st.selectbox("Region of origin:", 
        ['United_States', 'South_America', 'Asia', 'Europe', 'Canada', 'Other'])
if person_country == 'Other':
  person_country = '?'
person_industry = st.selectbox("Work sector:", 
        ['State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov', 'Local-gov', 'Other'])
if person_industry == 'Other':
  person_industry = '?'
person_marital = st.selectbox("Marital status:", 
        ['Never-married', 'Married', 'Divorced', 'Separated', 'Widowed'])
person_race = st.selectbox("Race:", 
        ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'])


#Changing the data into numeric
person_education = education_dict.get(person_education, 0)  # Default to 0 if key is not found
person_info = [person_age, person_industry, person_education, person_marital, person_race, person_sex, person_country]
for i in range(len(string_to_int_dicts)-1):
  person_info[i+1] = string_to_int_dicts[i].get(person_info[i+1], 0)

x = [person_info]
pred =  my_model.predict(x)


#PRESENT INFO TO USER -----------------------------------------------------------------

with st.expander('What is Gradient Boosting?'):
  st.markdown('''
      "This algorithm builds an additive model in a forward stage-wise fashion; it allows for the optimization of 
      arbitrary differentiable loss functions. In each stage n_classes_ regression trees are fit on the negative 
      gradient of the loss function, e.g. binary or multiclass log loss. Binary classification is a special case 
      where only a single regression tree is induced."

      Source: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html
  ''', unsafe_allow_html=True)
  
with st.expander('Results of predictions'):
  st.markdown('''
 
  ''', unsafe_allow_html=True)
  conf_mat = confusion_matrix(y_test, y_pred)
  fig, ax = plt.subplots()
  disp = ConfusionMatrixDisplay(conf_mat, display_labels=df1.iloc[:, -1].unique())
  disp.plot(cmap='viridis', values_format='d', ax=ax)
  st.pyplot(fig)

if pred[0] == 1:
  st.markdown("Our system predicts that you earn **over** $50,000 per year.")
else:
  st.markdown("Our system predicts that you earn **less** than $50,000 per year.")

