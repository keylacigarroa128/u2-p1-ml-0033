# Keyla Paola NC = 0033
import numpy as np

calificaciones = np.array([60,70,90])
print(" --------- ej 1 imprimir califas ---------")
print(calificaciones) # Imprime listas de calificaciones
print(type(calificaciones)) # muestra el tipo de arreglo
print("  ")
print(" --------- ej 2 0 dimensiones de un array ---------")
calificaciones = np.array(60)
print(calificaciones)
print("Dimension : ", calificaciones.ndim)
print("  ")
print(" --------- ej 3 1 dimension de un array ---------")
calificaciones = np.array([60,70,90])
print(calificaciones)
print("Dimension : ", calificaciones.ndim)
print("  ")
print(" --------- ej 4 2 dimensiones de un array ---------")
calificaciones = np.array([
    [60,70,90],
    [50,80,98]
     ]) # un arreglo de dos dimensiones es como una tabla de excel
print(calificaciones)
print("Dimension : ", calificaciones.ndim)
print("  ")
print(" --------- ej 5 3 dimensiones de un array ---------")
calificaciones = np.array([
    [
     [60,70,90],
     [50,80,98]
    ],
    [
     [60,70,90],
     [50,80,98]
    ]
    ]) # un arreglo de tres dimensiones es como una tabla de excel
print(calificaciones)
print("Dimension : ", calificaciones.ndim)
print("keyla Paola NC = 0033")