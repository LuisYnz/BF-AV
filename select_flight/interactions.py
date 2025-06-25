from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import os

class select_flight1:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.warnings_list = []

    def click_element(self, xpath): #Declara la función con los metodos a utilizar.
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))) #Espera que los elementos sean interactivo antes de dar click.
        element.click() #Clica en los elementos.

    def send_keys(self, xpath, keys): #Declara la función con los metodos a utilizar.
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath))) #Localiza los elementos.
        element.send_keys(keys) #Ingresa informacion en los input.

    def capture_screenshot(self, filename): #Declara la función con los metodos a utilizar.
        ruta = os.path.join("screenshots", filename) #Crea la ruta del screenshot.
        os.makedirs(os.path.dirname(ruta), exist_ok=True) #Crea los directorios en caso de no existir.
        self.capture_screenshot(ruta) #Realiza la captura de pantalla en la ruta creada

    def capture_error(self, mensaje, ruta_error): #Declara la función con los metodos a utilizar.
        self.warnings_list.append(mensaje) #Agrega el mensaje de advertencia a la warning list.
        logging.warning(mensaje) #Agrega el mensaje de advertencia en los logz.
        os.makedirs(os.path.dirname(ruta_error), exist_ok=True) #Crea los directorios en caso de no existir.
        self.capture_screenshot(ruta_error) #Realiza la captura de pantalla en la ruta creada.

    def select_flight(self):
        try:
            self.wait = WebDriverWait(self.driver, 30)
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader")))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[.//span[normalize-space(text())='Seleccionar de tarifa']])[1]"))).click()        
            select_fare = self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[contains(@class, 'fare_button') and .//span[normalize-space(text())='Seleccionar']])[1]")))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_fare)
            time.sleep(2)
            select_fare.click() 
            self.capture_screenshot("select_flight.png")

            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'fare-confirmation')]")))
            contiue_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='maincontent']/div/div[2]/div/div/button-container/div/div/button")))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", contiue_button)
            time.sleep(2)
            contiue_button.click()
        except Exception as e: #Controla los errores del bloque try con exception.
            self.capture_error(f"⚠️ no fue posible seleccionar vuelo {e}", "screenshots/error_select_flight.png")
        
        if self.warnings_list: #Verifica que la warning list no esta vacia.
            all_warnings = "\n".join(self.warnings_list) #Unifica todos los elementos que contienen warning.
            assert False, f"❌ Se encontraron los siguientes errores durante select flight:\n{all_warnings}" #Lanza un assertion con los warning de la lista indicando que fallo la prueba
        return True #Devuelve el valor tru si la warning list esta vacia.