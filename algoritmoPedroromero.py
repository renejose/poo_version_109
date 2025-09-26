#Introduccion a la programacion orientada a objetos
#Algoritmo de búsqueda lineal

def buscar(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor = 5

print(buscar(lista, valor))