wagi = [18, 5, 12, 3, 9]
n = len(wagi)
porownania = 0

print(f"Początkowa lista: {wagi}\n")

# Selection Sort
for i in range(n - 1):
    index_min = i

    for j in range(i + 1, n):
        porownania += 1
        if wagi[j] < wagi[index_min]:
            index_min = j

    # jesli indeks najmniejszej wagi to nie i to nastepuje zamiana miejs
    if index_min != i:
        wagi[i], wagi[index_min] = wagi[index_min], wagi[i]

    print(f"Lista po iteracji {i + 1} - {wagi}")

print(f"Lista posortowana: {wagi}")
print(f"Łączna liczba porównań: {porownania}")