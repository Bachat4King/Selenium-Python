from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class StructurePage(BasePage):
    edit_button = (By.ID, "btnEdit")
    engineering_add_button = (By.ID, "treeLink_addChild_3")

    unit_id_element = (By.XPATH, "//input[@name='txtUnit_Id']")
    element_name = (By.XPATH, "(//input[@id='txtName'])")
    element_description = (By.XPATH, "//textarea")
    save_button = (By.XPATH, "//input[contains(@id, 'Save')]")

    done_button = (By.ID, "btnEdit")
    last_element_created = (By.XPATH, "//span[@class='labelNode tiptip']")


    def __init__(self, driver):
        super(StructurePage, self).__init__(driver)

    def add_engineering_section(self, unit_id, name, description):
        self.do_click(self.edit_button)
        self.do_click(self.engineering_add_button)

        self.do_send_keys(self.unit_id_element, unit_id)
        self.do_send_keys(self.element_name, name)
        self.do_send_keys(self.element_description, description)

        self.do_click(self.save_button)
        self.do_click(self.done_button)

    def get_element(self):
        return self.get_text(self.last_element_created)