# Inmutabilidad en cadenas

cadena1 = 'Hola mundo'
#cadena1[0] = 't'

# It generates error because is not possible change any character directly
#print(cadena1)

cadena2 = cadena1
# You must change all the variable
cadena1 = "I have been changed"
print(cadena1)
print(cadena2)