from time import sleep
from os import system
from programa import maximo
from programa import largo_lista
from programa import sumatoria
from programa import interseccion_listas
from Práctico_de_GIT2_I import mayor_de_3
from Práctico_de_GIT2_II import vocal_o_consonante
from Práctico_de_GIT2_III import prod_de_lista
from palindromo import es_capicua


def hold(t):
    return sleep(t)


def clear():
    return system('clear')


def ejercicio1():
    a = int(input('Ingrese el primer número para comparar:\n>>> '))
    b = int(input('Ingrese el segundo número para comparar:\n>>> '))

    clear()

    print(f'El mayor número entre {a} y {b} es: {maximo(a,b)}')


def ejercicio2():
    mayor_de_3()


def ejercicio3():
    a = input('Ingrese los elementos de la lista separados por ",":\n>>> ')
    
    clear()

    print(f'La lista tiene {largo_lista(a.split(","))} elementos.')


def ejercicio4():
    vocal_o_consonante()


def ejercicio5():
    a = input('Ingrese los números de la lista separados por ",":\n>>> ')
    b = [int(i.strip()) for i in a.split(',')]

    clear()

    print(f'La sumatoria de los números de la lista es: {sumatoria(b)}')




def ejercicio6():
    prod_de_lista()


def ejercicio7():
    a = input('Ingrese los elementos de la primera lista separados por ",":\n>>> ')
    l1 = [i.strip() for i in a.split(',')]

    b = input('Ingrese los elementos de la segunda lista separados por ",":\n>>> ')
    l2 = [i.strip() for i in b.split(',')]

    res = 'si' if interseccion_listas(l1, l2) else 'no'

    clear()

    print(f'Las listas {res} tienen elementos en común.')


def ejercicio8():
    a = input('Ingrese una palabra:\n>>> ')

    res = 'si' if es_capicua(a) else 'no'

    clear()

    print(f'La palabra "{a}" {res} es un palíndromo.')
    


def procedimiento(key):
    funciones[key]()
    hold(3)
    

funciones = {
    '1': ejercicio1,
    '2': ejercicio2,
    '3': ejercicio3,
    '4': ejercicio4,
    '5': ejercicio5,
    '6': ejercicio6,
    '7': ejercicio7,
    '8': ejercicio8
}