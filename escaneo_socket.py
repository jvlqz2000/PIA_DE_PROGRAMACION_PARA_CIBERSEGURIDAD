import socket
from socket import *
import logging

logging.basicConfig(level=logging.INFO, filename="pia.log", format="%(asctime)s %(levelname)s:%(message)s")
def escaneo(ip, begin, end):
    try:
        print('comenzando el escaneo en la ip: ', ip)
        for puertos in range(int(begin), int(end)+1):
            cliente = socket(AF_INET, SOCK_STREAM)
            resultado = cliente.connect_ex((ip, puertos))
            if (resultado == 0):
                print(('puerto %d: Abierto') %(puertos))
            else:
                print(('puerto %d: Cerrado') %(puertos))
          #por ultimo cerramos la conexion para que se analice el siguiente puerto
            cliente.close()
    except Exception as error:
        logging.error(error, exc_info=True)
        print("Ocurrió un error:( ")

    
