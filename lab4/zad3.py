def undo_system():
    stos = []
    while True:
        slowo = input("POdaj jakiś tekst(Undo abycofnąć i Exit aby wyjść)")

        if slowo.lower() == "undo":
            if stos:
                cofniete = stos.pop()
                print(f"cofnirieto {cofniete}")
            else:
                print("stos pusty")

        elif slowo.lower() == "exit":
            print("koniec programu")
            break

        else:
            stos.append(slowo)
            print(stos)
undo_system()