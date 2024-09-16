print('*** Sistema de Empleados ***')
nombre_empleado = input('Digite el nombre del empleado: ')
edad_empleado = int(input('Digite el edad del empleado: '))
salario_empleado = float(input('Digite el salario del empleado: '))
es_jefe = input('Es jefe de departamento?: ').lower()
es_jefe_boolean = es_jefe == 'si' or es_jefe == 's'

print(f'Nombre del empleado: {nombre_empleado}')
print(f'Edad del empleado: {edad_empleado}')
print(f'Salario del empleado: {salario_empleado:.1f}')
print(f'Es jefe de departamento (Si/No)? : {es_jefe_boolean}')
