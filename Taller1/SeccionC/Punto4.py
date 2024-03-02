import matplotlib.pyplot as ploit

# Obtener las coordenadas del usuario
x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))

# Crear la figura y los ejes 3D
figura = ploit.figure()
axes = figura.add_subplot(111, projection='3d')

# Dibujar el vector
axes.quiver(0, 0, 0, x, y, z, color='purple', arrow_length_ratio=0.1)

# Establecer los límites de los ejes
max_coord = max(x, y, z)
axes.set_xlim([0, max_coord])
axes.set_ylim([0, max_coord])
axes.set_zlim([0, max_coord])

# Etiquetar los ejes
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_zlabel('Z')

# Título de la gráfica
ploit.title('Sistema Coordenado 3D')

# Mostrar la gráfica
ploit.show()
