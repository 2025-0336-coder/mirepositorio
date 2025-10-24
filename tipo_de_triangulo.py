# Programa que determina si un triángulo es equilátero, isósceles o escaleno

a = float(input("Introduce la primera longitud: "))
b = float(input("Introduce la segunda longitud: "))
c = float(input("Introduce la tercera longitud: "))

# Primero verificamos si se puede formar un triángulo
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b and b == c:
        print("El triángulo es equilátero.")
    elif a == b or a == c or b == c:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")
else:
    print("Las longitudes NO pueden formar un triángulo.")