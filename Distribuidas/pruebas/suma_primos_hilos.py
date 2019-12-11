"""
Pseudocódigo


"""

from threading import Thread
import math, time

total = 0

class Sumador(Thread):
    minimo = None
    maximo = None
    suma = None
    identificador = None
    def __init__(self, minimo, maximo, identificador):
        self.minimo = minimo
        self.maximo = maximo
        self.identificador = identificador
        Thread.__init__(self)
    
    def sum_primes(self):
        return sum([x for x in range(self.minimo, self.maximo + 1) if self.is_prime(x)])

    def is_prime(self, numero):
        if numero<2:
            return False
        if numero == 2:
            return True
        for i in range(2, int(math.sqrt(numero)) + 1):
            if numero % i == 0:
                return False
        return True

    def run(self):
        self.suma = self.sum_primes()
        global total
        total += self.suma
        print("Soy el hilo %d y la suma de los primos entre %d y %d es %d" %(
            self.identificador, self.minimo, self.maximo, self.suma
        ))


if __name__ == '__main__':
    while 1:
        
        input_n = input("Ingrese el número de máximo para la suma de primos: \n")
        input_numero_hilos = input("Ingrese el número de hilos: \n")
        

        try:
            n = int(input_n)
            numero_hilos = int(input_numero_hilos)
        except ValueError :
            print("Los numeros deben ser enteros ")
            continue

        if numero_hilos > n:
            print("El numero de hilos debe ser menor al numero máximo para la suma")
            continue
        else:
            break

    

    pasos = math.ceil(n/numero_hilos)
    array = []
    for i in range(numero_hilos):
        min =  i*pasos + 1 
        max = (i+1) * pasos
        if min >= n  :
            array.append(n-1)
            break
        array.append(min)
        if max >= n:
            array.append(n-1)
            break
        array.append(max)
    hilos = []
    tiempo_inicial = time.time()
    for i in range(0,numero_hilos * 2,2):
        print('Creando proceso', str(i/2))
        hilos.append(Sumador(array[i], array[i+1], i/2))
    
    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    tiempo_final = time.time()
    
    print("El total de la suma de los primos hasta el %d es: %d" %(n, total))
    print("El tiempo es del calculo de los primos hasta el %d con %d hilos es %f: segundos" %(n, numero_hilos ,tiempo_final - tiempo_inicial))
    
    