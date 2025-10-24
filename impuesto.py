#Pide al usuario su salario mensual y aplica los siguientes impuestos: ○ Menos de 10,000: 0% 
# Entre 10,000 y 30,000: 10% ○ Más de 30,000: 20% 

print ("aplicacion de impuesto")

impuesto= float (input("ingrese el salario") )
                 
                 
if impuesto <10000:
    print ("se le aplicara un 0% de impuesto")
    
elif impuesto >30000:
    print ("se le aplicara un impuesto del 20%")
    
else: 
    print ("se le aplicara un descuento de un 10%")
