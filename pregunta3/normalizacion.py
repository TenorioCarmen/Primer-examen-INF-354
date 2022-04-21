# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:00:10 2022

@author: PC
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing

datos=pd.read_csv('dataR2.csv')
datos=datos.replace(np.nan,"0")
df=pd.DataFrame(datos)
print(df['MCP.1'].describe())

fig,(ax1,ax2)=plt.subplots(ncols=2,figsize=(6,5))
ax1.set_title("Antes de escalar")
sns.kdeplot(df['MCP.1'],ax=ax1)
sns.kdeplot(df['HOMA'],ax=ax1)

scaler=preprocessing.StandardScaler()
#scaler=preprocessing.Normalizer(norm='l2',copy=True)
df[['HOMA','MCP.1']]=scaler.fit_transform(df[['HOMA','MCP.1']])

print("----------------------------")
print(df['MCP.1'].iloc[0])
print(df['MCP.1'].describe())

df.to_csv('prepro.csv',sep='\t')
ax2.set_title("Despues de escalar")
sns.kdeplot(df['MCP.1'],ax=ax2)
sns.kdeplot(df['HOMA'],ax=ax2)

plt.show()








