# Programa que determina el tipo de ángulo según su medida en grados

angulo = float(input("Introduce el valor del ángulo en grados: "))

if angulo < 90:
    print("El ángulo es agudo.")
elif angulo == 90:
    print("El ángulo es recto.")
elif angulo > 90 and angulo < 180:
    print("El ángulo es obtuso.")
elif angulo == 180:
    print("El ángulo es llano.")
else:
    print("El valor del ángulo no está en el rango válido (0°–180°).")