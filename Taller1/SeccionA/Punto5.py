#5 Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo) y un parámetro de salida (matriz).
import numpy as np

angulo = 45

def RotX(theta):
    Rx = [(1 , 0 , 0) , (0 , np.cos(theta) , -np.sin(theta)) , (0 , np.sin(theta) , np.cos(theta))]
    return Rx

def RotY(theta):
    Ry = [(np.cos(theta) , 0 , np.sin(theta)) , (0 , 1 , 0) , (-np.sin(theta) , 0 , np.cos(theta))]
    return Ry

def RotZ(theta):
    Rz = [(np.cos(theta) , -np.sin(theta) , 0) , (np.sin(theta) , np.cos(theta) , 0) , (0 , 0 , 1)]
    return Rz

rotacion_matrix_x = np.array(RotX(angulo))
rotacion_matrix_y = np.array(RotY(angulo))
rotacion_matrix_z = np.array(RotZ(angulo))
print(f"Matriz de rotación en el eje X: \n {rotacion_matrix_x} ")
print(f"Matriz de rotación en el eje y: \n {rotacion_matrix_y} ")
print(f"Matriz de rotación en el eje z: \n {rotacion_matrix_z} ")