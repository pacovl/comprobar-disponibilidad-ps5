# Autor: Francisco de Vicente
# Versión: github
# Fecha: 16/04/2021
# Inspiracion: https://github.com/satssehgal/stockchecker/blob/main/stockchecker.py

# Librerias
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime

import smtplib
from email.message import EmailMessage

# Tiempo de refresco, en segundos
refresh_time = 3600

# Clase para gestionar las conexiones
class Stockr:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument("--headless") # Con esta opción algunas páginas bloquean la conexión
        self.driver = webdriver.Chrome(executable_path = 'chromedriver', options = chrome_options)
        self.timeout = 30

    def cerrar(self):
        self.driver.quit()
    
    # Caso genérico que devuelve el texto que hay dentro del elemento al que apunta cierto xpath dentro del link indicado
    def texto_xpath(self, link, xpath):
        self.driver.get(link)
        time.sleep(3)
        try:
            texto = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH, xpath))).text
        except:
            return 'MAL'
        print(texto)
        return texto
    
# Función para enviar un correo con cierto texto
def mandar_correo(texto):
    msg = EmailMessage()
    msg.set_content(texto)

    me = '<correo_origen>'     ### <-------------------------------------- Sustituir 
    you = '<correo_destino>'   ### <-------------------------------------- Sustituir
    msg['Subject'] = 'Aviso python'
    msg['From'] = me
    msg['To'] = you

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()

    gmail.login(me,'<contraseña_correo_origen>')   ### <------------------ Sustituir
    try:
        gmail.send_message(msg)
    except:
        print('No se puede mandar el correo')

# Ejecución principal
def main():
    # Flags para evitar repetición de correos
    flag_ejemplo = True

    # Bucle para refrescar
    while True:
        S = Stockr()
        print('Ejecutando a las: ', datetime.now())

        # EJEMPLO =================================================================================
        print('vvvvvvvvvv EJEMPLO vvvvvvvvvv')
        link_ejemplo = 'https://www.mediamarkt.es/es/product/_consola-sony-ps5-825-gb-4k-hdr-blanco-1487016.html'
        xpath_ejemplo = '//*[@id="root"]/div[2]/div[3]/div[1]/div/div[4]/div/div/div[3]/div/span'

        if ( S.texto_xpath(link_ejemplo, xpath_ejemplo) != 'Este artículo no está disponible actualmente.' and flag_ejemplo ):
            mandar_correo('Disponible en: ' + link_ejemplo)
            flag_ejemplo = False
        # FIN EJEMPLO =================================================================================
        
        S.cerrar() # cierra chrome
        time.sleep(refresh_time)

if __name__ == "__main__":
    main()