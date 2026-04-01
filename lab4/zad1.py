def odwroc_kod ():
    stos = []
    liczby = input("podaj ciag liczb: ").split()
    for a in liczby:
        stos.append(int(a))
    while stos:
        print(stos.pop())

odwroc_kod()
