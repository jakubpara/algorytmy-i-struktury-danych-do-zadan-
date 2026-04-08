import heapq
kolejka = []
heapq.heapify(kolejka)
def main():
    while True:
        print('wybierz działanie: \n'
              '1. Dodaj zadanie z priorytetem\n'
              '2. obsłuż zadanie z najwyższym priorytetem \n'
              '3. Pokaż kolejkę zadań \n'
              '4. Zakończ działanie programu')
        dzialanie = input("podaj liczbe: ")
        if dzialanie == '1':
            zadanie = input('podaj zadanie: ')
            priorytet = input('podaj priorytet zadania: ')
            calosc = (zadanie , priorytet)
            heapq.heappush(kolejka, calosc)
            print('zadanie dodane')
        elif dzialanie == '2':
            if kolejka:
                zadanie , priorytet = heapq.heappop(kolejka)
                print(f'Obsłużono zadanie {zadanie}, (priorytet = {priorytet})')
            else:
                print('W kolejce nic nie ma')
        elif dzialanie == '3':
            if kolejka:
                print('tak wygląda obecnie kolejka')
                for z,p in kolejka:
                    print(f'zadanie {z} - {p}')
        elif dzialanie == '4':
            break
        else:
            print('Nie ma takiego numeru')


main()

