##Problema 1- Resultado de sumar de 1-9
#Cinthia Guadalupe Olivas Calderon

def Suma(n):             		#Definimos el metodo donde se haran las operaciones      
	if n==1:                    #Como se le manda directamente el parametro de 9 se va al else                 
	  return 1         
	else:
	    return Suma(n-1)+n 	#Toma el parametro y realiza la operacion 
print ("La suma 1+2+3+4+5+6+7+8+9 da un igual de: ")
print(Suma(9))                       
