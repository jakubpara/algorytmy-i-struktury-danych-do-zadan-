import queue

q = queue.Queue()
for i in range(3):
    q.put(int(input(f'Podaj liczbe {i+1} do kolejki: ')))

while not q.empty():
    print(q.get())