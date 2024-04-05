# Instrucciones: Crear un programa que pida al usuario su nombre, apellido paterno, 
# apellido materno, edad, peso y estatura, desplegarlos en pantalla junto con 
# su Índice de Masa Corporal (IMC). El programa no puede permitir que ningún dato quede vacío,
# además de asegurarse de que en los campos de edad, peso y estatura el usuario introduzca una cifra. 
# Todo esto antes de proceder con el cálculo del IMC siguiendo la fórmula:
# Peso / estatura2   -> Peso sobre estatura al cuadrado

print("¡Bienvenido a la Calculadora de Índice de Masa Corporal! ")

name = input("Ingresa tu nombre: \n")

# Aquí evitamos que el campo quede vacío
if not name:
    print("Por favor ingresa un nombre válido \n")
    name = input("Ingresa tu nombre: \n")

print("Hola, " + name)

paterno = input("Ingresa tu apellido paterno: \n")
if not paterno:
    print("Por favor ingresa un apellido válido \n")
    paterno = input("Ingresa tu apellido paterno: \n")

materno = input("Ingresa tu apellido materno: \n")
if not materno:
    print("Por favor ingresa un apellido válido \n")
    materno = input("Ingresa tu apellido materno: \n")

# Le preguntamos su edad:
age = int(input("Ingresa tu edad (ejemplo: 34): \n"))
if not age:
    print("Por favor ingresa un número válido \n")
    age = int(input("Ingresa tu edad (ejemplo: 34): \n"))

# Le preguntamos su peso:
mass = int(input("Ingresa tu peso (ejemplo: 80): \n"))
if not mass:
    print("Por favor ingresa un número válido \n")
    mass = int(input("Ingresa tu peso (ejemplo: 80): \n"))

# Le preguntamos su estatura:
height = float(input("Ingresa tu estatura en metros (ejemplo: 1.75): \n"))
if not height:
    print("Por favor ingresa un número válido \n")
    height = float(input("Ingresa tu estatura en metros (ejemplo: 1.75): \n"))

print("Aquí tienes tu información: \n ")

# Fórmula para calcular el IMC
imc = mass / height**2

# Imprimimos toda la info del usuario

print("Nombre: " + name)
print("Apellido Paterno: " + paterno)
print("Apellido Materno: " + materno)
print("Edad: " + str(age) + " años")
print("Peso: " + str(mass) + " kg")
print("Estatura: " + str(height) + " m")
print("Índice de Masa Corporal: " + str(imc))

