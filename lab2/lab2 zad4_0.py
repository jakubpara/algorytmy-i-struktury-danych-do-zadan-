slowo = str(input('podaj slowo: '))
slowo = slowo.lower()
slowo = slowo.strip()
litery = []

# tworzenie listy z liter
for i in slowo:
    litery.append(i)

# długość jako ilosc znaków słowa
dlugosc = len(litery)



def sprawdzenie(lista):
    wartosci = 0
    for indeks, element in enumerate(lista):
        od_konca = dlugosc - indeks - 1
        if element == lista[od_konca]:
            wartosci += 1
        else:
            print("Słowo nie jest tym jak to sie tam nazywa")
            break
    if wartosci == dlugosc:   #takie potwierdzenie że wszystko sie zgadza
        print("to jest to coś")

#jesli słowo ma nieparzysta ilosc liter to srodkową litere wywalamy
if dlugosc % 2 == 1:  # nieparzysta ilość znaków
    del (litery[dlugosc // 2]) #usuwamy środkowy
    dlugosc = len(litery)  # nowa dlugosc listy
    sprawdzenie(litery) #dodajemy to funkcje która sprawdza czy sie zgadza wszystko

elif dlugosc % 2 == 0:  # parzysta ilość znaków
    sprawdzenie(litery)
