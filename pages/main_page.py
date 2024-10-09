from pages.base_page import Page


class MainPage(Page):

    SEARCHPRODUCT =(BY.CSS, "input[data-test='@web/Search/SearchInput']")
    def open_main(self):
        self.open('https://www.target.com/')

    def search_for_product(self, product_name): # homework lesson 7 # 2
        self.driver.find_element(*self.SEARCHPRODUCT).click()
