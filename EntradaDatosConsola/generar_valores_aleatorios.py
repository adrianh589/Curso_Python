import random # forma 1 de importar
from random import randint # forma 2, importacion directa

# Valores aleatorios con la funcion randint

# Generar un numero aleatorio enter 1 y 10
numero = randint(1, 10)
print(f'Numero aleatorio entre 1 y 10: {numero}')

# Simular un dado de seis caras
dado = randint(1, 6)
print(f'Resultado de lanzar el dado: {dado}')

