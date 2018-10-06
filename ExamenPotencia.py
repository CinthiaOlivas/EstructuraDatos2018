#Problema 2. Programa que regresa resultado de 2 a la n potencia
#Cinthia Guadalupe Olivas Calderon

def Num(n):   			#Al metodo Num se le manda un parametro para que realice las operaciones			
	if n==0:                                     
	  return 1         
	else:
	    return 2*Num(n -1)	#Al tener el valor dado por el usuario eleva 2 a la potencia dada

x = int(input("Ingrese grado de la potencia para el numero 2:-- "))	#Se pide al usuario el valor de la potencia
print("El resultado es: ")									
print(Num(x))  			#Se imprimen los resultados
