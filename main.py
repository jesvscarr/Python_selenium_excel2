from selenium import webdriver
import pandas as pd
from pages.amazon_page import AmazonPage
from pages.mercadolibre_page import MercadoLibrePage
from pages.ripley_page import RipleyPage
from pages.falabella_page import FalabellaPage

def search_and_save_to_excel():
    driver = webdriver.Chrome()
    data = []

    try:
        amazon = AmazonPage(driver)
        amazon.search("motos")
    #    data.extend(amazon.get_results())

        mercado_libre = MercadoLibrePage(driver)
        mercado_libre.search("motos")
        data.extend(mercado_libre.get_results())

        ripley = RipleyPage(driver)
        ripley.search("polos")
    #    data.extend(ripley.get_results())

        falabella = FalabellaPage(driver)
        falabella.search("libros")
    #    data.extend(falabella.get_results())

        print(f"Datos extraídos: {data}")   
        if data:   
            df = pd.DataFrame(data)
            df.to_excel("resultados_busquedas.xlsx", index=False)
            print("Datos guardados en 'resultados_busquedas.xlsx' exitosamente.")
        else:
            print("No se extrajeron datos, archivo no guardado.")
    except Exception as e:
        print(f"Error en la ejecución general: {e}")
    finally:
        driver.quit()   

# Ejecutar la función
if __name__ == "__main__":
    search_and_save_to_excel()

