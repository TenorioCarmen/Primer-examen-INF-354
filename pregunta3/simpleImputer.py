# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 07:57:35 2022

@author: PC
"""
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

df=pd.read_csv('dataR2.csv')
print(df)
prepro = SimpleImputer(missing_values=np.nan, strategy="mean")
X2=prepro.fit_transform(df)
print(X2)

print("-----------------------------------")
imp = SimpleImputer(missing_values=np.nan, strategy="mean")
imp.fit(df)
df=imp.transform(df)
print(df)

df=pd.DataFrame(imp.transform(df),columns=["Age","BMI ","Glucose","Insulin","HOMA", "Leptin", "Adiponectin","Resistin", "MCP.1", "Classification" ],dtype=int)
print(df)