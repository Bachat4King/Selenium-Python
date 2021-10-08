from pages.HomePage import HomePage
from pages.OrangePage import OrangePage
from pages.StructurePage import StructurePage


def test_login_orange(init_driver):

    homepage = HomePage(init_driver)
    homepage.load_page("https://opensource-demo.orangehrmlive.com/")
    homepage.login("Admin", "admin123")

    orangepage = OrangePage(init_driver)
    orangepage.go_to_structure()

    structurepage = StructurePage(init_driver)
    structurepage.add_engineering_section("123", "Cloud", "GoogleCloud")

    assert structurepage.get_element() == "123 : Cloud"
