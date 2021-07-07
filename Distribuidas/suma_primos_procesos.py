import math, time
from multiprocessing import Process, Pipe

def isprime(n):
    if n<2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            return False
    return True  
  
def sum_primes(identificador,minimo,maximo,conn):
    suma = sum([x for x in range(minimo, maximo+1) if isprime(x)])
    conn.send(suma)
    print("Soy el proceso %d y la suma de los primos entre %d y %d es %d" %(
            identificador, minimo, maximo, suma ))

if __name__ == '__main__':
    while 1:
        
        input_n = input("Ingrese el número de máximo para la suma de primos: \n")
        input_numero_hilos = input("Ingrese el número de procesos: \n")        

        try:
            n = int(input_n)
            numprocess = int(input_numero_hilos)
        except ValueError :
            print("Los numeros deben ser enteros ")
            continue

        if numprocess > n:
            print("El numero de procesos debe ser menor al numero máximo para la suma")
            continue
        else:
            break
    
    pasos = math.ceil(n/numprocess)
    array = []
    for i in range(numprocess):
        min =  i*pasos + 1 
        max = (i+1) * pasos
        if min >= n:
            array.append(n-1)
            break
        array.append(min)
        if max >= n:
            array.append(n-1)
            break
        array.append(max)

    Tinicial = time.time()

    processes = []
    parent_conn = []
    child_conn = []

    for i in range(numprocess):
        parent_conn.append(0)
        child_conn.append(0)        

    for i in range(numprocess):
        parent_conn[i], child_conn[i] = Pipe()
    
    for i in range(0,numprocess * 2,2):
        print('Creando proceso', str(i/2))
        processes.append(Process(target=sum_primes,
        args=(i/2,array[i],array[i+1], child_conn[int(i/2)],)))    
    
    for process in processes:
        process.start()

    for process in processes:
        process.join()

    total = 0
    
    for i in range(numprocess):
        total += parent_conn[i].recv()
  
    print("El total de la suma de los primos hasta el %d es: %d" %(n, total))
    print("El tiempo es del calculo de los primos hasta el %d con %d hilos es %f: " 
    %(n, numprocess ,time.time() - Tinicial))
