from actions.click import Click
from ui.login_ui import LoginUi
from actions.display import Display
from actions.get import Get
from actions.send_keys import SendKeys
from selenium import webdriver


class LoginPage:

    def init_page(self, driver: webdriver):
        try:
            Get().get(driver, LoginUi.base_url)
            driver.maximize_window()
            return Display().view_element(driver, LoginUi().xpath_image_login)
        except Exception as inst:
            print("Error: To init the request", inst)

    def enter_credencial(self, driver: webdriver, user, password):
        try:
            Get().get(driver, LoginUi.base_url)
            driver.maximize_window()
            SendKeys().send_text(driver, LoginUi().input_user, user)
            SendKeys().send_text(driver, LoginUi().input_password, password)

        except Exception as inst:
            print("Error: login", inst)
    def click_login(self, driver: webdriver, user, password):
        try:
            Get().get(driver, LoginUi.base_url)
            driver.maximize_window()
            SendKeys().send_text(driver, LoginUi().input_user, user)
            SendKeys().send_text(driver, LoginUi().input_password, password)
            Click().click_element(driver, LoginUi().button)

        except Exception as inst:
            print("Error: login", inst)

