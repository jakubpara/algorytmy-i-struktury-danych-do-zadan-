import random

x = random.randint(1,100) #krok 1.1
licznik = 1 #krok 1.2



while True:
    proba = int(input('podaj liczbe od 1 do 100: ')) #krok 1.3
    if proba == x:  #krok 1.3.1
        print(f'gratulacje, poprawna liczba. ')
        break
    elif proba > x:
        print(f'wpisana liczba jest za duża.') #krok 1.3.2
        licznik += 1 #1.3.4
    elif proba < x:
        print(f'wpisana liczba jest za mała. ') #krok 1.3.3
        licznik += 1 #1.3.4
print(f'szukaną liczbą było {x}') #krok1.4
print(f'twoja liczba prób to {licznik}') #krok 1.5

