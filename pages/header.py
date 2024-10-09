from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    CART_BTN =(By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGNIN_BTN=(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']")
    NAVIGATION_SIGNIN = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
    ADDPRODUCT=(By.CSS_SELECTOR, "button[data-test='chooseOptionsButton']")
    PRODUCTNAME=(By.CSS_SELECTOR, ".h-text-bs.h-display-flex")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6) # wait for search results page to load

    def click_cart(self):
        # self.wait_to_be_clickable_click(*self.CART_BTN)
        self.driver.find_element(*self.CART_BTN).click()

    def click_sign_in(self):  # homework lesson 7 # 1
        # Method to click on the "Sign In" button in the header
        self.driver.find_element(*self.SIGNIN_BTN).click()

    def navigation_menu_signin(self): # homework lesson 7 # 1
        # Verify that the sign-in form is displayed
        return self.driver.find_element(*self.NAVIGATION_SIGNIN).click()

    def add_product_to_cart(self): # homework lesson 7 #2
        self.driver.find_element(*self.ADDPRODUCT).click()

    def get_product_name(self): #homework lesson 7 #2
        return self.driver.find_element(*self.PRODUCTNAME).text
