def wyszukiwanie_binarne(tablica,x,indeks_poczatek, indeks_koniec):
    if indeks_poczatek  <= indeks_koniec:
        indeks_srodek = (indeks_poczatek + indeks_koniec ) // 2

        if tablica[indeks_srodek] == x:
            return indeks_srodek
        elif tablica[indeks_srodek] < x:
            return wyszukiwanie_binarne(tablica, x, indeks_srodek + 1, indeks_koniec)
        elif tablica[indeks_srodek] > x:
            return wyszukiwanie_binarne(tablica, x, indeks_poczatek, indeks_srodek - 1)

    return -1
#test
tablica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("indeks na którym znajduje się szukany element to: ", wyszukiwanie_binarne(tablica, 8, 0, len(tablica) - 1))

