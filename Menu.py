def numeros(n):                  ### Se crea un metodo que recibe como parametro un dato
	if n<101:                    ### El parametro es pasado por un condicional para definir un limite
  		print (n)                  ### Se imprime el valor almacenado en el parametro
  		return numeros(n+1)        ### La funcion se regresa a si misma incrementado en 1 
########################################################################################################################		                      
def FactorialIterativo(n):					### Se define metodo que va a recibir el dato    
	aux = 1									### Declaramos aux como variable para almacenar los datos 
	for i in range (1,n):					### Ciclo for que comienza en 1  
		aux*= (i+1)					
	return aux

def Datos():								### Se creaa metodo para pedir datos al usuario y se imprime el resultado
	dato = int(input("Ingrese numero que desea el factorial iterativo \n"))
	x = FactorialIterativo(dato)
	
	return (x)


def FactorialRecursivo(n):					### Se define el metodo de modo recursivo que va a recibir el dato
	if n ==1:							    ### Si el factorial es igual a 1 regresa el mismo valor 
		return n
	else:
		 return n*FactorialRecursivo(n-1)   ### El dato ingresado se multiplica por la funcion que se llama a si misma con el parametro restandole 1 hasta que este sea igual a 1 

def Dato():									### Se crea metodo para pedir datos al usuario y se imprime el resultado
	datos = int(input("Ingrese numero que desea el factorial recursivo \n"))
	z = FactorialIterativo(datos)
	return (z)
##############################################################################################################################
def FibonacciRecursivo(n):			###Se define el metodo donde se hara el procedimiento recursivo
	if n<2:							###Creamos la condicion para que al introducir el numero si es menor a 2 no se puede hacer la serie fibonacci
		return n
	else:
		return FibonacciRecursivo(n-1)+FibonacciRecursivo(n-2)		###Teniendo el numero se manda a la serie donde se hace la operacion
																	###La operacion consiste en tener el numero que seran las veces que se realizara la operacion, comenzando con el cero y sumandole uno y a ese sumarle el anterior 
 
def ImprimirR():													##Metodo que pide el numero y con un ciclo for hace que comience desde el cero y manda a llamar al metodo recursivo
	x= int(input("Ingrese numero para metodo recursivo: \n"))

	for i in range(x): 
		print(FibonacciRecursivo(i))

def FibonacciIterativo(n):			###Se define el metodo donde se hara el procedimiento recursivo
	x=0								###Se declaran las tres variables 
	y=1								###A las variables Y y Z se inicializan en 1 para poder hacer las operaciones
	z=1
	for i in range (0,n):			###Hacemos un ciclo for para que comience en cero y haga las operaciones hasta el numero que el usuario da
		x=y 						###se iguala la variable X con Y que dara como resultado que X vale uno
		y=z 						###Ahora Y va a valer lo que vale Z
		z= x+y 						###Se hace la suma de X y Y
	return x 						###El metodo regresa el valor de X hasta completar el ciclo
	
def ImprimirIterativo():							###Metodo que pide el numero y con un ciclo for hace que comience la serie y manda a llamar al metodo para realizar las operaciones de la serie
	m= int(input("Ingrese numero para metodo iterativo: \n"))			###Se pide al usuario introducir el numero que seran las veces que se realizaran las operaciones

	for i in range(m):
		print(FibonacciIterativo(i))

###############################################################################################################################################

def Menu(): 						#Creamos un menu para que el usuario decida que opcion quiere, luego ingresa la opcion y conforme al programa muestra diferentes operaciones				
	print ("Que desea hacer\n 1.- Numeros 1-100\n 2.-Factorial\n 3.- Fibonacci\n 4.- Salir")
	opc = int(input("Ingresa opcion: "))
	if opc== 1:
		numeros(1)
		Menu()
	elif opc==2:
		print(Datos())
		print (Dato())
		Menu()
	elif opc==3:
		ImprimirR()
		ImprimirIterativo()
		Menu()
	elif opc==4:
		exit()
	else:
		print("Opcion invalida")

Menu() 								###Se imprime el menu
