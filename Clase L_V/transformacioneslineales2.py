#Problema 2: Reducción de Gauss
import numpy as np

# Definir la matriz de coeficientes y el vector de resultados
A = np.array([[4, 2]])  # Coeficientes de la ecuación 4x + 2y = 100
b = np.array([100])  # Total de horas disponibles

# Solución para cumplir las restricciones mínimas
min_x = 10  # Mínimo de unidades del modelo A
min_y = 5   # Mínimo de unidades del modelo B

# Establecer límites mínimos
if min_x * 4 + min_y * 2 > 100:
    print("No es posible cumplir con las restricciones mínimas de producción dado el número de horas disponible.")
else:
    # Resolver el sistema para el caso exacto de usar todas las horas disponibles
    x = min_x
    y = (100 - 4 * x) / 2  # Resolver para y
    if y >= min_y:
        print(f"La empresa puede producir {x} unidades del modelo A y {int(y)} unidades del modelo B.")
    else:
        print("No es posible satisfacer las restricciones dentro del límite de horas.")
