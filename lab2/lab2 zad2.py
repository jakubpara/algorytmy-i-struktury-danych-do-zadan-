import numpy as np

def znajdz_min_max(macierz):
    tablica = np.array(macierz)
    print(f'Oryginalna macierz:\n{tablica}\n')

    min_wartosc = np.min(tablica)
    max_wartosc = np.max(tablica)

    min_indeks = [] # tu bedą w liscie krotki a w nich indeksy najmniejszych i najwikszych elementów
    max_indeks = []

    for i, wiersz in enumerate(macierz):
        for j, wartosc in enumerate(macierz[i]):

            if wartosc == min_wartosc:
                min_indeks.append((i, j))

            if wartosc == max_wartosc:
                max_indeks.append((i,j))

    for i in min_indeks:
        macierz[i[0]][i[1]] = "MIN"

    for i in max_indeks:
        macierz[i[0]][i[1]] = "MAX"

    for wiersz in macierz:
        print(wiersz)

    return macierz

macierz = [
    [5, 2, 9, 8],
    [1, 7, 3, 9],
    [6, 0, 2, 5]
]

znajdz_min_max(macierz)