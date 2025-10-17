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
