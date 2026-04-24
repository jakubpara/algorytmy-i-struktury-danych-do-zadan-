Graf = {
    "A":{'B', 'C'},
    "B":{'D'},
    "C":{'B', 'E'},
    "D":{'E'},
    "E":{'B'}
}

def wypisz_sasiadow(Graf, wierzcholek):
    if wierzcholek in Graf :
        for i in Graf[wierzcholek]:
            print(i)
    else:
        print(f"nie ma wierzchołka {wierzcholek} w tym grafie")

wypisz_sasiadow(Graf, 'A')
wypisz_sasiadow(Graf, 'B')
wypisz_sasiadow(Graf, 'C')