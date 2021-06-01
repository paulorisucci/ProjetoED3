import timeit

def delayShellSort(list):
    inicio = timeit.default_timer()
    listaOrdenada = shellSort(list)
    delay = timeit.default_timer() - inicio
    return {"time":delay, "lista":listaOrdenada}

#ShellSort
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:


      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)


      sublistcount = sublistcount // 2
    return alist

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position] = currentvalue
