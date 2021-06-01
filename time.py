import timeit
from random import randint
from ShellSort import *
from QuickSort import *
from MergeSort import *

lista = []
qtde_valores = 5


for i in range(qtde_valores):
    lista.append(randint(1, 5000))

print(shellSort(lista))
#print(mergeSort(lista))
print(mergeSort(lista))
#inicio = timeit.default_timer()
#shellSorted = shellSort(lista)
#quickSorted = quickSort(lista)
#mergeSorted = mergeSort(lista)
#fim = timeit.default_timer()

#print(fim-inicio)