from Wappalyzer import Wappalyzer, WebPage
import logging

logging.basicConfig(level=logging.INFO, filename="pia.log", format="%(asctime)s %(levelname)s:%(message)s")
def tecnologi(url):
    wap = Wappalyzer.latest()
    try:
        #warnings.simplefilter("ignore")
        web = WebPage.new_from_url(url)
        tecnologias = wap.analyze(web)
        for i in tecnologias:
            print("Tecnologias detectadas: {}".format(i))
    except Exception as e:
        print("Ocurrio un error intente nuevamente")
        logging.error(e, exc_info=True)
        

