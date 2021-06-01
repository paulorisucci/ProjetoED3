import timeit

def delayBubbleSort(list):

    inicio = timeit.default_timer()
    listaOrdenada = bubbleSort(list)
    delay = timeit.default_timer() - inicio
    return {"time":delay, "lista":listaOrdenada}

    return listaOrdenada


def bubbleSort(alist):

    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


    return alist