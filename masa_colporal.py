# Programa que calcula el Índice de Masa Corporal (IMC) y lo clasifica

peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / (altura ** 2)

print("Tu IMC es:", round(imc, 2))

if imc < 18.5:
    print("Clasificación: Bajo peso.")
elif imc < 25:
    print("Clasificación: Normal.")
elif imc < 30:
    print("Clasificación: Sobrepeso.")
else:
    print("Clasificación: Obesidad.")
