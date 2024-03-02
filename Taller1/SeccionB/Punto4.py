# Punto No. 4 

print("\n**** Tipos de Robot y sus Articulaciones ****")

opcion = int(input("\nSelecciona el robot que deseas: \n1. Cilíndrico\n2. Cartesiano\n3. Esférico\n"))

# Robot Cilíndrico
if opcion == 1:
    print("Robot Cilíndrico")
    print('Robot de tipo RPP. Cuenta con dos articulaciones prismáticas y una articulación rotacional.')

# Robot Cartesiano
elif opcion == 2:
    print("Robot Cartesiano");
    print('Robot de tipo PPP. Cuenta con tres articulaciones prismáticas.')

# Robot Esférico
elif opcion == 3:
    print("Robot Esférico")
    print('Robot de tipo RRP. Cuenta con dos articulaciones rotacionales y una articulación prismática.')

# Opción Incorrecta
else:
    print('Selecciona una opción entre 1 y 3')
