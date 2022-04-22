# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:31:51 2022

@author: PC
"""
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('dataR2.csv')
print(df.describe())
#Grafico de dispersion, que nos servira para representar la relacion
#de dos variables

#Ej. Ver la relacion entre 
#HOMA (Evaluación del modelo de homeostasis) y  la glucosa

df.plot.scatter(x="HOMA", y="Glucose")
plt.show()

#en el eje y se tiene el valor de la glucosa 
#mientras mas arriba este el punto es mayor la cantidad de glucosa
#se ve una correlacion que nos indica que a mayor cantidad de 
#glucosa menor indice de (Evaluación del modelo de homeostasis)



#Ej. Ver la relacion entre 
#HOMA (Evaluación del modelo de homeostasis) y  la glucosa

df.plot.scatter(x="Insulin", y="Glucose")
plt.show()

#en el eje x se tiene el valor de la insulina que es la que regula la 
#cantidad de glucosa existente en la sangre,en el eje y se tiene el valor 
#de la glucosa 
#Como se puede observar en el grafico, en la correlacion observamos que que a mayor 
#cantidad de insulina se vera alrededor de la misma cantidad la glucosa en la sangre 


#matriz con scatterplot
df.info()
pd.plotting.scatter_matrix(df.loc[:,'Age':'MCP.1'])
