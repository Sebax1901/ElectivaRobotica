import matplotlib.pyplot as ploit

# Obtener las coordenadas del usuario
x1 = 1
y1 = 1
x2 = 3
y2 = 3

# Crear la figura y los ejes 3D
figura = ploit.figure()
axes = figura.add_subplot(111)

# Dibujar el vector
axes.quiver(x1, y1, x2, y2, color='purple')

# Establecer los límites de los ejes
max_coord = max(x1, y1 , x2, y2)
axes.set_xlim([x1, x2])
axes.set_ylim([y1, y2])

# Etiquetar los ejes
axes.set_xlabel('X')
axes.set_ylabel('Y')

# Título de la gráfica
ploit.title('Sistema Coordenado 2D')

# Mostrar la gráfica
ploit.show()
