#Recibir de forma dinamica el nombre la edad ano de nacimiento correo y contrasena de un cliente


name = input("Introduce tu nombre: ")
birth_year = input("Introduce tu birth year: ")
email = input("Introduce tu email: ")
password = input("Introduce tu password: ")
asteriscos = len(password)

print(f'Nombre:{name} '
      f'Tendras {int(birth_year) - 2025} en el 2050'
      f'Email: {email} '
      f'{"*" * asteriscos}')

