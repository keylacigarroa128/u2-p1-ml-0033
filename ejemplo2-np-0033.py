# Keyla Paola NC = 0033
import numpy as np

print("-----llenar  matriz de cero -----")
matriz = np.zeros([3,5]) #  3 filas por 5 columnas 
print(matriz)
print("  ")
print("-----llenar matriz de unos -----")
matriz = np.ones([3,5])
print(matriz) 
print("  ")
print("-----llenar matriz vacios -----")
matriz = np.empty([3,5])
print(matriz)
print("  ")
print("-----llenar listas con rango -----")
# el primer parametro es el valor inicial 
# el segundo parametro es el valor final
# el tercer parametro es el incremento
matriz = np.arange(0,10,2) 
print(matriz)
print("  ")

print("-----llenar listas con rango NO. 2 ----")
lista = np.arange(0,10,1) 
print(lista)
print("  ")
print("Keyla Paola Nc = 0033")