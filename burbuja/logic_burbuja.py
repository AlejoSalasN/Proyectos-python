def ordenamientoBurbuja(arr):
    n: int = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


lista = [45, 1, 47, 89, 100]
ordenamientoBurbuja(lista)

print(lista)
