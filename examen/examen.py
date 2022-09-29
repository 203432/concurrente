import threading
from time import sleep, time

mutex = threading.Lock()
def comer(id):
    global palillos;
    palIzq= id-1
    palder = id
    if palillos[palIzq].estado == "libre" and palillos[palder].estado == "libre":
        palillos[palIzq].estado = "ocupado"
        palillos[palIzq].ocupadoPor = id
        palillos[palder].estado = "ocupado"
        palillos[palder].ocupadoPor = id
        print("La persona " +str(id)+ " esta usando Palillo izquierdo Num: "+str(palillos[palIzq].num)+" y Palillo derecho es el numero "+str(palillos[palder].num)  )
        print("Comiendo ")
        sleep(10)
        palillos[palIzq].estado = "libre"
        palillos[palIzq].ocupadoPor = id
        palillos[palder].estado = "libre"
   
class Palillo():
    def __init__(self,num,estado,ocupadoPor):
        self.num = num
        self.estado = estado
        self.ocupadoPor = ocupadoPor
class Persona(threading.Thread):
     def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

     def run(self):
        mutex.acquire() #Inicializa semáforo , lo adquiere
        comer(self.id)
        mutex.release() #Libera un semáforo e incrementa la varibale

palillos=[Palillo(1,"libre",0),Palillo(2,"libre",0),Palillo(3,"libre",0),Palillo(4,"libre",0),Palillo(5,"libre",0),Palillo(6,"libre",0),Palillo(7,"libre",0),Palillo(8,"libre",0),Palillo(9,"libre",0)];
Personas = [Persona(1), Persona(2), Persona(3), Persona(4), Persona(5), Persona(6), Persona(7), Persona(8)]
for p in Personas:
    p.start()