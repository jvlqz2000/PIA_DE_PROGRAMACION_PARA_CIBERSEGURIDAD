from pyhunter import PyHunter
from openpyxl import Workbook
import logging

logging.basicConfig(level=logging.INFO, filename="pia.log", format="%(asctime)s %(levelname)s:%(message)s")
def hunter(api, organizacion):
    try:
        print("Script para buscar información sobre un dominio")
        hunter = PyHunter(api)
#orga = input("Dominio a investigar: "
        def busqueda(organizacion):
            resultado = hunter.domain_search(company=organizacion, limit=1,emails_type='personal')
            return resultado
        def guardar_informacion(datos_encontrados, organizacion):
            libro = Workbook()
            hoja = libro.create_sheet(organizacion)
            libro.save("Hunter" + organizacion + ".xlsx")
            hoja = libro.active
            hoja.title = "Información"
            hoja["A1"] = "Dominio"
            hoja["A2"] = "Disponibilidad"
            hoja["A3"] = "Organización"
            hoja["A4"] = "País"
            hoja["A5"] = "Email encontrado"
            hoja["A6"] = "Tipo"
            hoja["A7"] = "Dominio de la fuente 1"
            hoja["A8"] = "Url de la fuente 1"
            hoja["A9"] = "Extraído el "
            hoja["A10"] = "Funcionamiento"
            hoja["B1"] = datos_encontrados["domain"]
            hoja["B2"] = datos_encontrados["disposable"]
            hoja["B3"] = datos_encontrados["organization"]
            hoja["B4"] = datos_encontrados["country"]
            hoja["B5"] = datos_encontrados["emails"][0]["value"]
            hoja["B6"] = datos_encontrados["emails"][0]["type"]
            hoja["B7"] = datos_encontrados["emails"][0]["sources"][0]["domain"]
            hoja["B8"] = datos_encontrados["emails"][0]["sources"][0]["uri"]
            hoja["B9"] = datos_encontrados["emails"][0]["sources"][0]["extracted_on"]
            hoja["B10"] = datos_encontrados["emails"][0]["sources"][0]["still_on_page"]
          
            print("Datos guardados en el excel")
            libro.save("Hunter"+organizacion+".xlsx")
        #busqueda(organizacion)
        datos_encontrados = busqueda(organizacion)
        guardar_informacion(datos_encontrados, organizacion)
        if datos_encontrados == None:
            #print("Dominio no encontrado:(")
            exit()
        else:
            print(datos_encontrados)
            print(type(datos_encontrados))
            guardar_informacion(datos_encontrados, organizacion)
    except Exception as e:
        print("Ocurrió un error, intente nuevamente")
        logging.error(e, exc_info=True)