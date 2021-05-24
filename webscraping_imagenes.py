from bs4 import BeautifulSoup
import requests
import os.path
import logging


logging.basicConfig(level=logging.INFO, filename="pia.log", format="%(asctime)s %(levelname)s:%(message)s")
def web_imagenes(url, ruta):
    try:
        r=requests.get(url)
        soup= BeautifulSoup(r.content, 'html.parser')
        links=list()
        images=soup.select('img[src]')
        for img in images:
            links.append(img['src'])
        os.mkdir(ruta)
        i=1
        for index, img_link in enumerate(links):
            if i<=len(links):
                img_data=requests.get(img_link).content
                with open(ruta+'\\'+str(index+1)+'.jpg', 'wb+') as f:
                    f.write(img_data)
                i+=1
            else:
                f.close()
                break
    except Exception as error:
        logging.error(error, exc_info=True)
        print("Ocurrió un error:( ")

