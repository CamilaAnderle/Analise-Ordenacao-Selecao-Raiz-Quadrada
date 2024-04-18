import heapq as hq
import random
import time
from math import sqrt,floor

n = 10**4

vetor  =  [random.randint(0, n) for x in range(n)]
inicio_do_programa = time.perf_counter()

vetor = [-x for x in vetor]

vetoresdivididos = []
sqra = floor(sqrt(n))

for x in range(1,len(vetor)//sqra +1):
    vetoresdivididos.append(vetor[(x-1)*sqra:x*sqra])
if sqra*sqra != len(vetor):
    vetoresdivididos.append(vetor[sqra*(sqra):])

activeb  = len(vetoresdivididos)
betters = []
result =  []
for i in range(len(vetoresdivididos)):
    hq.heapify(vetoresdivididos[i])

while activeb:
    maxt = -1  
    index =-1 
    for j in range(len(vetoresdivididos)):
        if vetoresdivididos[j][0]*-1 >= maxt:
            maxt = vetoresdivididos[j][0]*-1
            index = j 
    result.append(hq.heappop(vetoresdivididos[index])*-1)
    if(len(vetoresdivididos[index]) == 0):
        vetoresdivididos.pop(index)
        activeb -= 1

fim_do_programa = time.perf_counter()
tempo_total = fim_do_programa - inicio_do_programa
print(f"Tempo total: {tempo_total:.6f} segundos.")
