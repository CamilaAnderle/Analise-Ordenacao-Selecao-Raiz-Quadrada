from math import sqrt,floor
import time 
import random

n = 10**4
inicio_do_programa = time.perf_counter()
vetor  = [random.randint(0, n) for x in range(n)]

vetoresdivididos = []
sqra = floor(sqrt(len(vetor)))

for x in range(1,len(vetor)//sqra +1):
    vetoresdivididos.append(vetor[(x-1)*sqra:x*sqra])
if sqra*sqra != len(vetor):
    vetoresdivididos.append(vetor[sqra*(sqra):])

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return
        
activeb  = len(vetoresdivididos)
betters = []
result =  []

for i in range(len(vetoresdivididos)):
    bubbleSort(vetoresdivididos[i])
while activeb:
    maxt = -1  
    index =-1
    for j in range(len(vetoresdivididos)):
        if vetoresdivididos[j][0] >= maxt:
            maxt = vetoresdivididos[j][0]
            index = j 
    result.append(vetoresdivididos[index].pop(0))
    if(len(vetoresdivididos[index]) == 0):
        vetoresdivididos.pop(index)
        activeb -= 1


fim_do_programa = time.perf_counter()
tempo_total = fim_do_programa - inicio_do_programa
print(f"Tempo total: {tempo_total:.6f} segundos.")
