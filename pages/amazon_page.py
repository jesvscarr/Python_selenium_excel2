from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class AmazonPage:
    def __init__(self, driver):  # Asegúrate de que el constructor acepte un parámetro 'driver'
        self.driver = driver
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.results = (By.XPATH, '//div[contains(@class, "s-result-item")]')

    def search(self, search_term):
        self.driver.get("https://www.amazon.com/-/es/b/?_encoding=UTF8&node=120152003011&pd_rd_w=zPZhR&content-id=amzn1.sym.fe8213b5-7ead-49d7-8375-a5da28a9e0b0&pf_rd_p=fe8213b5-7ead-49d7-8375-a5da28a9e0b0&pf_rd_r=2X0Y8HW1G6N068242QGC&pd_rd_wg=hsNa9&pd_rd_r=4c6a9833-a492-4911-9d27-5f475a77d072&ref_=pd_hp_d_atf_unk")
        time.sleep(2)
        self.driver.find_element(*self.search_box).send_keys(search_term + Keys.RETURN)
        time.sleep(3)

    # def get_results(self):
    #     elements = self.driver.find_elements(*self.results)[:5]
    #     data = []
    #     for element in elements:
    #         try:
    #             product_name = element.find_element(By.XPATH, './/h2/a/span').text
    #             product_link = element.find_element(By.XPATH, './/h2/a').get_attribute("href")
    #             data.append({"WEB": "Amazon", "NOMBRE PRODUCTO": product_name, "LINK DEL PRODUCTO": product_link})
    #             print(f"Producto extraído: {product_name}")  # Asegúrate de que los datos se estén extrayendo
    #         except Exception as e:
    #             print(f"Error extrayendo un producto de Amazon: {e}")
    #    return data

