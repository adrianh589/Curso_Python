from random import randint

print('*** Sistema Generador de ID Único ***')

nombre= input('Cual es tu nombre?')
apellido= input('Cual es tu apellido?')
anio_nacimiento = input('Cual es tu anio nacimiento (YYYY)?')
digitos_finales = str(randint(1000, 9999))
id_generado = nombre.upper()[0:2] + apellido.upper()[0:2] + anio_nacimiento[2:4] + digitos_finales

print(f'''\nHola {nombre}
Tu nuevo número de identificación (ID) generado por el sistema es:
{id_generado}
Felicidades!
''')

