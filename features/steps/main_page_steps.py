from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon') #homework lesson 3
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

# 1 update Target product seach test case homework lesson 4
@when('Search for a {item}')
def search_product(context, item):
    print(item)
    # Search field => enter tea
    context.driver.find_element(By.ID, 'search').send_keys(item)
    # Search button => click
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)  # wait for search results page to load
    sleep(8)  # wait for search results page to load


# Example with multiple variables:
# @when('Login as {username} and {pw}')
# def search_product(context, username, pw):
#     context.driver.find_element(By.ID, 'username').send_keys(username)
#     context.driver.find_element(By.ID, 'password').send_keys(pw)

@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount) # '6' => 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


@then('Verify header is shown')
def verify_header(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_utilityHeaderContainer']")
