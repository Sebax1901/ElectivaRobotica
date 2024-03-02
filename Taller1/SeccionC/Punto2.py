#Punto 2

import control
import matplotlib.pyplot as plot

wn = float(input("Ingresa la frecuencia natural del sistema: "))
factor = float(input("Ingresa el factor de amortiguamiento: "))
ganancia = float(input("Ingresa la ganancia estática: "))

numerador = ganancia * wn**2
coeficiente1 = 1
coeficiente2 = 2 * factor * wn
coeficiente3 = wn**2

denominador = []

denominador.append(coeficiente1)
denominador.append(coeficiente2)
denominador.append(coeficiente3)

funcionTrasnferencia = control.TransferFunction(numerador, denominador)

print("Función de transferencia:")
print(funcionTrasnferencia)

system_info = control.damp(funcionTrasnferencia)

if factor < 1:
    texto = "subamortiguado."
elif factor > 1:
    texto = "sobreamortiguado."
elif factor == 1:
    texto = "críticamente amortiguado."


t, y = control.step_response(funcionTrasnferencia)

plot.plot(t, y, color='purple')
plot.title(f'Respuesta del sistema {texto}\n')
plot.xlabel('Tiempo')
plot.ylabel('Respuesta')
plot.grid(True, linestyle='--', linewidth=0.5, color='gray')
plot.show()