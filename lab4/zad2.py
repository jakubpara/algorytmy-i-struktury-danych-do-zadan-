def sprawdz(wyrazenie):
    stos = []
    for znak in wyrazenie:
        if znak == "(":
            stos.append(znak)
        elif znak == ")":
            if not stos:
                return False
    stos.pop()

    return len(stos) == 0

print(sprawdz("(()"))
