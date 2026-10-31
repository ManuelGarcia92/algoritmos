def obtener_menor(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor

def ordenamiento_beta(lista):
    nueva_lista = []
    while lista:
        numero = obtener_menor(lista)
        nueva_lista.append(numero)
        lista.remove(numero)
    return nueva_lista

def ordenamiento_alfa(lista):
    e = 0
    while e < len(lista):
        lista_iterable = lista[e:]
        menor = lista_iterable[0]
        indice_menor = 0
        for t, i in enumerate(lista_iterable):
            if i < menor:
                menor = i  
                indice_menor = t + e
                lista[e], lista[indice_menor] = lista[indice_menor], lista[e]
        e += 1
    return lista

def ordenamiento_gama(lista):
    e = 0
    while e < len(lista):
        indice_menor = e
        for i in range(e, len(lista)):
            if lista[i] < lista[indice_menor]:
                indice_menor = i
        lista[e], lista[indice_menor] = lista[indice_menor], lista[e]
        e += 1
    return lista
