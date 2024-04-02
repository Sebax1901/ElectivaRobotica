#1. Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos vectores previamente inicializados.
import numpy as np

nums1 = np.array([9,8,7])
nums2 = np.array([3,4,5])

#Operaciones
suma = nums1+nums2
resta = nums1-nums2
producto_p = nums1 * nums2
producto_c = np.cross(nums1, nums2)

print(f"Datos del vector1: \n{nums1}")
print(f"Datos del vector2: \n{nums2}")
print(f"Resultado de la suma de los vectores: \n{suma}")
print(f"Resultado de restar el vertor 2 del vector 1: \n{resta}")
print(f"Resultado de producto punto de los vectores: \n{producto_p}")
print(f"Resultado de producto cruz de los vectores: \n{producto_c}")