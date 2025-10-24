#Solicita la calificación de un estudiante (0-100) y determina si aprobó (mínimo 60) o reprobó. 

print ("ingresa tu calificacion asi sabras si estas aprovado o reprobado")

calificacion= float (input("ingresar tu calificacion:"))

if calificacion >60:
    print ("aprobaste")
    
else :
    print ("reprovaste")
