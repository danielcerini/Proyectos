# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:28:24 2024

@author: danie
"""
import numpy as np
import matplotlib.pyplot as plt
import random
import math

"""Estudio estadístico de Llenado de un album mediante numeros aleatorios uniformes"""

def album(n):
    return([0]*n)

#### DISTRIBUCION UNIFORME DE FIGURITAS EN CADA PAQUETE-------------------
def paquete(k):
    figus=[]
    for i in range(k):
        figu=random.randint(0,N-1)
        figus.append(figu)
    return (figus)


def albumlleno(album):
    suma=sum(album)
    lleno=False
    if suma==N:
        lleno=True
    return(lleno)


def llenar1paq(k):
    figus=paquete(k)
    for i in range(k):
        mialbum[figus[i]]=1


#Cantidad de personas que compran paquetes hasta llenar el album
personas=3000


llenados=[]
for i in range(personas):
    mialbum=album(N)
    compras=0
    K=10
    while albumlleno(mialbum)==False:
        llenar1paq(K)
        compras+=1
    llenados.append(compras)
    
media=np.mean(np.array(llenados))
plt.hist(llenados,density=True)
plt.title("Media = %f"%media)
plt.xlabel("Paquetes de %i figuritas comprados hasta llenar el album"%K)
plt.ylabel("Personas")


#----------------------------------------------------------------
"""Distribucion teórica cuando las figuritas son equiprobables"""
#Compra de muchas figus de a una y evaluo la probabilidad de que haya completado
##P(X_1>=1,X_2>=1,...,X_N>=1)
##X_i: cantidad de figus de la numero i

#Defino funcion recursiva que muestre todas las particiones de un num
#ignorando el orden de los sumandos
def particiones(n, max_val=None):
    if max_val is None:
        max_val = n
    if n == 0:
        return [[]]
    resultado = []
    for i in range(min(n, max_val), 0, -1):
        for particion in particiones(n - i, i):
            # print(i, particion)
            resultado.append([i] + particion)
    return resultado


#De las particiones de n me quedo con las que tienen m sumandos 
def filtro (n,m):
    part=particiones(n)
    res=[]
    for i in range(len(part)):
        if len(part[i])==m:
            res.append(part[i])
    return(res)

#Defino coeficiente multinomial
def coefmulti(listan):
    N=sum(listan)
    den=1
    for i in range(len(listan)):
        den=den*math.factorial(listan[i])
    return(math.factorial(N)/den)


#Funcion de prob de la distribucion multinomial
def distmulti(listan, listap):
    coef=coefmulti(listan)
    p=1
    for i in range(len(listap)):
        p=p*listap[i]**listan[i]
    return(coef*p)
        

from collections import Counter

#Numero de figuritas del album
N=6

#Defino funcion que cuente las posibles permutaciones de una lista de num
#para contar configuraciones equiprobables
def perm(lista):
    repesdic=Counter(lista)
    repes=list(repesdic.values())
    comb=coefmulti(repes)
    return(comb)


#Calculo la probabilidad de llenar un album de N si compré "compra" figuritas
def probalbumlleno(N,compra):
    p=[1/N]*N
    eventos=filtro(compra,N)
    resultado=0
    for i in range(len(eventos)):
        resultado+=perm(eventos[i])*distmulti(eventos[i],p)
    return(resultado)


##Compro figuritas equiprobables
  
for i in range(N,30):
    plt.scatter(i,probalbumlleno(N,i))

plt.grid()
plt.xlabel("Figuritas compradas")
plt.ylabel("Probabilidad de llenar el álbum")
plt.title("Probabilidad de llenar un álbum de %i figuritas"%N)



