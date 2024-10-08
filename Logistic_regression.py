# -*- coding: utf-8 -*-
"""Vital_Monitoring_System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p00aZ9S2bE-SEVcFmuoJllwfb6DPA_-M
"""

pip install catboost

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import xgboost as xgb
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.metrics import mean_squared_error, mean_absolute_error

data = pd.read_csv('/content/24_hrs_fin.csv')
data

df = pd.DataFrame(data)

df['Label'] = df['Label'].astype(int)

col_name = 'Label'
col_data = [col_name]
num_zeros = (df['Label'] == 0).sum()
num_ones = (df['Label']  == 1).sum()
print("Number of zeros in column '%s': %d" % (col_name, num_zeros))
print("Number of ones in column '%s': %d" % (col_name, num_ones))

df.drop(columns = ['TimeStamp'])

X = df[['AccX','AccY','AccZ','GyroX','GyroY','GyroZ','Temp','Gas','RotX','RotY','RotZ','RotW','RotAcc','Pressure','HeartRate','AQI']]
y = df['Label']

from sklearn.preprocessing import MinMaxScaler

# Create an instance of MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the data
data = scaler.fit_transform(df)

from imblearn.over_sampling import RandomOverSampler
import pandas as pd

# assume that you have an imbalanced dataframe df with the target variable 'y'

# define the RandomOverSampler object
oversampler = RandomOverSampler(random_state=42)

# perform random oversampling on the dataset
X, y = oversampler.fit_resample(X, y)

# create a new dataframe for the resampled data
resampled_df = pd.concat([pd.DataFrame(X), pd.DataFrame(y)], axis=1)

# print the number of samples in each class before and after oversampling
print('Original dataset shape:', data.shape)
print('Resampled dataset shape:', resampled_df.shape)
#print('Original class distribution:\n', data['y'].value_counts())
#print('Resampled class distribution:\n', resampled_df['y'].value_counts())

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.metrics import mean_squared_error, mean_absolute_error
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# create a logistic regression classifier and fit it on the training set
lr = LogisticRegression()
lr.fit(X_train, y_train)

# make predictions on the test set
y_pred = lr.predict(X_test)

# evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy 3:", accuracy)

# calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)

# calculate the root mean squared error
rmse = np.sqrt(mse)
print("RMSE 3:", rmse)

# calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

# calculate the mean absolute error
mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae)

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error

# Assuming X and y are already defined as your dataset and labels
# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression classifier and fit it on the training set
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lr.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

# Calculate the root mean squared error
rmse = np.sqrt(mse)
print("RMSE:", rmse)

# Calculate the mean absolute error
mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae)

def predict_output(X_test_scaled):
    # Predict the output using the trained logistic regression model
    output = lr.predict(X_test_scaled)
    return output

# Prompt the user to enter values for each feature
AccX = float(input("Enter AccX value: "))
AccY = float(input("Enter AccY value: "))
AccZ = float(input("Enter AccZ value: "))
GyroX = float(input("Enter GyroX value: "))
GyroY = float(input("Enter GyroY value: "))
GyroZ = float(input("Enter GyroZ value: "))
Temp = float(input("Enter Temp value: "))
Gas = float(input("Enter Gas value: "))
RotX = float(input("Enter RotX value: "))
RotY = float(input("Enter RotY value: "))
RotZ = float(input("Enter RotZ value: "))
RotW = float(input("Enter RotW value: "))
RotAcc = float(input("Enter RotAcc value: "))
Pressure = float(input("Enter Pressure value: "))
HeartRate = float(input("Enter HeartRate value: "))
AQI = float(input("Enter AQI value: "))

# Create the input sequence from user input
input_sequence = np.array([
    [AccX, AccY, AccZ, GyroX, GyroY, GyroZ, Temp, Gas, RotX, RotY, RotZ, RotW, RotAcc, Pressure, HeartRate, AQI]
])

# Ensure the input data has the correct shape
print("Input data shape:", input_sequence.shape)

# Predict output using the predict_output function defined earlier
predicted_output = predict_output(input_sequence)
print("Predicted output:", predicted_output)