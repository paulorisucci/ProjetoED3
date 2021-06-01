import timeit
from random import randint
from ShellSort import *
from QuickSort import *
from MergeSort import *
from InsertionSort import *
from BubbleSort import *

lista = []
qtde_valores = 20000


for i in range(qtde_valores):
    lista.append(randint(1, 5000))
bubbleSortedList = lista.copy()
insertionSortedList = lista.copy()
shellSortedList = lista.copy()
mergeSortedList = lista.copy()
quickSortedList = lista.copy()


print(f"Bubble Sort: {delayBubbleSort(bubbleSortedList)['time']}")
print(f"Insertion Sort: {delayInsertionSort(insertionSortedList)['time']}")
print(f"Shell Sort: {delayShellSort(shellSortedList)['time']}")
print(f"Merge Sort: {delayMergeSort(mergeSortedList)['time']}")
print(f"Quick Sort: {delayQuickSort(quickSortedList)['time']}")

