slowo = str(input('podaj slowo: '))
slowo = slowo.lower()
slowo = slowo.strip()
slowo = "".join(i for i in slowo if i.isalnum() or i.isspace())


def czy_palindrom(napis):
    if len(napis) == 0 or len(napis) == 1:
        return True
    if napis[len(napis)-1] == napis[0]:
        return czy_palindrom(napis[1:len(napis)-1])
    else:
        return False


print(czy_palindrom(slowo))
print(czy_palindrom('kajak'))
print(czy_palindrom('słowo'))
