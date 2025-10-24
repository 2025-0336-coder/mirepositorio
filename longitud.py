# Programa que determina si tres longitudes pueden formar un triángulo

a = float(input("Introduce la primera longitud: "))
b = float(input("Introduce la segunda longitud: "))
c = float(input("Introduce la tercera longitud: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Las longitudes pueden formar un triángulo.")
else:
    print("Las longitudes NO pueden formar un triángulo.")