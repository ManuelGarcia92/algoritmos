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
