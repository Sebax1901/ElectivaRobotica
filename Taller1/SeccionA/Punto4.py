#4. Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de la temperatura.
temp = -200;

if temp >= 0:
    R0 = 100
    A =  3.9083 * 10**-3
    B = -5.775 * 10**-7
    resistencia = R0 * (1+ A*temp + B*(temp**2))

else:
    R0 = 100
    A =  3.9083 * 10**-3
    B = -5.775 * 10**-7
    C = -4.183 * 10**-12
    resistencia = R0 * (1 + A*temp + B*temp**2 + C*(temp-100) * temp**3)    

print(f"La resistencia de la PT100 a {temp}°C es de: {resistencia} omh")