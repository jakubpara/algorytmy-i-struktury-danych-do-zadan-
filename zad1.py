import math

a = float(input('Podaj a: '))
b= float(input('Podaj b: '))
c = float(input('Podaj c: '))


def f_kwadratowa(a,b,c):
    delta = b ** 2 - 4 * a * c
    if a == 0:  #obsługa reszty przypadków
        if b == 0:
            print('brak rozwiazan')
        else:
            print(f'jest jedno miejsce zerowe bo to funkcja liniowa')
    else:  #głowny algorytm


        if delta < 0:
            return (f'brak rozwiązań, dleta równa {delta}')

        elif delta == 0:
            x = -b/(2*a)
            return (f'jedno miejsce zerowe: {x}')

        elif delta > 0:
            x1 = -b - math.sqrt(delta)/(2*a)
            x2 = -b + math.sqrt(delta)/(2*a)
            return (f'dwa miejsca zerowe: {x1 , x2}')
print(f_kwadratowa(-1,4,2))
print(f_kwadratowa(1,2,3))
print(f_kwadratowa(a,b,c))