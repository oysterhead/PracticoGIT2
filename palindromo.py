class Pila:
    def __init__(self):
        self.items = []

    def __eq__(self, otra):
        return self.items == otra.items

    def estaVacia(self):
        return self.items == []

    def incluir(self, item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()
    
    def inspeccionar(self):
        return self.items[len(self.items)-1]

    def tamano(self):
        return len(self.items)

    #Ejercicio 2

    def dar_vuelta_pila(self):
        aux = []
        while not self.estaVacia():
            aux.append(self.extraer())
        self.items = aux

    def imprimir_pila(self):
        for i in self.items:
            print(i)
    
    def vaciar_pila(self):
        while not self.estaVacia():
            self.extraer()

    '''
    def dar_vuelta_pila(self):
        self.items = self.items[::-1]

    def imprimir_pila(self):
        print(self.items)

    def vaciar_pila(self):
        self.items = []
    '''


def es_capicua(palabra: str) -> bool:
    pila = Pila()
    pila2 = Pila()
    for letra in palabra:
        pila.incluir(letra.lower())
        pila2.incluir(letra.lower())
    pila2.dar_vuelta_pila()
    return pila == pila2

assert es_capicua('ahora') == False
assert es_capicua('camion') == False
assert es_capicua('Neuquen') == True
assert es_capicua('Ala') == True
