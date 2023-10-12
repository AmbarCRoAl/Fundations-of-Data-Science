pip install seaborn

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error


points = [
    {'x':0.5, 'y':2},
    {'x': 1, 'y':1}]
df1= pd.DataFrame(points)
df22=sns.load_dataset("mpg")
df22=df22.dropna()
ncols = df22.select_dtypes(include=[np.number]).columns
df2=df22[ncols]
st.title("Regression Analysis App")
dataset_choice = st.selectbox("Select a dataset:", ("Custom Dataset", "Seaborn MPG Dataset"))
# User selects dataset

if dataset_choice == "Custom Dataset":
    selected_data = custom_data
    x_variable = 'X'  # Set the default x-variable for the custom dataset
    y_variable = 'Y'  # Set the default y-variable for the custom dataset
else:
    selected_data = mpg_data
    x_variable = st.selectbox("Select the X-variable:", list(mpg_data.columns))
    y_variable = st.selectbox("Select the Y-variable:", list(mpg_data.columns))
# Display selected dataset
st.dataframe(selected_data)
# Regression model selection
model_choice = st.radio("Select a regression model:", ("Line", "RBF-NN"))
# Regression and Plotting
if model_choice == "Line":
    st.subheader("Linear Regression")
    slope = st.slider("Select slope:", min_value=-10.0, max_value=10.0, step=0.1, value=1.0)
    intercept = st.slider("Select intercept:", min_value=-10.0, max_value=10.0, step=0.1, value=0.0)
    # Calculate predictions
    y_pred = slope * selected_data[x_variable] + intercept
    # Plot the data and regression line
    plt.figure(figsize=(8, 6))
    plt.scatter(selected_data[x_variable], selected_data[y_variable], label="Data Points")
    plt.plot(selected_data[x_variable], y_pred, color='red', label="Regression Line")
    plt.xlabel(x_variable)
    plt.ylabel(y_variable)
    plt.legend()
    st.pyplot()
    # Calculate and display error metrics
    mae = mean_absolute_error(selected_data[y_variable], y_pred)
    mse = mean_squared_error(selected_data[y_variable], y_pred)
    st.write(f"Mean Absolute Error (MAE): {mae}")
    st.write(f"Mean Squared Error (MSE): {mse}")
elif model_choice == "RBF-NN":
    st.subheader("Radial Basis Function Neural Network (RBF-NN)")
    # User input for RBF-NN
    center1 = st.number_input("Center 1:")
    center2 = st.number_input("Center 2:")
    bandwidth = st.number_input("Bandwidth (L):")
    weights = st.number_input("Weights:")
    # Calculate RBF-NN predictions

    def RBF_func(x, w, x1, x2, L):
      y = []
      for i in range(len(x)):
        y.append(w*exp(-(x[i]-x1)**2/L)+ w*exp(-(x[i]-x2)**2/L))
      return y
    x_data = np.array(selected_data[x_variable])
    rbf_nn_predictions = RBF_func(x_data, weights, center1, center2, bandwidth)
    # Plot the data and RBF-NN predictions
    plt.figure(figsize=(8, 6))
    plt.scatter(selected_data[x_variable], selected_data[y_variable], label="Data Points")
    plt.plot(selected_data[x_variable], rbf_nn_predictions, color='red', label="RBF-NN")
    plt.xlabel(x_variable)
    plt.ylabel(y_variable)
    plt.legend()
    st.pyplot()
    # Calculate and display error metrics
    mae = mean_absolute_error(selected_data[y_variable], rbf_nn_predictions)
    mse = mean_squared_error(selected_data[y_variable], rbf_nn_predictions)
    st.write(f"Mean Absolute Error (MAE): {mae}")
    st.write(f"Mean Squared Error (MSE): {mse}")
