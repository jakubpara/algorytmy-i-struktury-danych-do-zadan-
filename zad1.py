import math

a = float(input('Podaj a: '))
b= float(input('Podaj b: '))
c = float(input('Podaj c: '))

delta = b**2 - 4*a*c

if a == 0:  #obsługa reszty przypadków
    if b == 0:
        print('brak rozwiazan')
    else:
        print(f'jest jedno miejsce zerowe bo to funkcja liniowa')
else:  #głowny algorytm


    if delta < 0:
        print(f'brak rozwiązań, dleta równa {delta}')
    if delta == 0:
        x = -b/(2*a)
        print(f'jedno miejsce zerowe: {x}')
    if delta > 0:
        x1 = -b - math.sqrt(delta)/(2*a)
        x2 = -b + math.sqrt(delta)/(2*a)
        print(f'dwa miejsca zerowe: {x1 , x2}')
