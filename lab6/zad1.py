def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1 -i ):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = input("podaj wyniki po spacji: ").split()
lista= list(map(int, lista))

print(bubble_sort(lista))
print(bubble_sort([0,6,3,4,9,7,2]))
