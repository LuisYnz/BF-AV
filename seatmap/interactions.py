from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import logging

class seleccion_asientos:
    def __init__(self, driver):
        self.warnings_list = []
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def click_element(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def capture_screenshot(self, filename):
        ruta = os.path.join("screenshots", filename)
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        self.capture_screenshot(ruta)

    def capture_error(self, mensaje, ruta_error):
        self.warnings_list.append(mensaje)
        logging.warning(mensaje)
        os.makedirs(os.path.dirname(ruta_error), exist_ok=True)
        self.capture_screenshot(ruta_error)

    def selected_seat(self):
        self.wait = WebDriverWait(self.driver, 30)
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader")))
        seats = [ #Define la lista de asientos y pasajaeros.
            (1, "//*[@id='seatmapContainer']/div[1]/div/ul/li[3]/ol/li[1]/row/div/seat[1]/button"), #Define el pasajero y el asiento.
            (2, "//*[@id='seatmapContainer']/div[1]/div/ul/li[3]/ol/li[1]/row/div/seat[3]/button"),
            (3, "//*[@id='seatmapContainer']/div[1]/div/ul/li[3]/ol/li[1]/row/div/seat[4]/button"),
        ]   

        for passenger_number, xpath in seats: #Recorre cada uno de los asientos definidos en el xpath.
            try:
                seat = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath))) #Espera hasta que el asiento (definido por el XPath) sea visible en la página.
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", seat) #Realiza scroll en los asientos.
                seat.click() #Selecciona el asiento.
                self.capture_screenshot(f"select_seat_passenger_{passenger_number}.png") #Captura el screenshot del asiento seleccionado.
                logging.info(f"✅ Asiento seleccionado passenger {passenger_number}.") #Imprime el logging por asiento seleccionado.
            except Exception as e: #Controla el error.
                self.capture_error( #Captura el error si no no es psobile seleccionar el asiento.
                    f"⚠️ No fue posible seleccionar asiento passenger {passenger_number}: {e}", #Imprime el warning del asiento no seleccionado.
                    f"screenshots/error_select_seat_passenger_{passenger_number}.png" #Captura el screenshot del asiento no seleccionado.
                )
            logging.warning("⚠️ No se encontraron asientos para seleccionar.")
            return False

    def continue_button(self):
        xpaths = [  # Define la lista de los botones
            "/html/body/div[1]/main/div/div[4]/div/div/amount-summary-button-container/amount-summary-button/div/div/div[2]/ds-button[2]/button",
            "/html/body/div[1]/main/div/div[4]/div/div/amount-summary-button-container/amount-summary-button/div/div/div[2]/button[2]"
        ]

        for xpath in xpaths:  # Recorre los botones definidos en la lista.
            try:
                continuar = self.driver.find_elements(By.XPATH, xpath)
                if continuar:  # Verifica que el botón de la lista está presente.
                    continuar[0].click()  # Realiza click en el botón que encuentra de la lista.
                    logging.info("✅ Botón de continuar clickeado.")
                    return True
            except Exception as e:  # Controla el error si no fue posible encontrar el botón.
                self.capture_error(  # Captura el error si no fue posible hacer clic.
                    f"⚠️ No fue posible hacer clic en el botón de continuar: {e}",  # Imprime el warning del botón no encontrado.
                    f"screenshots/error_continue_button.png"  # Captura el screenshot del error.
                )
        logging.warning("⚠️ No se encontró el botón de continuar en ninguno de los XPaths.")
        return False

