from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MercadoLibrePage:
    def __init__(self, driver):
        self.driver = driver

    def search(self, search_term):
        self.driver.get("https://www.mercadolibre.com.pe/#from=homecom")
        time.sleep(2)
        search_box = self.driver.find_element(By.NAME, "as_word")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

    def get_results(self):
        results = []
        try:
            # Selecciona los primeros 5 productos usando el XPath correcto
            items = self.driver.find_elements(By.XPATH, '//*[@id="root-app"]/div/div[3]/section/ol/li[position() <= 5]/div/div/div[2]/h3/a')

            # Itera sobre los elementos encontrados y extrae el nombre y el enlace
            for item in items:
                try:
                    product_name = item.text  # Nombre del producto
                    product_link = item.get_attribute("href")  # Enlace del producto
                    results.append({
                        "WEB": "Mercado Libre",
                        "NOMBRE PRODUCTO": product_name,
                        "LINK DEL PRODUCTO": product_link
                    })
                except Exception as e:
                    print(f"Error extrayendo un producto de Mercado Libre: {e}")
        except Exception as e:
            print(f"Error obteniendo resultados de Mercado Libre: {e}")

        return results
