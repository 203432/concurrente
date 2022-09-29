import threading
from pytube import YouTube
import time

mutex = threading.Lock()
def crito(id,url):
    global x;
    print("Hilo = "+str(id)+" => "+url)
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("C:/Users/camac/Documents/concurrente/files/mutexes")
    print(yt)
    print("Video descargado con exito")

class Hilo(threading.Thread):
    def __init__(self,id,url):
        threading.Thread.__init__(self)
        self.id = id
        self.url = url

    def run(self):
        mutex.acquire()
        crito(self.id, self.url)
        # print("valor "+ str(self.id))
        mutex.release()

hilos = [
    Hilo(1,"https://www.youtube.com/watch?v=fjLIkF01a7Y"), #Mapache comiendo uvas
    Hilo(3,"https://www.youtube.com/watch?v=E5xC9i_1vvY"), #Thor love and thunder
    Hilo(4,"https://www.youtube.com/watch?v=ycz1K-vi-tg"), #Off de roblox
    Hilo(5,"https://www.youtube.com/watch?v=VZzSBv6tXMw"), #Minero del rubius
    ]
x=1;
init_time = time.time()
for h in hilos:
    h.start()
end_time = time.time() - init_time
print(end_time)