import threading 
import time 
import random


class Philosopher(threading.Thread):

    def __init__(self, name, forkl, forkr, stopevent):
        threading.Thread.__init__(self)
        self.name = name
        self.forkl = forkl
        self.forkr = forkr
        self.stopevent = stopevent
        self.numVeces=0
        self.estado='pensando'
        

    def run(self):
        while not self.stopevent.is_set():
            self.think()
            self.estado='hambriento'
            self.dine()
        print(self.name, 'ha comido', self.numVeces)
        print(self.name, 'estado:',self.estado)

    def think(self):
        print(self.name,' está pensando.')
        time.sleep( random.uniform(2,10))
        self.estado='pensando'

    def dine(self):

        while not self.stopevent.is_set() or self.estado=='hambriento':
            print(self.name, ' está hambriento.')
            tenedori=self.forkl
            tenedord=self.forkr
            tenedori.acquire(True)
            print(self.name, 'Tomó el tenedor de la izquierda.')
            condicional = tenedord.acquire(False)
            print(self.name, 'Intenta tomar el tenedor de la derecha.')
            if condicional:
                self.estado='comiendo'
                print(self.name, '  Ha tomado los 2 tenedores.')
                print (self.name,' empezó a comer')
                time.sleep(random.uniform(1,5))
                print (self.name,' terminó de comer')
               
                self.numVeces=self.numVeces+1;
                tenedori.release()
                tenedord.release()
                self.estado='pensando'

            else:
                
                tenedori.release()
                print(self.name, ' Intento tomar otro tenedor y no pudo. Esperará.Suelta el tenedor')
                tenedori,tenedord  = tenedord, tenedori
                time.sleep(random.uniform(2,4))
        else:
            return




def main():
    forks = [threading.Lock() for i in range(5)]
    stopevent = threading.Event()
    philosophers = [Philosopher('Philosopher %i' % i, forks[i%5], forks[(i+1)%5], stopevent) for i in range(5)]
    for p in philosophers:
        p.start()

    time.sleep(20)
    print ('[Setting Stop-Event.]')
    stopevent.set()
    print ('[Waiting for Philosophers to stop...',)
    for p in philosophers:
        p.join()
    print ('Done.')


if __name__ == '__main__':
    main()

