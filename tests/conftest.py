import pytest
import json
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def load_data(path):

    with open(path) as data_file:
        data = json.load(data_file)

    return data

@pytest.fixture()
def config(scope="session"):
    with open("/Users/bastian.silva/Desktop/Python/ConfiguracionInicial/config.json") as config_file:
        config = json.load(config_file)

    assert config["browser"] in ["Firefox", "Chrome", "Headless Chrome"]

    return config


@pytest.fixture()
def init_driver(config):
    if config["browser"] == "Firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    elif config["browser"] == "Chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

    else:
        raise Exception("Browser" + config["browser"] + "is not supported")

    driver.maximize_window()

    # Retorna el driver
    yield driver

    # Cierra el driver para limpiar todo
    driver.quit()
