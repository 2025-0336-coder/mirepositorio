#El mayor de 3 números: Programa para validar 
# cuál es el número mayor entre 3 números.


print("=== TABLA DE MULTIPLICAR ===")

# Pedir el número y el límite
numero = int(input("Introduce el numero que deseas multiplicar: "))
limite = int(input("¿Hasta que numero deseas la tabla?: "))

print(f"\nTabla del {numero} hasta {limite}\n")

# Generar la tabla
for i in range(1, limite + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
