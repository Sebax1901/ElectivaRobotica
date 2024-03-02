import numpy
import matplotlib.pyplot as plot

# Obtener los valores del usuario
voltaje = float(input("Ingrese el valor del voltaje (V): "))
resistencia = float(input("Ingrese el valor de la resistencia (Ω): "))
capacitancia = float(input("Ingrese el valor de la capacitancia (F): "))

tau = resistencia * capacitancia

# Crear el vector de tiempo
tiempo = numpy.arange(0, 5*tau, 0.001)

# Comportamiento de carga del circuito RC
carga = voltaje * (1 - numpy.exp(-tiempo/(resistencia*capacitancia)))
plot.figure()
plot.plot(tiempo, carga, color='purple')
plot.xlabel("Tiempo (Segundos)")
plot.ylabel("Tensión (Voltios)")
plot.title("Comportamiento de Carga circuito RC")
plot.grid(True, linestyle='--', linewidth=0.5, color='gray')

# Comportamiento de descarga del circuito RC
descarga = (voltaje) * (numpy.exp(-tiempo/(resistencia*capacitancia)))
plot.plot(tiempo, descarga, color='blue')
plot.xlabel("Tiempo (Segundos)")
plot.ylabel("Tensión (Voltios)")
plot.title("Comportamiento de Descarga circuito RC")
plot.grid(True, linestyle='--', linewidth=0.5, color='gray')

plot.show()
