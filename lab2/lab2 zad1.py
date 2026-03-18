def druga_najwieksza(lista):
    lista = set(lista) #usuwanie powtórek
    lista = list(lista)

    for i in range(1,len(lista)):
        sprawdzany = lista[i]
        od_i = i-1

        while od_i >= 0:
            if lista[od_i] > sprawdzany:
                lista[od_i+1] = lista[od_i]
                od_i = od_i - 1
            else:
                break

        lista[od_i+1] = sprawdzany

    return lista[-2]
print(druga_najwieksza([1,26,7,3]))
print(druga_najwieksza([23,54,76,21,32,11,4,5]))
print(druga_najwieksza([1,3,7,2,8,3,9,9,8]))

