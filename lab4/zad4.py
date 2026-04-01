def ONP (wyrazenie):

    lista = wyrazenie #dzieki temu mamy całe liczby a nie pojedyncze cyfry

    operacje = {
        "+" : lambda x, y: x + y,
        "-" : lambda x, y: x - y,
        "*" : lambda x, y: x * y,
        "/" : lambda x, y: x / y,
        "^" : lambda x, y: x**y,
        "**" : lambda x, y: x**y
    }


    stos = []

    for i in wyrazenie.split():
        print(i)
        print (stos)
        if i.isdigit():
            stos.append(int(i))
            print(stos)
        elif i in operacje:
            x = stos.pop()
            y = stos.pop()
            wynik = operacje[i](y,x) #zamiana kolejności zeby dobrze odejmowało i dzielilo jesli dobrze rozumiem onp
            stos.append(wynik)
        elif i == "=":
            if stos:
                return stos.pop()
            else:
                print("Jest coś nie tak w zapisie")

print(ONP(" 10 2 - 4 / ="))
print(ONP(" 10 3 2 + / ="))
