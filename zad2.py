n=int(input('podaj liczbe n: '))
lista = []


def sprawdzenie_parzystosci(liczba):
    if n > 0:

        i = 0
        licznik = 0
        while i < n:
            i += 1
            lista.append(i)

        for i in lista:
            if i % 2 == 0:
                licznik += 1
        return licznik

    else:
        return 'niepoprwna liczba'



print(sprawdzenie_parzystosci(n))
print(sprawdzenie_parzystosci(7))
print(sprawdzenie_parzystosci(-3))
