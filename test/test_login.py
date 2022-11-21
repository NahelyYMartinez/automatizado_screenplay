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
    __incorrect_usu = 'locked_out_user'


    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test1_login(self):
        page_login = LoginPage().init_page(self.driver)
        self.assertTrue(page_login)
        sleep(5)

    def test2_login_incorrect(self):
        driver = self.driver
        LoginPage().incorrec_login(driver, self.__incorrect_usu, self.__password)
        self.assertTrue("user incorrect")
        sleep(2)

    def test3_login_correct(self):
        driver = self.driver
        LoginPage().enter_login(driver, self.__user, self.__password)
        self.assertTrue("user correct")

    # @classmethod
    # def tearDownClass(cls):
    # cls.driver.quit()
