class Lista:
    '''Vamos a generar una lista para poder cargar items (numeros) que se van a multiplicar'''
    
    def __init__(self):
        #Constructor de la clase.
        self.items = []
    
    def incluir(self, item):
        #Metodo para agregar elementos a la pila. Agrega al ultimo de la pila.
        self.items.append(item)
    
    def multiplicar(self):
        producto = 1
        for i in self.items:
            producto = producto * i
        return producto


l = Lista ()

item = int(input("Ingrese la cantidad de numero que quiera multiplicar (con 0 termina): "))
while item != 0:
    l.incluir(item)
    item = int(input("Siguiente numero (con 0 sale): "))

valor = l.multiplicar()

print("El PRODUCTO de la lista es: ", valor)

#Ejercicio Par Nro 3.-