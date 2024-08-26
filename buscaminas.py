# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 00:16:13 2024

@author: danie
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import math

#Creo un tablero vacio de m filas y n columnas donde coloco una cantidad de minas
def tablero(m,n,minas):
    tab=[0]*m*n
    pos=[i for i in range(m*n)]
    minascol=0
    while minascol<minas:
        indiceazar=random.randint(0,m*n-1)
        if tab[indiceazar]==0:
            tab[indiceazar]="X"
            minascol+=1
    tab=np.reshape(np.array(tab),[m,n])
    return (tab)

mitab=tablero(8,8,24)
# print(mitab)

#Defino funcion que diga si en la posicion (i,j) hay una mina
def haymina(tablero,i,j):
    resultado=False
    if tablero[i,j]=="X":
        resultado=True
    return resultado


#Defino una funcion que me diga si un par (i,j) está fuera del tablero
def fueralim(tablero,i,j):
    N=np.shape(tablero)[0]
    M=np.shape(tablero)[1]
    resultado=False
    if i<0 or j<0 or i>=N or j>=M:
        resultado=True
    return(resultado)
    
    
# print(fueralim(mitab,8,3))

#Defino una funcion que cuente la cantidad de minas alrededor de (i,j)    
def contminas(tablero,i,j):
    minas=0
    tab=tablero.copy()
    vecinos=[[i-1,j-1],[i-1,j],[i-1,j+1],[i,j+1],[i+1,j+1],[i+1,j],[i+1,j-1],
              [i,j-1]]
    for k in range(len(vecinos)):
        fila=vecinos[k][0]
        col=vecinos[k][1]
        if fueralim(tablero,fila,col)==False and haymina(tablero,i,j)==False:
            minas+=haymina(tablero,fila,col)
            tab[i,j]=str(minas)
    return tab

#Aplico funcion anterior a todo el tablero
def tabnum(tablero):
    N=np.shape(tablero)[0]
    M=np.shape(tablero)[1]
    tab=tablero.copy()
    for i in range(N):
        for j in range(M):
            tab=contminas(tab,i,j)
    return tab

mitab=tabnum(mitab)
# print(mitab)

#Cuento la cantidad de veces que aparece num en un tablero dado
def contadornum(tablero,num):
    apariciones=0
    for i in range(len(tablero)):
        apariciones+=list(tablero[i]).count(str(num))
    return apariciones

#Frecuencias de todos los numeros del 0 al 8 inclusive
def contadortot(tablero):
    resultado=np.zeros(9)
    for i in range(9):
        resultado[i]=contadornum(tablero,i)
    return resultado


#Grafico y comparo con la distribucion Poisson

x= range(9)
frecuencias=np.zeros(9)
numtab=500


for i in range(numtab):
    mitab=tablero(20,20,100)
    mitab=tabnum(mitab)
    frecuencias+=contadortot(mitab)
    


media=1/sum(frecuencias)*np.dot(np.array(x),frecuencias)
desv=np.sqrt(1/(sum(frecuencias)-1)*np.dot(frecuencias,(x-media)**2))

print("Media = %f"%media)
print("Desviacion estandar = %f"%desv)

frecuencias=1/sum(frecuencias)*frecuencias
    
plt.bar(x, frecuencias)
# plt.scatter(x, frecuencias, color='r')
plt.title('Distribución de los números que aparecen en el tablero')
plt.xlabel('Casillero')
plt.ylabel('Frecuencia')

#Comparo con una distribucion Poisson
for i in x:
    plt.scatter(i,media**i/math.factorial(i)*np.exp(-media),color='r')

plt.legend(["Distribucion Poisson"])

