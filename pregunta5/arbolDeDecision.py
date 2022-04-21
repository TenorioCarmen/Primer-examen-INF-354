# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 06:10:48 2022

@author: PC
"""
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

df=pd.read_csv('dataR2.csv')
df=df.replace(np.nan,"0")

print(df.sample(10))
explicativas=df.drop(columns='Classification')
objetivo=df.Classification

model=DecisionTreeClassifier(max_depth=3)
model.fit(X=explicativas,y=objetivo)
DecisionTreeClassifier()

plot_tree(decision_tree=model,feature_names=explicativas.columns,filled=True,fontsize=8)
plt.figure(figsize=(14,8))



