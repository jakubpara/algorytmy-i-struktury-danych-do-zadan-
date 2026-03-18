n = int(input('podaj ile ma być liczb w ciągu:'))   #krok 1
x = int(input('podaj jaką liczbe sprawdzic w ciagu'))  #krok 3

#tworze przykładowy ciąg
lista=[n]
for i in range(n-1):
    lista.append(lista[i]+i)
print(lista)


#faktyczny algorytm
def szukanie(n,x):
    if n <= 0:   #krok 2
      return 'wartość niepoprawna'
    else:
        if  any(x in lista for i in lista ):#zapobieganie żeby nie napisało ileś razy że obiektu nie ma
            for indeks,element in enumerate(lista):  #krok 4


                if x == element:
                    return f'znaleziono liczbe {x} na miejscu o indeksie {indeks}'    #krok 5

        else:
          return 'nie znaleziono podanej liczby'

print(szukanie(n,x))


