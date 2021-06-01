import timeit


def delayInsertionSort(list):
    inicio = timeit.default_timer()
    listaOrdenada = insertionSort(list)
    delay = timeit.default_timer()-inicio
    return {"time":delay, "lista":listaOrdenada}

def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr