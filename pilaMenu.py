indice = 0
class Pila:
    def __init__(self):         ###Inicializamos la clase Pila
        self.pila = []

    def push(self,item, num):   ###Metodo push que agrega los elementos a la pila
        global indice           
        if indice < num:        ###Condicion para evitar el desbordamiento
            self.pila.append(item)   ###Se agregan los elementos a la pila       
            indice += 1              ###Al agregar un valor a la pila incrementamos el indice
        else:
            print("Pila llena")     ###En caso de llenarse la pila muestra este mensaje

    def  pop(self):                     ###Metodo para eliminar el ultimo elemento ingresado
        global indice                  
        if indice > 0:                  ###Condicion para que se elimine el elemento
            indice = -1
            return self.pila.pop()      ###Regresa el valor eliminado
       
    def peek(self):                     ###Metodo que imprime el primer valor ingresado de la pila
        return self.pila[0]

    def  peekall(self):                 ###Funcion que imprime toda la pila
        print("")
        self.pila.reverse()                       ### Reverse se utiliza para que al mostrar todo lo acomode conforme fue entrando a la pila
        for i,j in enumerate(self.pila):          ### Ciclo que recorre toda la pila ordenando con su respectivo indice y dato
            print('\t\t\t'+str([i,j]))            ### Imprime los datos que se encuentran en la pila

    def PeekIndex(self,dato):                   ###Muestra el dato que el usuario desee, pide la posicion de en el indice y lo muestra
        for i in self.pila:
            if i == dato:
                return i

        
num= int(input("Numero de indices a ingresar:\n "))         ###Se pide el numero de indices
pil= Pila()

opc = 0
while (opc!=6):                     ###Menu que muestra las diferentes opciones, en cada una de las opciones muestra lo que el usuario pidio
    print ("\t\nQue desea hacer\n 1.- Agregar elementos (push)\n 2.- ELiminar elemento (pop)\n 3.-Mostrar ultimo elemento (peek)\n 4.- Mostrar todos los elementos (peekall)\n 5.- Buscar un elemento (PeekIndex)\n 6.- Salir\n")
    opc = int(input("Ingresa opcion: "))

    if opc== 1:
        for i in range(num):                                             
            pil.push(int(input("Valor que desea ingresar:  ")),num)      

    elif opc==2:
        print("\nElemento eliminado: ")
        print (pil.pop())
        
    elif opc==3:
        print("Ultimo elemento de la pila: ")
        print (pil.peek())
       
    elif opc ==4:
        print ("Elementos de la pila: ")
        print (pil.peekall())
       
    elif opc ==5:
        pil.PeekIndex(int(input("Ingrese numero de indice a mostrar: ")))
        print(pil.PeekIndex(i))
        
    elif opc==6:
        exit()
    else:
        print("Opcion invalida")
        