from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Tests
def test_basic_search(init_driver):
    init_driver.get("https://www.google.com/")

    google_search_bar = init_driver.find_element(By.NAME, "q")
    google_search_bar.send_keys("Tarjeta De Video" + Keys.RETURN)

    search_bar = init_driver.find_element(By.NAME, "q")
    search_bar.clear()

    first_element = init_driver.find_element(By.XPATH, "(//div[@class='yuRUbf']/a/h3)[1]")
    first_element_text = first_element.text.lower()

    assert first_element_text.startswith("tarjeta")

    first_link = init_driver.find_element(By.XPATH, "(//div[@class='yuRUbf']/a/h3)[1]")
    first_link.click()


def test_basic_search_amazon(init_driver):
    init_driver.get("https://www.amazon.com/")

    wait = WebDriverWait(init_driver, 10)

    search_bar = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
    search_bar.send_keys("iphone")

    search_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-search-submit-button")))
    search_button.click()

    price = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='a-price'])[2]")))
    price_text = price.text.replace("\n", ".")

    second_element = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='a-size-medium a-color-base a-text-normal'])[2]")))
    second_element.click()

    price_in_product = wait.until(EC.visibility_of_element_located((By.ID, "priceblock_ourprice")))
    price_in_product_text = price_in_product.text

    assert price_text == price_in_product_text
