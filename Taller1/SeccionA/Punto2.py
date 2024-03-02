#2. Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos matrices previamente inicializadas.
import numpy as np
m1 = ([(1,2,3),(4,5,6),(9,8,7)])
m2 = ([(6,7,8),(9,1,2),(3,5,7)])
ms1 = np.add(m1, m2) 
mr2 = np.subtract(m1, m2)
mpp = np.multiply(m1, m2)
mpx = np.cross(m1, m2)
md1 = np.divide(m1, m2)
print(f"Datos del vector1: \n{m1}")
print(f"Datos del vector2: \n{m2}")
print(f"Resultado de la suma de los vertores: \n{ms1}")
print(f"Resultado de la resta de los vertores: \n{mr2}")
print(f"Resultado del producto punto de los vertores: \n{mpp}")
print(f"Resultado del producto cruz de los vertores: \n{mpx}")
print(f"Resultado de la division de los vertores: \n{md1}")

# 3. Realice un programa que convierta coordenadas rectangulares a cilíndricas y esféricas, para lo cual deben consultar sobre el uso de funciones trigonométricas en Python.
import math
x=4
y=7
z=3
#coordenadas cilindricas Radio, theta, Z
r_c = round(math.sqrt(x**2+y**2),2)
ang_c = math.atan2(y,x)
grad_c= round(ang_c*180/math.pi,2)
z_c=z
#coordenadas esfericas Radio, theta, Phi
r_e= round(math.sqrt(x**2+y**2+z**2),2)
ang_e=math.atan2(y,x)
grad_e=round(ang_e*180/math.pi,2)
ang2_e=math.acos(z/r_e)
grad2_e=round(ang2_e*180/math.pi,2)

print(f"Para las coordenadas cilindricas el radio es: {r_c}, el angulo theta es: {grad_c} y Z es {z_c} ")
print(f"Para las coordenadas esfericas el radio es: {r_e}, el angulo theta es: {grad_e} y el angulo phi es {grad2_e} ")

#4. Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de la temperatura.
temp=30;
resistencia = round(0.3535*temp + 100.76,2) 
print(f"La resistencia de la PT100 a {temp}°C es de: {resistencia} omh")

#5 Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo) y un parámetro de salida (matriz).
import numpy as np
angulo = 0
cos_theta = np.cos(angulo)
sin_theta = np.sin(angulo)
rotacion_matrix_x = np.array([(1, 0, 0),(0, cos_theta, -sin_theta),(0, sin_theta, cos_theta)])
rotacion_matrix_y = np.array([(cos_theta, 0, sin_theta),(0, 1, 0),(-sin_theta, 0, cos_theta)])
rotacion_matrix_z = np.array([(cos_theta, -sin_theta, 0),(sin_theta, cos_theta, 0),(0, 0, 1)])
print(f"Matriz de rotación en el eje X: \n {rotacion_matrix_x} ")
print(f"Matriz de rotación en el eje y: \n {rotacion_matrix_y} ")
print(f"Matriz de rotación en el eje z: \n {rotacion_matrix_z} ")

#6. Realice un programa que calcule la fuerza de avance y retroceso de un cilindro neumático de doble efecto. Debe establecer previamente los valores de presión, así como las dimensiones físicas del cilindro para realizar el cálculo.
import math
P=6; #fuerza de vance
D_emb=int(8); # Diametro del embolo
D_vast=float(2.5); # Diametro del vastago

S_avance = (math.pi*((D_emb)**2))/4 #seccion de avance
F_avance = round(P*S_avance,2) #Fuerza de avance
S_retroceso = math.pi*((D_emb)**2-(D_vast)**2)/4 #Seccion de retroceso
F_retroceso = round(P*S_retroceso,2) #fuerza de retroceso

print(f"La fuerza de avance es de {F_avance}N y la fuerza de retroceso es de {F_retroceso}N ")