import pytest
from pages.HomePage import HomePage
from pages.OrangePage import OrangePage
from pages.StructurePage import StructurePage

from conftest import load_data

data = load_data("/Users/bastian.silva/Desktop/Python/ConfiguracionInicial/data/OrangeData.json")

@pytest.mark.parametrize('credentials', data["Credentials"])
@pytest.mark.parametrize('section', data["Section"])
def test_login_orange(init_driver, section, credentials):

    homepage = HomePage(init_driver)
    homepage.load_page("https://opensource-demo.orangehrmlive.com/")
    homepage.login(credentials["user"], credentials["password"])

    orangepage = OrangePage(init_driver)
    orangepage.go_to_structure()

    structurepage = StructurePage(init_driver)
    structurepage.add_engineering_section(section["id"], section["name"], section["description"])

    assert structurepage.get_element() == "123 : Cloud"

