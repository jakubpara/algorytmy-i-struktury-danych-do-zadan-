import queue
q = queue.Queue()

def pobieranie(lista,n):
    lista_pomocnicza = []
    if q.qsize() == 0:
        print('Kolejka jest pusta')

    for i in range (len(lista)):
        q.put(lista[i])

    if n >= q.qsize():
        print( list(q.queue))
        return
    elif n < q.qsize():

        for i in range(n):
            lista_pomocnicza.append(q.get())

        print(lista_pomocnicza)
        lista_pomocnicza.clear()
        return
pobieranie([1,2,3,4,5,6,7,8,9,10],11)
pobieranie([10,20,30,40,50,60,70],5)
