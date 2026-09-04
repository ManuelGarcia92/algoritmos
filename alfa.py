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