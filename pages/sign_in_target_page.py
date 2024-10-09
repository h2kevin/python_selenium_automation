from selenium.webdriver.common.by import By
from time import sleep

from pages.main_page import Page
from pages.base_page import Page

class SignInTargetPage:

    SignInTargetPage=(By.CSS_SELECTOR, ".sc-fe064f5c-0")

    def verify_sign_in_page(self): #homework lesson 7 #1
        self.verify_sign_in_page(*self.SignInTargetPage).click()

