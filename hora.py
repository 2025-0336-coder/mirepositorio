# Programa que determina el momento del día según la hora

hora = int(input("Introduce la hora (0-23): "))

if hora < 0 or hora > 23:
    print("Hora no válida. Debe estar entre 0 y 23.")
elif 6 <= hora <= 11:
    print("Mañana.")
elif 12 <= hora <= 17:
    print("Tarde.")
elif 18 <= hora <= 23:
    print("Noche.")
else:
    print("Madrugada.")
