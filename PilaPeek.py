indice=0
class Pila:                     
    def __init__(self):             ###Se inicializa la clase 
        self.pila = []

    def push(self, item, num):      ###Metodo push que agrega elementos a la pila
        global indice
        if indice < num:            ###Condicion para evitar desbordamiento
            self.pila.append(item)          ###Se agregan los elementos a la pila 
            indice +=1                      ###Al agregar un valor a la pila incrementamos el indice 
        else:
            print("Pila llena")             ###En caso de llenarse la pila muestra el mensaje 

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

def Numeros(num):                       ###Metodo que contiene un ciclo for para agregar los valores de la pila en los indices
    for i in range(num):
            pil.push(int(input("Valor que desea ingresar:  ")),num)

num= int(input("Numero de indices a ingresar: "))         ###Se le pregunta al usuario el numero de indices que quiere agregar a la pila
pil=Pila()
Numeros(num)                                              ###Se manda a llamar el metodo Numeros y se le manda el parametro num que contiene el numero de indices

#print("\nElemento eliminado: ")
#print (pil.pop())

print("Ultimo elemento de la pila: ")               ###Muestra el ultimo elemento ingresado
print (pil.peek())

print ("Elementos de la pila: ")                        ###Muestra en pantalla todos los elementos de la pila y sus indices
print (pil.peekall())

i= pil.PeekIndex(int(input("Ingrese numero de indice a mostrar: ")))    ###Se ingresa el indice que se quiere mostrar
print(pil.PeekIndex(i))                                                 ###Se manda a llamar al metodo que mostrara ese indice