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

