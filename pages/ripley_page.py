from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class RipleyPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.XPATH, "//*[@id='__next']/main/section/nav/main/nav/div/form/input")
        self.results = (By.XPATH, '//div[contains(@class, "catalog-product-details")]')

    def search(self, search_term):
        self.driver.get("https://simple.ripley.com.pe/")
        time.sleep(2)
        self.driver.find_element(*self.search_box).send_keys(search_term + Keys.RETURN)
        time.sleep(3)

    # def get_results(self):
    #     elements = self.driver.find_elements(*self.results)[:5]
    #     data = []
    #     for element in elements:
    #         try:
    #             product_name = element.find_element(By.XPATH, './/a').text
    #             product_link = element.find_element(By.XPATH, './/a').get_attribute("href")
    #             data.append({"WEB": "Ripley", "NOMBRE PRODUCTO": product_name, "LINK DEL PRODUCTO": product_link})
    #         except Exception as e:
    #             print(f"Error extrayendo un producto de Ripley: {e}")
    #    return data