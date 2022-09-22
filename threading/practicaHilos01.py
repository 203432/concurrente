import requests
import time
import concurrent.futures
import threading
import psycopg2

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)
    

def get_service(url):
    conexion = connect_db()
    cursor1=conexion.cursor()
    response = requests.get(url)
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
    url_site = ["https://jsonplaceholder.typicode.com/photos"]
    service(url_site)
    end_time = time.time() - init_time
    print(end_time)