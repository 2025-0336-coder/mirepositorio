#Escribe un programa que solicite un número al usuario y determine si es positivo, negativo o cero. 

print ("ingresa un numero y te dire si es positivo,negativo o cero")

num = float (input("ingrese un numero:"))

if num >0:
    print('tu numero es positivo')
    
elif num <0: 
    print('tu numero es negativo')

else:
    print('tu numero es 0')
