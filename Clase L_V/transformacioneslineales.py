#Problema 1: Regla de Cramer

import numpy as np

def cramer_solve(A, B):
    # Calculamos el determinante de la matriz A
    det_A = np.linalg.det(A)
    
    if det_A == 0:
        return "El sistema no tiene solución única."
    
    # Matrices con sustituciones para aplicar la regla de Cramer
    A_x = np.copy(A)
    A_x[:, 0] = B
    A_y = np.copy(A)
    A_y[:, 1] = B
    
    # Determinantes de las matrices modificadas
    det_A_x = np.linalg.det(A_x)
    det_A_y = np.linalg.det(A_y)
    
    # Soluciones para x y y
    x = det_A_x / det_A
    y = det_A_y / det_A
    
    return x, y

# Datos del problema
A = np.array([[120, 80], [1, 1]])
B = np.array([1200, 10])

hectareas_maiz, hectareas_soja = cramer_solve(A, B)
print(f"Hectáreas de maíz: {hectareas_maiz}")
print(f"Hectáreas de soja: {hectareas_soja}")
