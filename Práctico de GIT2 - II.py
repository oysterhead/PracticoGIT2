op = input("Ingrese letra [Con 0 termina]: ")

while op != '0':
    if op == 'a' or op == 'e' or op == 'i' or op == 'o' or op == 'u':
        print ("%s Es una vocal" %op)
    else:
        print ("%s No es vocal" %op)

    op = input("Ingrese letra [Con 0 termina]: ")

#Ejercicio Par nro 2