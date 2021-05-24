
import argparse
import logging
import os.path
import subprocess


from Hunter import *
from metadata_imagenes import *
from tecnologia_web import tecnologi
from escaneo_socket import escaneo
from webscraping_imagenes import web_imagenes

 
#---------------------------------------------------------------------------------------

    
#------------------------------------------------------------------------------------------



if __name__=="__main__":
    #Menu
    description ="""Bienvenido este Menú realiza diversas actividades de Ciberseguridad. 
    Actividades que realiza el Script: 
    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    [1].- WEB SCRAPING(Extraer las imagenes de un sitio web)
    -Execution Example:PIA_de_PC.py -op 1 -url "URL" -R "RUTA(ruta donde se almacenaran las imagenes)"
    
    [2].- METADATA DE IMÁGENES (Analizar metadatos de Imagenes)
    -Execution Example:PIA_de_PC.py -op 2  -R "RUTA"
    
    [3].- ESCANEO CON SOCKET(Detecta los puertos si estan abiertos o cerrados)
    -Execution Example:PIA_de_PC.py -op 3 -ip "IP" -begin "30" -end "50"
    
    [4].- IDENTIFICAR TECNOLOGIA DE WEBSITE(Ingresa un sitio web que desas analizar)
    -Execution Example:PIA_de_PC.py -op 4 -url "URL"
    
    [5].- EXTRAER INFORMACION DE UN DOMINIO(Script para buscar información sobre un dominio)
    -Execution Example:PIA_de_PC.py -op 5 -api "APIKEY" -organizacion "ORGANIZACION"
    
    [6].- OBTENCIÓN DE CLAVES HASH(Obtener la calve Hash de un carpeta) 
    -Execution Example:PIA_de_PC.py -op 6 -R "RUTA"

   
    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||  
    """
    #Argumentos

    parser = argparse.ArgumentParser(description = "Multiples actividades de CiberSeguridad", epilog=
                                         description, formatter_class = argparse
                                         .RawDescriptionHelpFormatter) 
    parser.add_argument("-op", '--op', help = 'Selecciona una Opcion a ejecutar', required = 'True')
    parser.add_argument('-url', '--url', help = 'Ingresa la url del sitio web', default = '')
    parser.add_argument('-R', '--ruta', help = 'Ingresa una ruta ', default = '')      
    parser.add_argument('-ip', help = 'Ingresa una IP', default = '')
    parser.add_argument('-begin', '--begin', help = 'Ingresa el puerto inicial', default = '')
    parser.add_argument('-end', '--end',help = 'Ingresa el puerto final', default = '') 
    parser.add_argument('-api', '--api',help = 'Ingresa tu api key', default = '')
    parser.add_argument('-organizacion', '--organizacion', help = 'ngresa la organización a investigar', default = '')
    parser.add_argument('-option', '--option', help = 'Ingresa el tipo de red que deseas analizar (Status, Publica, Private)', default = '') 
    args = parser.parse_args()
    opcion = args.op 
    ruta = args.ruta
    option = args.option
    ip = args.ip
    begin = args.begin
    end = args.end
    url = args.url
    api = args.api
    organizacion = args.organizacion

    #os.mkdir("Reportes")     

    if opcion == str(1):
        web_imagenes(url, ruta)
    
    if opcion == str(2):
        printMeta(ruta)
        
    if opcion == str(3):
        escaneo(ip, begin, end)
    
    if opcion == str(4):
        tecnologi(url)

    if opcion == str(5):
        hunter(api, organizacion)   

    if opcion == str(6):
        if os.path.isdir(ruta):
            logging.basicConfig(level=logging.INFO, filename="pia.log", format="%(asctime)s %(levelname)s:%(message)s")
            try:
                PS = 'Powershell -ExecutionPolicy ByPass -File .\\Hash.ps1 -ruta ' + ruta
                runningProcesses = subprocess.check_output(PS)
                print(runningProcesses.decode())
                print('Valor Hash obtenido')
            except Exception as e:
                logging.error("Ocurrio un error")
                print("Ocurrio un error")
        else:
            logging.error("La ruta que ingreso no existe")
            logging.error(e, exc_info=True)
            print("La ruta no es valida, intente nuevamente")


    
    


    

