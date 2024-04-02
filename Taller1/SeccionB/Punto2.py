#Punto No. 2

import random

print("\n**** Generador de números aleatorios ****\n")

cantidad = int(input("Ingresa la cantidad de números que deseas generar: "))
minimo = int(input("Ingresa el valor mínimo del rango en el que los quieres generar: "))
maximo = int(input("Ingresa el valor máximo del rango en el que los quieres generar: "))

numeros = random.sample(range(minimo, maximo + 1), cantidad)

print(f"Tus números son: {numeros}")