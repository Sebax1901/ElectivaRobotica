#Punto No. 3

import math

print("\n**** Calculadora de volúmenes ****\n")
prompt = "Selecciona una opción para calcular: \n\n1. Prisma\n2. Pirámide\n3. Cono\n4. Truncado\n5. Cilindro\n"
opcion = int(input(prompt))

#Volumen de un prisma
if opcion == 1:
    largo = float(input('Indique el largo (cm): '))
    ancho = float(input('Indique el ancho (cm): '))
    altura = float(input('Indique la altura (cm): '))
    volumen = largo * ancho * altura
    print(f"\nEl volumen del prisma es: {volumen} cm^3")

#Volumen de una piramide
elif opcion == 2:
    base = float(input('Indique la base (cm): '))
    altura = float(input('Indique la altura (cm): '))
    volumen = (1/3) * base**2 * altura
    print(f"\nEl volumen del prisma es: {volumen} cm^3")

#Volumen de un cono
    
elif opcion == 3:
    radio = float(input('Indique el radio (cm): '))
    altura = float(input('Indique la altura (cm): '))
    volumen = (1/3) * math.pi * altura * radio**2
    print(f"\nEl volumen del cono es: {volumen} cm^3")

#volumen de un truncado
    
elif opcion == 4:
    radioMenor = float(input('Indique el radio menor (cm): '))
    radioMayor = float(input('Indique el radio Mayor (cm): '))
    altura = float(input('Indique la altura (cm): '))
    volumen = (1/3) * math.pi * altura * (radioMayor**2 + radioMenor**2 + (radioMayor * radioMenor))
    print(f"\nEl volumen del truncado es: {volumen} cm^3")

elif opcion == 5:
    radio = float(input('Indique el radio (cm): '))
    altura = float(input('Indique la altura (cm): '))
    volumen = math.pi * radio**2 * altura
    print(f"\nEl volumen del cilindro es: {volumen} cm^3")

else:
    print("[!] Opción no válida... Saliendo del programa")