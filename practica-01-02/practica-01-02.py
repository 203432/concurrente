from threading import Thread, Lock ,Semaphore 
import time

semaforoConsumidor = Semaphore(1)
semaforoProductor = Semaphore(1)

PERSONAS = 9
PRODUCTORES = 5
CONSUMIDORES = 5
almacen = [];


class item(Thread):
    def __init__(self,id):
        super(Productor,self).__init__()
        self.id = id

class Productor(Thread):
    def __init__(self,id):
        super(Productor,self).__init__()
        self.id = id

    def producir(self):
            print("Agregando")
            time.sleep(3)
            print("El productor "+str(self.id)+" almaceno una nueva caja")
            almacen.append("Caja")
            semaforoConsumidor.release()

    def bloquear(self):
        print("Esta lleno el almacen")
        semaforoProductor.acquire()

    def run(self):
        for i in range(100):
            time.sleep(1)
            if len(almacen) > 5:
                self.bloquear()
            else:
                self.producir()
    


class Consumidor(Thread):
    def __init__(self,id):
        super(Consumidor,self).__init__()
        self.id = id

    def consumir(self):
            if len(almacen) < 1:
                semaforoConsumidor.acquire()
                print("No hay nada que el consumidor "+self.id+" pueda agarrar.")
            else:
                print("Consumiendo")
                almacen.pop(0)
                time.sleep(5)
                print("el consumidor "+self.id+" consumio con exito")
                semaforoProductor.release()
                

    def run(self):
        for i in range(100):
            time.sleep(3)
            self.consumir()
            

def main():
    productor = []
    consumidor = []

    for i in range(5):
        productor.append(Productor(str(i+1)))

    for i in range(5):
        consumidor.append(Consumidor(str(i+1)))

    for p in productor:
        p.start()
    for C in consumidor:
        C.start()


if __name__ == '__main__':
    main()