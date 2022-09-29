import threading
import concurrent.futures
from time import sleep
from turtle import title
from unicodedata import name
import requests
import psycopg2
from pytube import YouTube
import time

def get_services(dato = 0):
    print(f'Dato = {dato}')
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        result = response.json().get('results')
        name = result[0].get('name').get('first')
        print(name)

def register_db():
    conexion = connect_db()
    cursor1=conexion.cursor()
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    if response.status_code == 200 :
        data = response.json()
        for dataout in data:
            cursor1.execute("insert into prueba1(texto) values ('"+dataout["title"]+"')")
            print("Agregado a la base de datos: su id es: "+str(dataout["id"]))
        conexion.commit()
        conexion.close()
    else:
        pass



def connect_db():
    conexion1 = psycopg2.connect(database="Concurrente", user="postgres", password="Nintendo64")
    return conexion1

def download_vid():
    urlsList = [
    "https://www.youtube.com/watch?v=fjLIkF01a7Y", #Mapache comiendo uvas
    "https://www.youtube.com/watch?v=E5xC9i_1vvY", #Thor love and thunder
    "https://www.youtube.com/watch?v=ycz1K-vi-tg", #Off de roblox
    "https://www.youtube.com/watch?v=VZzSBv6tXMw", #Minero del rubius
    ]
    for url in urlsList:
        thDownload = threading.Thread(target = get_video, args=[url])
        thDownload.start()
def get_video(url):
    print("Descargando un video nuevo")
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print(yt)
    print("Video descargado con exito")

if __name__ == '__main__':
    thVideo = threading.Thread(target = download_vid)
    thRegister = threading.Thread(target= register_db)
    thVideo.start()
    thRegister.start()
    for x in range(0,50):
       thService = threading.Thread(target = get_services, args=[x])
       thService.start()