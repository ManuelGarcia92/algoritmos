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