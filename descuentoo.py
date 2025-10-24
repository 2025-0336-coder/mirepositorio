# Programa que aplica descuentos según el precio del producto

precio = float(input("Introduce el precio del producto: "))

if precio < 50:
    descuento = 0
elif precio <= 100:
    descuento = precio * 0.05
else:
    descuento = precio * 0.10

precio_final = precio - descuento

print("Descuento aplicado: $", round(descuento, 2))
print("Precio final a pagar: $", round(precio_final, 2))