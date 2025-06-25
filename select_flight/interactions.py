from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import os

class select_flight1:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
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
        self.driver.save_screenshot(ruta) #Realiza la captura de pantalla en la ruta creada

    def capture_error(self, mensaje, ruta_error): #Declara la función con los metodos a utilizar.
        self.warnings_list.append(mensaje) #Agrega el mensaje de advertencia a la warning list.
        logging.warning(mensaje) #Agrega el mensaje de advertencia en los logz.
        os.makedirs(os.path.dirname(ruta_error), exist_ok=True) #Crea los directorios en caso de no existir.
        self.save_screenshot(ruta_error) #Realiza la captura de pantalla en la ruta creada.

    def select_flight(self):
        try:
            self.wait = WebDriverWait(self.driver, 30)
            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='journeyFare_3432344634373745343334433446374533383334333033393745343135363745333233303332333532443330333632443330333237453335333333343335333433373332343433343331333533363333333833333334333333303333333933323434333433323334343633343337333433333334343333343436333234343333333233333330333333323333333533323434333333303333333633323434333333303333333233323434333333303333333533333331333333307E33313333']/journey-control-custom/div/div/div[1]/div[2]/button"))).click()            
            select_fare = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='journeyFare_3432344634373745343334433446374533383334333033393745343135363745333233303332333532443330333632443330333237453335333333343335333433373332343433343331333533363333333833333334333333303333333933323434333433323334343633343337333433333334343333343436333234343333333233333330333333323333333533323434333333303333333633323434333333303333333233323434333333303333333533333331333333307E33313333']/journey-control-custom/div/div/div[2]/div/div/div/div[1]/fare-control/div/div[3]/button")))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", select_fare)
            time.sleep(2)
            select_fare.click() 
            self.capture_screenshot("select_flight.png")

            self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader")))
            self.click_element("//*[@id='maincontent']/div/div[2]/div/div/button-container/div/div/button")
        except Exception as e: #Controla los errores del bloque try con exception.
            self.capture_error(f"⚠️ no fue posible seleccionar vuelo {e}", "screenshots/error_select_flight.png")
        
        if self.warnings_list: #Verifica que la warning list no esta vacia.
            all_warnings = "\n".join(self.warnings_list) #Unifica todos los elementos que contienen warning.
            assert False, f"❌ Se encontraron los siguientes errores durante select flight:\n{all_warnings}" #Lanza un assertion con los warning de la lista indicando que fallo la prueba
        return True #Devuelve el valor tru si la warning list esta vacia.