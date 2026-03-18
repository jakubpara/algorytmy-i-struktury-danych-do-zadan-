n=int(input('podaj liczbe n: ')) #krok 1
lista = []


def sprawdzenie_parzystosci(liczba):
    if n > 0:#krok 2

        i = 0#krok 3
        licznik = 0
        while i < n:
            i += 1
            lista.append(i)

        for i in lista:#krok 4
            if i % 2 == 0:
                licznik += 1
        return licznik #krok5

    else:#krok 2
        return 'niepoprwna liczba'



print(sprawdzenie_parzystosci(n))
print(sprawdzenie_parzystosci(7))
print(sprawdzenie_parzystosci(-3))
