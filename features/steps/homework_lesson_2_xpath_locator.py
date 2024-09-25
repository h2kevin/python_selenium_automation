from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
# Amazon logo
driver.find_element(By.XPATH,"//i[@aria-label='Amazon']")
#Email field
driver.find_element(By.ID,'ap_email')
#Continue button
driver.find_element(By.ID,'continue')
#conditions of use link
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")
#privacy notice link
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")
#need help link
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")
#forgot your password link
driver.find_element(By.ID,'auth-fpp-link-bottom')
#other issues with Sign-in
driver.find_element(By.ID,'ap-other-signin-issues-link')
#create your amazon account button
driver.find_element(By.ID,'createAccountSubmit')
