import math
import os
from time import time
from multiprocessing import Process

numprocess = os.cpu_count()
total = 0

def isprime(n):
    if n<2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            return False
    return True
  
  
def sum_primes(n,sumas):
    numFinal = 100000
    #print(sum([x for x in range(2, numFinal) if (x % numprocess)==n if isprime(x)]))
    for x in range(2, numFinal):
        if (x % numprocess)==n:
            if isprime(x):
                sumas +=x

    

if __name__ == '__main__':

    Tinicial = time()

    processes = []
    suamtotal = [0,0,0,0]

    for i in range(numprocess):
        print('registering process %d' % i)
        processes.append(Process(target=sum_primes,args=(i,suamtotal[i]),))

    for process in processes:
        process.start()

    for process in processes:
        process.join()
   
    Tfinal = time() - Tinicial
    total=0
  
    print(suamtotal)
    #for process in suamtotal:
    #    total+=suamtotal[process]
    print("El valor de la suma es: ",total)
    print("El tiempo de ejecucion fue de: ",Tfinal)