from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):

    username = (By.ID, "txtUsername")
    password = (By.ID, "txtPassword")
    button = (By.NAME, "Submit")
    
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def load_page(self, url):
        self.driver.get(url)

    def login(self, username_text, password_text):
        self.do_send_keys(self.username, username_text)
        self.do_send_keys(self.password, password_text)
        self.do_click(self.button)
