import numpy
import matplotlib.pyplot as plot

# Rango de temperaturas
temperatura = numpy.linspace(-200, 200, 1000)

# Calcula la resistencia correspondiente a cada temperatura
resistencia = []

for T in temperatura:
    if T >= 0:
        R0 = 100
        A =  3.9083 * 10**-3
        B = -5.775 * 10**-7
        resistenciaActual = R0 * (1+ A*T + B*(T**2))
    else:
        R0 = 100
        A =  3.9083 * 10**-3
        B = -5.775 * 10**-7
        C = -4.183 * 10**-12
        resistenciaActual = R0 * (1 + A*T + B*T**2 + C*(T-100) * T**3)
    
    resistencia.append(resistenciaActual)

# Gráfico
plot.figure(figsize=(10, 6))
plot.plot(temperatura, resistencia, color='purple')
plot.title('Comportamiento de un sensor PT100')
plot.xlabel('Temperatura (°C)')
plot.ylabel('Resistencia (Ω)')
plot.grid(True, linestyle='--', linewidth=0.5, color='gray')
plot.show()