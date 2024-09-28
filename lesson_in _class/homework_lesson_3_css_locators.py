# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
# # open the url
# driver.get('https://www.amazon.com/')
# #amazon logo
# driver.find_element(By.CSS_SELECTOR,".a-link-nav-icon")
# #create account field
# driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")
# #email field
# driver.find_element(By.CSS_SELECTOR,"input#ap_email")
# #password field
# driver.find_element(By.CSS_SELECTOR,"input#ap_password")
# #re-enter password field
# driver.find_element(By.CSS_SELECTOR,"input#ap_password_check")
# #create your amazon account tab(continue tab)
# driver.find_element(By.CSS_SELECTOR,"input#continue")
# #conditions of use link
# driver.find_element(By.CSS_SELECTOR,"[href*='condition_of_use']")
# #privacy notice lin
# driver.find_element(By.CSS_SELECTOR,"#legalTextRow [href*='privacy_notice']")
# #sign in button
# driver.find_element(By.CSS_SELECTOR,".a-link-emphasis")
#
