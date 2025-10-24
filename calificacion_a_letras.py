# Programa que convierte una calificación numérica (0-100) en una letra

nota = float(input("Introduce la calificación (0-100): "))

if nota < 0 or nota > 100:
    print("Calificación no válida. Debe estar entre 0 y 100.")
elif nota >= 90:
    print("Calificación: A")
elif nota >= 80:
    print("Calificación: B")
elif nota >= 70:
    print("Calificación: C")
elif nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")