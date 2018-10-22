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

def Numeros(num):                       ###Metodo que contiene un ciclo for para agregar los valores de la pila en los indices
    for i in range(num):
            pil.push(int(input("Valor que desea ingresar:  ")),num)

num= int(input("Numero de indices a ingresar: "))         ###Se le pregunta al usuario el numero de indices que quiere agregar a la pila
pil=Pila()
Numeros(num)                                              ###Se manda a llamar el metodo Numeros y se le manda el parametro num que contiene el numero de indices

