# Programa que muestra un mensaje según la temperatura en grados Celsius

temperatura = float(input("Introduce la temperatura en grados Celsius: "))

if temperatura < 0:
    print("Hace mucho frío.")
elif temperatura <= 20:
    print("Clima fresco.")
elif temperatura <= 30:
    print("Clima agradable.")
else:
    print("Hace mucho calor.")
