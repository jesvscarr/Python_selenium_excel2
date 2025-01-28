from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class FalabellaPage:
    def __init__(self, driver):
        self.driver = driver
        self.close_popup_button = (By.ID, "closePopup")  # Locator para el popup
        self.search_box = (By.ID, "testId-SearchBar-Input")
        self.results = (By.XPATH, '//div[contains(@class, "pod-item")]')

    def close_popup(self):
        try:
            # Espera a que el popup esté presente y haga clic en él
            close_button = self.driver.find_element(*self.close_popup_button)
            close_button.click()
            print("Popup cerrado.")
        except Exception as e:
            print(f"No se pudo cerrar el popup: {e}")

    def search(self, search_term):
        self.driver.get("https://www.falabella.com/")
        time.sleep(2)
        # Llamar al metodo para cerrar el popup si es necesario
        self.close_popup()

        self.driver.find_element(*self.search_box).send_keys(search_term + Keys.RETURN)
        time.sleep(3)

    # def get_results(self):
    #     elements = self.driver.find_elements(*self.results)[:5]
    #     data = []
    #     for element in elements:
    #         try:
    #             product_name = element.find_element(By.XPATH, './/b[contains(@class, "pod-title")]').text
    #             product_link = element.find_element(By.XPATH, './/a').get_attribute("href")
    #             data.append({"WEB": "Saga Falabella", "NOMBRE PRODUCTO": product_name, "LINK DEL PRODUCTO": product_link})
    #         except Exception as e:
    #             print(f"Error extrayendo un producto de Saga Falabella: {e}")
    #    return data