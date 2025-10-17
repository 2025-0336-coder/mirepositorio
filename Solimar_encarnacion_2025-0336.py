#Crea un programa que permita realizar diversas operaciones 
# con dos números que se introducen por el teclado. Multiplicado,
# división, suma, resta, módulo o resto, raiz cuadrada y potencia


import math

print("=== CALCULADORA DE NuMEROS ===")

# Solicitar los números
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))

# Mostrar el menu de opciones
print("""
Elige la operacion que deseas realizar:
1. Suma
2. Resta
3. Multiplicacion
4. División
5. Módulo o resto
6. Raíz cuadrada
7. Potencia
""")

opcion = input("Opcion: ")

# realizar funcion escojida
if opcion == "1":
    print(f"La suma es: {num1 + num2}")
elif opcion == "2":
    print(f"La resta es: {num1 - num2}")
elif opcion == "3":
    print(f"La multiplicación es: {num1 * num2}")
elif opcion == "4":
    if num2 != 0:
        print(f"La división es: {num1 / num2}")
    else:
        print("Error: no se puede dividir entre cero.")
elif opcion == "5":
    if num2 != 0:
        print(f"El modulo o resto es: {int(num1) % int(num2)}")
    else:
        print("Error: no se puede calcular el módulo con divisor cero.")
elif opcion == "6":
    if num1 >= 0:
        print(f"La raiz cuadrada del primer número es: {math.sqrt(num1)}")
    else:
        print("Error: no se puede sacar raiz cuadrada de un numero negativo.")
    if num2 >= 0:
        print(f"La raíz cuadrada del segundo numero es: {math.sqrt(num2)}")
    else:
        print("Error: no se puede sacar raiz cuadrada de un numero negativo.")
elif opcion == "7":
    print(f"{num1} elevado a {num2} es: {math.pow(num1, num2)}")
else:
    print("Opción no válida.")
    



#Validación de contraseña: Crea un programa que permita validar una contraseña 
# para ingresar a un área protegida. Pide el nombre del usuario y una contraseña,
# si es válida, muestra el mensaje: Bienvenido + NombreUsuario.


# Contraseña predefinida
CONTRASENA_CORRECTA = "12345"

print("=== ACCESO AL ÁREA PROTEGIDA ===")

# Pedir datos al usuario
nombre = input("Introduce tu nombre de usuario: ")
contrasena = input("Introduce tu contraseña: ")

# Verificar si la contraseña es correcta
if contrasena == CONTRASENA_CORRECTA:
    print(f"Bienvenido {nombre}")
else:
    print("Contraseña incorrecta. Acceso denegado.")



#El mayor de 3 números: Programa para validar 
# cuál es el número mayor entre 3 números.

print("=== DETERMINAR EL MAYOR DE TRES NÚMEROS ===")

# Pedir los tres números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Determinar cuál es el mayor
if num1 > num2 and num1 > num3:
    print(f"El número mayor es: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"El número mayor es: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"El número mayor es: {num3}")
else:
    print("Hay números iguales.")


#Tabla de multiplicar hasta N: Pide un número
# por teclado y luego pide el límite de la tabla.
# Crea la tabla de multiplicar desde 1 hasta N para el número en cuestión.


print("=== TABLA DE MULTIPLICAR ===")

# Pedir el número y el límite
numero = int(input("Introduce el numero que deseas multiplicar: "))
limite = int(input("¿Hasta que numero deseas la tabla?: "))

print(f"\nTabla del {numero} hasta {limite}\n")

# Generar la tabla
for i in range(1, limite + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")



#Calculadora de Temperatura: Crea un programa que pida un valor en grados Farenheit 
# y lo convierta a Celsius, y otra opción que pida Celsius y lo convierta a Fahrenheit

print("=== CALCULADORA DE TEMPERATURA ===")
print("1. Convertir de Fahrenheit a Celsius")
print("2. Convertir de Celsius a Fahrenheit")

opcion = input("Elige una opción (1 o 2): ")

if opcion == "1":
    fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F equivalen a {celsius:.2f}°C")

elif opcion == "2":
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

else:
    print("Opción no válida. Debes elegir 1 o 2.")
