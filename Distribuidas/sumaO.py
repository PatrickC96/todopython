import math
from time import time
from multiprocessing import Process

def isprime(n):
    if n<2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            return False
    return True
  
  
def sum_primes(numInicial,numFinal):
    return sum([x for x in range(numInicial, numFinal) if isprime(x)])


if __name__ == '__main__':

    Tinicial = time()
    print("La suma de los numeros primos es: ",sum_primes(2,1000000))
    Tfinal = time() - Tinicial
    print("El tiempo de ejecucion fue de: ",Tfinal)