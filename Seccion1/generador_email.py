nombre = 'Adrian Yesith Hoyos Marquez'
empresa = '          Global Mentoring              '
dominio = '.com.co'
dominio_email = nombre.replace(' ', '.').lower().strip()
empresa_normalizada = empresa.replace(' ', '').lower().strip()
dominio_normalizado = f'@{empresa_normalizada}{dominio}'.strip()
email_final = f'{dominio_email}{dominio_normalizado}'

print('*** Generador de email ***')
print('Nombre usuario:', nombre)
print('Nombre usuario normalizado:', dominio_email)

print()

print('Nombre empresa:', empresa)
print('Extension del dominmio', dominio)
print('Dominio de email normalizado:', dominio_normalizado)

print()

print('Email final generado:', email_final)