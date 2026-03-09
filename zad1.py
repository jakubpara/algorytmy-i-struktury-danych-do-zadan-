import math

a = float(input('Podaj a: '))#krok 1
b= float(input('Podaj b: '))
c = float(input('Podaj c: '))


def f_kwadratowa(a,b,c):
    delta = b ** 2 - 4 * a * c #krok 3
    if a == 0:  #obsługa reszty przypadków krok 2
        if b == 0:
            print('brak rozwiazan')
        else:
            print(f'jest jedno miejsce zerowe bo to funkcja liniowa')
    else:  #głowny algorytm krok 2


        if delta < 0:#krok 4
            return (f'brak rozwiązań, dleta równa {delta}')

        elif delta == 0:#krok 4
            x = -b/(2*a)
            return (f'jedno miejsce zerowe: {x}')

        elif delta > 0:#krok 4
            x1 = -b - math.sqrt(delta)/(2*a)
            x2 = -b + math.sqrt(delta)/(2*a)
            return (f'dwa miejsca zerowe: {x1 , x2}')#krok 5
print(f_kwadratowa(-1,4,2))
print(f_kwadratowa(1,2,3))
print(f_kwadratowa(a,b,c))