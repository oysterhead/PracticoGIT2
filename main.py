from funciones import hold, clear, procedimiento


opcion = False

while not opcion:
    clear()
    print(
        '''¿Qué operación desea realizar?

        1- Determinar máximo entre 2 números.
        2- Determinar máximo entre 3 números.
        3- Determinar largo de una lista.
        4- Determinar si un caracter ingresado es vocal o consonante.
        5- Sumar los elementos de una lista.
        6- Multiplicar los elementos de una lista.
        7- Verificar si hay elementos en común entre 2 listas.
        8- Verificar si una palabra es palíndromo.

        0- Salir.
        ''')
    opcion = input('>>> ')

    clear()

    if opcion in ['1','2','3','4','5','6','7','8']:
        procedimiento(opcion)
        opcion = False
    else:
        break
        