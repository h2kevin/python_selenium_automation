from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# 2 create a test case will open the target circle page
@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('User can open the Target Circle page')
def open_target_circle(context):
    target_circle=context.driver.find_element(By.CSS_SELECTOR,"#utilityNav-circle").click


@then('Verify Target Circle page has {expected_amount} benefit cells')
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='h-margin-b-tiny']")
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


# 3  add any Target's product into the cart, and make sure it's there
@when('Search for a {item}')
def search_product(context, item):
    print(item)
    # Search field => enter tea
    context.driver.find_element(By.ID, 'search').send_keys(item)
    # Search button => click
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)  # wait for search results page to load


@then('Verify knife is in the shopping cart')
def verify_product(context):
    expected_result = 'Verify knife is in the shopping cart'
    actual_result =context.driver.find_element(By.CSS_SELECTOR, "#cart-summary-heading").text()
    assert expected_result == actual_result