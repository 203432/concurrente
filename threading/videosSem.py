from threading import Thread, Semaphore
from pytube import YouTube
semaforo = Semaphore(1)

def critico(id,url):
    print("Hilo = "+str(id)+" => "+url)
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print(yt)
    print("Video descargado con exito")


class Hilo(Thread):
    def __init__(self,id,url):
        Thread.__init__(self)
        self.id = id
        self.url = url

    def run(self):
        semaforo.acquire()
        critico(self.id, self.url)
        semaforo.release()

thread_semaforo = [
    Hilo(1,"https://www.youtube.com/watch?v=fjLIkF01a7Y"), #Mapache comiendo uvas
    Hilo(3,"https://www.youtube.com/watch?v=E5xC9i_1vvY"), #Thor love and thunder
    Hilo(4,"https://www.youtube.com/watch?v=ycz1K-vi-tg"), #Off de roblox
    Hilo(5,"https://www.youtube.com/watch?v=VZzSBv6tXMw"), #Minero del rubius
    ]
for t in thread_semaforo:
    t.start()