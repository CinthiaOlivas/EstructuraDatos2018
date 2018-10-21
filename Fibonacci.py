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

ImprimirR()															###Se imprimen los resultados

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

ImprimirIterativo()												###Se imprimen los resultados






