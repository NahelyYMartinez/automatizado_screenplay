import unittest
from selenium import webdriver
from tasks.login_page import LoginPage
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from time import sleep


class Test_Login(unittest.TestCase):
    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

    __user = 'standard_user'
    __password = 'secret_sauce'



    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test1_login(self):
        page_login = LoginPage().init_page(self.driver)
        self.assertTrue(page_login)
        sleep(5)

    def test2_insert_credential(self):
        driver = self.driver
        LoginPage().enter_credencial(driver, self.__user, self.__password)
        self.assertTrue("usuario correcto")
        sleep(2)

    def test3_login(self):
        driver = self.driver
        LoginPage().click_login(driver, self.__user, self.__password)
        self.assertTrue("login correcto")

    # @classmethod
    # def tearDownClass(cls):
    # cls.driver.quit()
