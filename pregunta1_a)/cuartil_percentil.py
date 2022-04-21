# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:48:13 2022

@author: PC
"""

import numpy as np
import pandas as pd
df=pd.read_csv('dataR2.csv')
df=df.replace(np.nan,0)
print(df.dtypes)
print("**************CUARTILES*************")
print("---------------Age-----------")
lista_valores1=df['Age'].tolist()
#print(lista_valores1)
lista_ordenada1=sorted(lista_valores1)
#print(lista_ordenada1)
long1=len(lista_ordenada1)
#print("longitud")
#print(long1)

q=(1*(long1+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada1[a-1]
val2=lista_ordenada1[a]

quantil1=val1+((val2-val1)*b)
print("------------Primer cuartil--------------")
print(quantil1)
q=(1*long1)/4
print("quantil",lista_ordenada1[int(q)])
print(np.quantile(df["Age"],[0.25]))

#Lo que se puede concluir:
#El 25% de personas mujeres tienen 44 o menos de 44 años de edad   
    

print("---------------BMI-----------")
lista_valores=df['BMI'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(1*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------Primer cuartil--------------")
print(quantil)
#Lo que se puede concluir:
#El 25% de personas mujeres realizandose un examen se observa que 
#tienen unBMI en un numero igual o menor a 22  


print("---------------Glucose-----------")
lista_valores=df['Glucose'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(1*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------Primer cuartil--------------")
print(quantil)
#Lo que se puede concluir:
#El 25% de personas mujeres tienen 85 o menos de 85 en lo que se refiere 
#a cantidad de glucosa  

print("---------------INSULIN-----------")
lista_valores=df['Insulin'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(1*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------Primer cuartil--------------")
print(quantil)
#El 25% de personas mujeres tienen 4 o menos de 4 en lo que se refiere 
#a cantidad de insulina  

print("---------------HOMA-----------")
lista_valores=df['HOMA'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(1*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------Primer cuartil--------------")
print(quantil)
#El 25% de personas mujeres respecto a evaluación del modelo de 
#homeostasis cuentan casi con numero cercano a uno del mismo


print("---------------Leptin-----------")
lista_valores=df['Leptin'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(1*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------Primer cuartil--------------")
print(quantil)


print("---------------Adiponectin-----------")
lista_valores=df['Adiponectin'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(1*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------Primer cuartil--------------")
print(quantil)


print("---------------Resistin-----------")
lista_valores=df['Resistin'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)


q=(1*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------Primer cuartil--------------")
print(quantil)


print("---------------MCP.1-----------")
lista_valores=df['MCP.1'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(1*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------Primer cuartil--------------")
print(quantil)
#Quimiocina Monocito Quimioatrayente Proteína 1(MCP.1)




print("**************PERCENTILES*************")
#El segundo cuartil equivale al perceptil 50

print("---------------Age-----------")
lista_valores1=df['Age'].tolist()
#print(lista_valores1)
lista_ordenada1=sorted(lista_valores1)
#print(lista_ordenada1)
long1=len(lista_ordenada1)
#print("longitud")
#print(long1)

q=(2*(long1+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada1[a-1]
val2=lista_ordenada1[a]

quantil1=val1+((val2-val1)*b)
print("------------percentil 50--------------")
print(quantil1)


print("---------------BMI-----------")
lista_valores=df['BMI'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(2*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------percentil 50--------------")
print(quantil)

print("---------------Glucose-----------")
lista_valores=df['Glucose'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(2*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------percentil 50--------------")
print(quantil)


print("---------------INSULIN-----------")
lista_valores=df['Insulin'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(2*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------percentil 50--------------")
print(quantil)

print("---------------HOMA-----------")
lista_valores=df['HOMA'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(2*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------percentil 50--------------")
print(quantil)


print("---------------Leptin-----------")
lista_valores=df['Leptin'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(2*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------percentil 50--------------")
print(quantil)


print("---------------Adiponectin-----------")
lista_valores=df['Adiponectin'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(2*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------percentil 50--------------")
print(quantil)


print("---------------Resistin-----------")
lista_valores=df['Resistin'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)


q=(2*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("------------percentil 50--------------")
print(quantil)


print("---------------MCP.1-----------")
lista_valores=df['MCP.1'].tolist()
#print(lista_valores)
lista_ordenada=sorted(lista_valores)
#print(lista_ordenada)
long=len(lista_ordenada)
#print("longitud")
#print(long)

q=(2*(long+1))/4
#print("posicion")
#print(q)
a = int(q) #Parte entera con o sin signo
b = abs(q) - abs(int(q)) #Parte decimal
#print("parte entera")
#print(a)
#print("parte decimal")
#print(b)

val1=lista_ordenada[a-1]
val2=lista_ordenada[a]

quantil=val1+((val2-val1)*b)
print("-----------percentil 50--------------")
print(quantil)














