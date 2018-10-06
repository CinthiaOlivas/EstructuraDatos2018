## Hacer un programa que simule la fila de clientes de una tienda de super mercado,
index = 0
class Tiendita():       #Se crea modulo que no recibe parametros 

    def __init__(self):                  #Se inicializa la cola
        self.cola = [0,0,0,0,0]          # Se declara la cola y el total de valores que puede tener
    
    def push(self,dato):                 #Este metodo sirve para ingresar los valores dados por el usuario
        global index
        self.cola[index] = dato
        index+=1
    
    def peek(self):                     #Este metodo sirve para quitar elementos de la cola cuando ya esta llena 
        global index
        if index!=0:
            print(str("\n\tCliente con el numero: [" + str(self.cola[0])) + "] Hizo su pago y dejo un lugar libre")
            for i in range(0,4):
                self.cola[i] = self.cola[i+1]     
            self.cola[4]=0
            index -=1
        else:   
            print("\nYa puede ingresar a la cola")

def menuTiendita():             #Se crea un menu para que el usuario pueda escojer la opcion deseada 
    cola = Tiendita()
    while True:                  #El ciclo se hace hasta que el usuario desee salir del programa
        print("\n\tTiendita 'BARBIE'\n")
        print("Que desea:")
        print("1.-Entrar a la cola\n2.-Atender cliente\n3.-Cerrar caja\n")     #Se crean las opciones para el menu
        dato = int(input("Ingrese su opcion:  "))
        if dato==1:                                              #Se hace la comparacion con el dato ingresado
            if index <= 4:
                num = int(input("\n\tIngrese numero de cliente: ")) #Se le pide al usuario ingresar valor y se manda a llamar al metodo push para almacenarlo
                cola.push(num)
            else:
                print("\n\tCOLA LLENA. POR FAVOR ESPERE A QUE SEAN ATENDIDOS PARA PODER INGRESAR")
        elif dato==2:                               #Se hace la comparacion con el dato ingresado
            cola.peek()                             #Como la opcion fue la 2 se manda a llamar al metodo peek para sacar un elemento de la cola
            
        elif dato==3:                               #Se hace la comparacion con el dato ingresado
            exit()                                  #Se termina el ciclo while
        else:
            print("\n\tOpcion invalida")
    
menuTiendita()                  #Se manda a llamar a menu