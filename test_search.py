from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Tests

def test_basic_search(init_driver):
    # Abrir pagina web
    init_driver.get("https://www.google.com/")

    # Buscar Elemento e Interactuar con el
    google_search_bar = init_driver.find_element(By.NAME, "q")
    google_search_bar.send_keys("Tarjeta De Video" + Keys.RETURN)

    # Limpiar barra de busqueda
    search_bar = init_driver.find_element(By.NAME, "q")
    search_bar.clear()

    # Verificar que la busqueda fue exitosa obteniendo el texto del elemento
    first_element = init_driver.find_element(By.XPATH, "(//div[@class='yuRUbf']/a/h3)[1]")
    assert "Tarjetas de Video - SP Digital.cl" == first_element.text

    # Buscar elemento y hacer click en el
    first_link = init_driver.find_element(By.XPATH, "(//div[@class='yuRUbf']/a/h3)[1]")
    first_link.click()
