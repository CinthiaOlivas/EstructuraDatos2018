###Programa que imprime los primeros 100 numeros naturales con recursividad

def numeros(n):                  ### Se crea un metodo que recibe como parametro un dato
	if n<101:                    ### El parametro es pasado por un condicional para definir un limite
	  print (n)                  ### Se imprime el valor almacenado en el parametro
	  return numeros(n+1)        ### La funcion se regresa a si misma incrementado en 1 
	    
numeros(1)                       ### Se manda el numero donde se va a inicializar
