import queue

kolejka = queue.Queue()


def sklep():
    while True:
        print('wybierz działanie: \n'
              '1. Dodaj osobe z kolejki\n'
              '2. usun pierwsza osobe z kolejki \n'
              '3. Pokaż kolejkę i przewidywany czas\n'
              '4. Zakończ działanie programu')
        dzialanie = input("podaj liczbe: ")

        if dzialanie == '1':
            osoba = input('osoba w kolejce: ')
            czas_obslugi = int(input('podaj czas obsługi klienta: '))
            calosc = [osoba, czas_obslugi]
            kolejka.put(calosc)
            print('osoba dodana')

        elif dzialanie == '2':
            if not kolejka.empty():
                osoba, czas_obslugi = kolejka.get()
                print(f'Obsłużono {osoba}, (czas obsługi to {czas_obslugi})')
            else:
                print('W kolejce nikogo nie ma')

        elif dzialanie == '3':
            if not kolejka.empty():
                lista_pomocnicza = []

                while not kolejka.empty():
                    lista_pomocnicza.append(kolejka.get())
#zamiana kolejki na liste a potem z listy znowu do kolejki aby móc zmienić czas obsługi
                czas_oczekiwania = 0

                for i, krotka in enumerate(lista_pomocnicza):
                    #to nie krotka bo jest niemutowalna, tylko lista ale zeby sie nie mylisć tak nazwałem
                    lista_pomocnicza[i][1] = krotka[1]
                    print(f'{i + 1}. {krotka[0]} - czas obsługitej osoby to: {krotka[1]}. Łącznie czeka: {czas_oczekiwania}')
                    czas_oczekiwania += krotka[1]

                for element in lista_pomocnicza:
                    kolejka.put(element)

            else:
                print('Kolejka jest pusta')

        elif dzialanie == '4':
            break
        else:
            print('Nie ma takiego numeru')


sklep()