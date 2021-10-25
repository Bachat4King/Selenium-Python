from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class OrangePage(BasePage):

    admin = (By.ID, "menu_admin_viewAdminModule")
    organization = (By.ID, "menu_admin_Organization")
    structure = (By.ID, "menu_admin_viewCompanyStructure")

    def __init__(self, driver):
        super(OrangePage, self).__init__(driver)

    def go_to_structure(self):
        self.do_click(self.admin)
        self.do_click(self.organization)
        self.do_click(self.structure)
