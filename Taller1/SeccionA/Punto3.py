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

