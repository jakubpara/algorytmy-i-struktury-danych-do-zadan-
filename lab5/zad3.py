import queue
q = queue.Queue()

def rejestracja():
    q.put(input('dodaj pacjenta do kolejki:'))

def wywolanie():
    pacjent = q.get()
    print(f'poproszono {pacjent} do gabinetu')

def kolejka():
    print(f'aktulna kolejka: {list(q.queue)}')


def menu():
    while True:
        print('wybierz działanie: \n'
              '1. Zarejestruj pacjenta\n'
              '2. Wywołaj pacjenta do gabinetu \n'
              '3. Pokaż aktualną kolejkę \n'
              '4. Zakończ działanie programu')
        dzialanie = input("podaj liczbe: ")

        if dzialanie == '1':
            rejestracja()
        elif dzialanie == '2':
            wywolanie()
        elif dzialanie == '3':
            kolejka()
        elif dzialanie == '4':
            break

        else:
            print("błędne działanie")

menu()

