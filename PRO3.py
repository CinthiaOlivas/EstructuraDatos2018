#Programa que lleve control de versiones de la actual a la antigua
indice = 0
class Stack:            #Se inicializa la pila en ceros
    def __init__(self):
        self.stack = []
   
    def push(self, item, numVer):     #Metodo para agregar valores de las versiones                  
         global indice
         if indice < numVer:            #Se crea la condicion para agregar los datos
            self.stack.append(item)
            indice += 1
         else:
            print("OverflowError- Pila llena")   #En caso de meter mas valores saldra este mensaje
        
    def peek(self, numVer):                     #Creamos metodo que mostrara las versiones                                                 
        for x in range(numVer-1, -1, -1):
            print ("Version "+str (x+1)+":" +str(self.stack[x]))
                   
pila = Stack()
numV = int(input("Numero de versiones: "))
for x in range(0, numV):        #Definimos con un ciclo for cuantos datos se van a ingresar
    pila.push(input("Version " + str(x+1) + ":"),numV)

print("\n\tListado de versiones tome en cuenta que va desde el actual al antiguo\n")    #Se imprime la lista
pila.peek(numV)