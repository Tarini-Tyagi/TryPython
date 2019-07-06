# -*- coding: utf-8 -*-
"""RandomF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nrNff1T25I2yj39PZvVFq5tt3lFs1U-q
"""

# Random Forest
import pandas as pd

df=pd.read_csv("http://13.234.66.67/summer19/datasets/social.csv")

# schema
df.info   # for data
df.info()  # for schema

# top 5 rows

df.head()

# removing user ID
filterdaata=df.iloc[0:,1:]

"""# take picture of person - recognize tshirt pattern - search and show the best offer on similar type stuff"""



# removing user ID
filterdata=df.iloc[0:,2:].values

# can label encode here

# features scaling for age and salary
# age too low sal too high, so we have to bring both in range
# Now apply traing test
features=filterdata[0:,0:2]
label=filterdata[0:,2]

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler      # for feature scaling

X,x,Y,y=train_test_split(features,label,test_size=0.2)
sc=StandardScaler()

# apply scaling in train dada only
X=sc.fit_transform(X)
X
# we can't compare this X with the actual data , we'll pass this X to the classifier and match the output with the actual data

# on data always
# Label Encoding
# hot shot /dummy variable
# Features Scaling

# testing data scaling
X=sc.transform(X)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# ensembling : Training itself on same data
# RF call with no. of decesion TREE
Rclf=RandomForestClassifier(n_estimators=20)   # By default it takes 10 trees

# Train the data
trained=Rclf.fit(X,Y)
# Predicting 
output=trained.predict(x)

output   # Predicted

y    # Actual

# to find acurracy score
from sklearn.metrics import accuracy_score
d=accuracy_score(output,y)

d

# RDS -- cloud good topic