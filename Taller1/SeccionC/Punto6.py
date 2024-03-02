import matplotlib.pyplot as plt
import matplotlib.patches as patches

def dibujar_semi_circulo(ax, centro_x, centro_y, radio, angulo_inicio, angulo_fin):
    """
    Dibuja un semicírculo orientado con un ángulo específico.

    ax: el eje donde se dibujará el semicírculo.
    centro_x, centro_y: las coordenadas del centro del semicírculo.
    radio: el radio del semicírculo.
    angulo_inicio, angulo_fin: ángulos que definen la apertura del semicírculo.
    """
    arc = patches.Arc((centro_x, centro_y), radio*2, radio*2,
                      angle=0, theta1=angulo_inicio, theta2=angulo_fin,
                      color="black", linewidth=2)
    ax.add_patch(arc)

def dibujar_letra_B(ax, offset):
    # Dibuja la línea vertical de la "B"
    ax.plot([-0.5+offset, -0.5+offset], [0, -3], color="black", linewidth=2)
    
    # Dibuja los semicírculos de la "B" orientados hacia la derecha
    dibujar_semi_circulo(ax, -0.5+offset, -0.75, 0.75, 270, 90)
    dibujar_semi_circulo(ax, -0.5+offset, -2.25, 0.75, 270, 90)

# Configuración del gráfico
fig, ax = plt.subplots()
ax.set_xlim(-3, 1)
ax.set_ylim(-4, 1)
ax.axis('off')

# Dibuja la letra "B"
dibujar_letra_B(ax, 0)

plt.show()
