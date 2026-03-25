def odwrocone_dzialania(wyrazenie):

    lista = wyrazenie.split #dzieki temu mamy całe liczby a nie pojedyncze cyfry

    operacje = {
        "+" : lambda x, y: x + y,
        "-" : lambda x, y: x - y,
        "*" : lambda x, y: x * y,
        "/" : lambda x, y: x / y,
        "^" : lambda x, y: x**y,
        "**" : lambda x, y: x**y
    }


    stos = []

    for i in wyrazenie:
        if not i in operacje.keys():

        else:

            #tez skonczyc