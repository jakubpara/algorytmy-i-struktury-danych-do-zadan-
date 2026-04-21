def wyszukiwanie_liniowe(lista, szukana_liczba):
    for i in range(len(lista)):
        if lista[i] == szukana_liczba:
            return i
    return -1

print(wyszukiwanie_liniowe([1,2,4,6,8],8))
print(wyszukiwanie_liniowe([1,2,4,6,8],9))