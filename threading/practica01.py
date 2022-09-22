from mimetypes import init
from urllib import response
import requests
import time
import psycopg2

def service():
    print("Hola Service")
    get_service()
    

def get_service():
    conexion = connect_db()
    cursor1=conexion.cursor()
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    if response.status_code == 200 :
        data = response.json()
        for dataout in data:
            cursor1.execute("insert into prueba1(title) values ('"+dataout["title"]+"')")
        conexion.commit()
        conexion.close()
    else:
        pass

def connect_db():
    conexion1 = psycopg2.connect(database="Concurrente", user="postgres", password="Nintendo64")
    return conexion1

def write_db():
  pass
    
    

if __name__ == "__main__":
    init_time = time.time()
    service()
    end_time = time.time() - init_time
    print(end_time)