
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


url = 'https://raw.githubusercontent.com/AmbarCRoAl/Fundations-of-Data-Science/main/midterm/adult_data.csv'
df_census = pd.read_csv(url)


st.title("Can income level be epproximated with these characteristics?")
#GOAL: Determine weather a person is under or over earner based on their characteristics from the census data


#Cleaning data -------------------------------------------------------------------

df1 = df_census.copy()
num_attributes = 15

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

# Replace string values with corresponding values
df1['countr'] = df1['countr'].replace(country_to_regions)
df1['mariatl'] = df1['mariatl'].replace(marital_married)

# Create encoder from string to integer and make all data numerical 
for i in range(num_attributes):
  label_encoder = LabelEncoder()
  integer_encoded = label_encoder.fit_transform(df1.iloc[:,i])
  string_to_integer_dict = {label: index for index, label in enumerate(label_encoder.classes_)}
  df1.iloc[df1.columns[i]] = df1.iloc[df1.columns[i]].replace(string_to_integer_dict)




#Creating model and testing -------------------------------------------------------------------

X = df1.iloc[:, :14]
y = df1.iloc[:, -1]

start_state = 42     #integer of the amount of "shuffles" before splitting the data into train and test
test_fraction = 0.2     #float for test percentage from data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_fraction, random_state=start_state)     #function that splits X and y into random subsets of train and test with 20% for test

my_scaler = StandardScaler()     #standardize features by removing the mean and scaling to unit variance
my_scaler.fit(X_train)     # y_train isn't used here because the scaler's purpose is to transform the input features

X_train_scaled = my_scaler.transform(X_train)     #scaling the input features for the train set
X_test_scaled = my_scaler.transform(X_test)     #scaling the input features for the test set

my_classifier = LinearSVC(random_state=0, tol=0.1)
my_model = my_classifier.fit(X_train_scaled, y_train)
y_pred = my_model.predict(X_test_scaled)
# Calculate the accuracy score
score = accuracy_score(y_test, y_pred)




#Webapp implementation -------------------------------------------------------------------

st.write("Accuracy of the model: ", score)

y_pred = my_model.predict(X_test_scaled)
conf_mat = confusion_matrix(y_test, y_pred)
fig = ConfusionMatrixDisplay.from_estimator(my_classifier, X_test_scaled, y_test)
st.pyplot(fig.plot(cmap='viridis', values_format='d'))
