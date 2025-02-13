# -*- coding: utf-8 -*-
"""xgboost_regressor.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CszoseH94bFTGFSXe2KdPoROB0_PcBB4

##IMPORTING DEPENDENCIES
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""###READING DATASET

Reading dataframe into a variable called df
"""

df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/Regression/insurance.csv")

"""###Checking the first 10 rows of the dataset"""

df.head(10)

"""###Checking the last 10 rows of the dataset"""

df.tail(10)

"""###Checking he columns of the dataset"""

df.columns

"""###Checking the shape of the dataset"""

print(f"Shape of the dataset is: {df.shape}")
print(f"Rows in dataset: {df.shape[0]}")
print(f"Collumns in dataset: {df.shape[1]}")

"""###Cheching Null values in dataset"""

df.isna().sum()

"""###Checking general information on dataset"""

df.info()

"""###Getting statistical insights on the dataset

###Plotting different graphs to see the distribution of data
"""

df.describe(include='all')

"""###Seprating object datatypes and numeric datatypes"""

#Selecting all columns of object data type
df_object = df.select_dtypes(include="object")

#Selecting all columns of numerical data type
df_numeric = df.select_dtypes(exclude="object")

"""###Encoding object data type columns"""

#checking distribution of data in each category
for column in df_object.columns:
  print(f"Unique values in {column} are {df[column].value_counts()}")
  print()

"""###Checking the distribution grphiclly"""

for column in df_object.columns:
  plt.bar(df[column], df['charges'])
  plt.title(column)
  plt.tight_layout()
  plt.show()

"""categories of 'Sex' and 'Region' column are is almost equally distributed, but smoker is not, as number of 'no' in 'smoker' columns is high, the ml algorith might be biased towards 'no' catrgory"""

#checking distribution of data in each numrical category
for column in df_numeric.columns:
  plt.hist(df[column], density=True)
  plt.title(column)
  plt.tight_layout()
  plt.show()

"""###most of the numerical columns are normally distributued

#DATA PREPROCESSING

TRANSFORMING OBJECT COLUMNS TO NUMERICAL COLUMNS

1. BY ONE HOT ENCODING FROM SKLEARN LIBRARY
2. BY PD.GET_DUMMIES METHOD
3. BY USING MAP FUNCTION
"""

for column in df_object:
  print(f"Unique values in {column} column are {df[column].unique()}")
  print()

"""USING GET DUMMIES METHOD TO ENCODE 'SEX' AND 'SMOKER' AND MAP TO ENCODE 'REGION'"""

#Creating a new column where insted of male or female it would show if male is true or false
df = pd.get_dummies(df, columns=['sex'], drop_first=True)

"""DOING THE SAME FOR SMOKER COLUMN"""

#Creating a new column where insted of male or female it would show if male is true or false
df = pd.get_dummies(df, columns=['smoker'], drop_first=True)

"""USING MAP FUNCTION TO ENCODE REGION"""

df['region'].unique()

"""Mapping       
'southwest' as 0,          
'southeast' as 1,         
'northwest' as 2,         
'northeast' as 3
"""

df['region'] = df['region'].map({'southwest':0, 'southeast' : 1, 'northwest' : 2, 'northeast' : 3 })

#Checking dataset afer encoding
df

#Checking correlation of columns with each other
df.corr()

#Checing correlation with a heatmap for visualization
sns.heatmap(df.corr(), annot=True)

#Checking correlation with charges column to each column
corelation_with_charges = df.corr()['charges']
corelation_with_charges

"""VISUALLY HECKING THE CORRELATION WITH CHARGES COLUMNS"""

#Creating x axis
x_axis = corelation_with_charges.index

#Creating y axis
y_axis = [corelation_with_charges[i] for i in corelation_with_charges.index]


#Plotting the graph
plt.bar(x_axis, y_axis)
plt.xlabel("Properties")
plt.ylabel("Correlation")
plt.title("Correlation with chrges")
plt.tight_layout()
plt.show()

"""We can see Smoker, Age and BMI are very corelated with charges but children, region and sex are not so correlated.

#SPLITTING DATA INTO DEPENDENT ND INDEPENDENT VARIABLE
"""

X = df.drop('charges', axis=1)
y = df['charges']

"""#SPLITTING DATA INTO TRAIN AND TEST"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=20)

#Checking shape of the datasets
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

"""## Implementing XGBoost regressor"""

#Importing algorithm
from xgboost import XGBRegressor

#Creating instance
xgb_model = XGBRegressor()

#Fitting data
xgb_model.fit(X_train, y_train)

"""Prediction and scoring"""

xgb_model_prediction = xgb_model.predict(X_test)

#Model's score with training data
score_with_training_set = xgb_model.score(X_train, y_train)
print(f"Model's score with training data is: {score_with_training_set}")


#Model's score with test data
score_with_test_set = xgb_model.score(X_test, y_test)
print(f"Model's score with test data is: {score_with_test_set}")


#Model's score with full data
score_with_full_set = xgb_model.score(X, y)
print(f"Model's score with full data is: {score_with_full_set}")

"""# XGB Regresson model is providing a good acuracy but is overfit."""