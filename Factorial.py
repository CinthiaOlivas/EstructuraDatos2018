###Practica factorial recursivo y con iteraciones

def FactorialIterativo(n):					### Se define metodo que va a recibir el dato    
	aux = 1									### Declaramos aux como variable para almacenar los datos 
	for i in range (1,n):					### Ciclo for que comienza en 1  
		aux*= (i+1)					
	return aux

def Datos():								### Se creaa metodo para pedir datos al usuario y se imprime el resultado
	dato = int(input("Ingrese numero que desea el factorial iterativo \n"))
	x = FactorialIterativo(dato)
	
	return (x)

print(Datos())								### Se imprime resultado		 

def FactorialRecursivo(n):					### Se define el metodo de modo recursivo que va a recibir el dato
	if n ==1:							    ### Si el factorial es igual a 1 regresa el mismo valor 
		return n
	else:
		 return n*FactorialRecursivo(n-1)   ### El dato ingresado se multiplica por la funcion que se llama a si misma con el parametro restandole 1 hasta que este sea igual a 1 

def Dato():									### Se crea metodo para pedir datos al usuario y se imprime el resultado
	datos = int(input("Ingrese numero que desea el factorial recursivo \n"))
	z = FactorialIterativo(datos)
	
	return (z)

print (Dato())								### Se imprime el resultado
