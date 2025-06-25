#   home_page/interactions.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#   CASO AUTOMATIZADO 1
class Home_Page1:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, xpath):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))  # Espera que los elementos sean interactivo antes de dar click.
        element.click()  # Clica en los elementos.

    def send_keys(self, xpath, keys):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))  # Localiza los elementos.
        element.send_keys(keys)  # Ingresa informacion en los input.

    def save_screenshot(self, path):
        self.driver.save_screenshot(path)  # Realiza la captura de pantalla.
        print(f"Captura guardada en: {path}")  # Imprime el mensaje de la captura guardada.

    def select_dropdown(self, xpath, value_xpath):
        self.click_element(xpath)  # Abre el dropdown
        self.click_element(value_xpath)  # Selecciona la opcion del dropdown

    def select_idioma(self):  # Seleccionar el idioma.
        self.wait = WebDriverWait(self.driver, 30)
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "page-loader")))
        self.select_dropdown("//*[contains(@id, 'languageListTriggerId')]", "/html/body/div[1]/div[1]/main-header-container/main-header-layout-custom/header/div[1]/secondary-nav-custom/nav/ul/li[1]/ibe-language-selector/div/dropdown-list/dropdown/div/div/options-list/ul/li[1]/button")
        
    def select_pos(self):
        self.wait = WebDriverWait(self.driver, 30)
        self.click_element("//*[@id='pointOfSaleSelectorId']")
        self.click_element("//*[@id='pointOfSaleListId']/li[11]/button")
        self.click_element("/html/body/points-of-sale-container/div/div/points-of-sale-popup-layout-custom/div/div/div[3]/div/button")
        self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/pos_seleccionado.png")

    def vuelo_ow(self):
        self.wait = WebDriverWait(self.driver, 30)
        radio_button = self.wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='ibeSearchJourneyTypeControlId']/journey-type-control-custom/div/div/div[2]/ibe-checkbox")))
        radio_button.click()

    def estacion(self, origen, destino):  # Seleccionar origen y destino.
        self.wait = WebDriverWait(self.driver, 30)
        self.click_element("//*[@id='originBtn']")  # Abrir el boton departure.
        self.send_keys("//*[@id='originDiv']/input", "Bogota")  # Ingresa la ciudad de origen.
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='BOG']"))).click()
        #   Ingresa la ciudad de destino.
        self.send_keys("//*[@id='searchContentId_OW']/div[1]/station-control-custom/div/div[1]/div[2]/div[3]/div/input","Cali")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='CLO']"))).click()
        self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/origen_destino_final.png")

    def select_fechas(self):  # Seleccionar fechas de salida.
        self.wait = WebDriverWait(self.driver, 5)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='departureDateButtonId']"))).click()  # Clicar en el boton departure
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ngbStartDatepickerId']/div[2]/div[1]/ngb-datepicker-month-view/div[6]/div[4]/span/div[1]"))).click()  # Seleccionar fecha salida
        self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/fechas_seleccionadas.png")

    def passenger(self, joven, niño, bebe):
        self.wait = WebDriverWait(self.driver, 5)
        self.click_element("//*[@id='paxControlSearchId']/div/div[2]/div/ul/li[2]/div[2]/ibe-minus-plus/div/button[2]") #Seleccionar pasajero joven.
        self.click_element("//*[@id='paxControlSearchId']/div/div[2]/div/ul/li[3]/div[2]/ibe-minus-plus/div/button[2]") #Seleccionar pasajero niño.
        self.click_element("//*[@id='paxControlSearchId']/div/div[2]/div/ul/li[4]/div[2]/ibe-minus-plus/div/button[2]") #Seleccionar pasajero bebe.
        self.click_element("//*[@id='paxControlSearchId']/div/div[2]/div/div/button") #Clicar boton confirmar pasajeros.
        self.click_element("//*[@id='searchButton']") #Clicar boton buscar vuelos.
        self.save_screenshot("C:/Users/LuisYánezMalavé/Pictures/Screenshots/pasajeros_seleccionados.png") 