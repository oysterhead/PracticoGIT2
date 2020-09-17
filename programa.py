def maximo(a: int, b: int) -> int:
    mayor = a
    if a < b:
        mayor = b
    else:
        pass
    return mayor

def largo_lista(lista: list) -> int:
    largo = 0
    for i in lista:
        largo += 1
    return largo

def sumatoria(lista: [int]) -> int:
    suma = 0
    for i in lista:
        suma += i
    return suma
