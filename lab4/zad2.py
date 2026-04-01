def sprawdz(wyrazenie):
    stos = []
    for znak in wyrazenie:
        if znak == "(":
            stos.append(znak)
        elif znak == ")":
            if not stos:
                return False  #jak nie ma nawiasu zamykającego pojawia sie false
    stos.pop()

    return len(stos) == 0 #jak zostanie jakis otwierający to z tego miejsca wyskoczy false

print(sprawdz("(()"))
