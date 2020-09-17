def palindroma (cadena):
    auxiliar = []
    auxiliar2 = []

    for c in cadena:
        auxiliar.insert(0,c)
        auxiliar2.append(c)
    
    return auxiliar == auxiliar2

txt = input("Ingrese texto aqui -> ")
print(palindroma(txt))