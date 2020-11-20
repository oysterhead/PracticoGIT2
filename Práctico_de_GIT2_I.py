class Arreglo:
    '''Esta clase tendrá como objetivo hacer un arreglo con un tope de 3 valores y luego, con distintas 
    funciones vamos a ir resolviendo lo que pide el ejercicio (Ejercicios pares)'''
    
    def __init__(self):
       self.valor=[]
    
    def incluir(self,value):
        self.valor.append(value)

    def mayor_de_tres(self):
        return max (self.valor)
    
def mayor_de_3():
    a = Arreglo()
    v1 = int(input("Ingrese 1er valor: "))
    a.incluir(v1)
    while len(a.valor)<3:
        v1 = int(input("otro valor: "))
        a.incluir(v1)

    print("El mayor de tres es: ",a.mayor_de_tres())

#Ejercicio Par nro 1

