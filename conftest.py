import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def init_driver():

    driver = webdriver.Chrome(ChromeDriverManager().install())

    yield driver

    driver.quit()