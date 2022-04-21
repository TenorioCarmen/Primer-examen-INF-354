# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 00:09:06 2022

@author: PC
"""

import numpy as np
import pandas as pd
df=pd.read_csv('dataR2.csv')
df=df.replace(np.nan,0)
print(df)
#Calculo por columnas
# primer cuartil
print("**************CUARTILES*************")
print(np.quantile(df["Age"],[0.25]))
print(np.quantile(df["BMI"],[0.25]))
print(np.quantile(df["Glucose"],[0.25]))
print(np.quantile(df["Insulin"],[0.25]))
print(np.quantile(df["HOMA"],[0.25]))
print(np.quantile(df["Leptin"],[0.25]))
print(np.quantile(df["Adiponectin"],[0.25]))
print(np.quantile(df["Resistin"],[0.25]))
print(np.quantile(df["MCP.1"],[0.25]))

# perceptil 50
print("**************PERCENTILES*************")
print(np.percentile(df["Age"],[50]))
print(np.percentile(df["BMI"],[50]))
print(np.percentile(df["Glucose"],[50]))
print(np.percentile(df["Insulin"],[50]))
print(np.percentile(df["HOMA"],[50]))
print(np.percentile(df["Leptin"],[50]))
print(np.percentile(df["Adiponectin"],[50]))
print(np.percentile(df["Resistin"],[50]))
print(np.percentile(df["MCP.1"],[50]))
