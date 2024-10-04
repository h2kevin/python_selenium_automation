# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
# # 2 create a test case will open the target circle page
# @given('Open target main page')
# def open_main(context):
#     context.driver.get('https://www.target.com/')
#
#
# @when('User can open the Target Circle page')
# def open_target_circle(context):
#     target_circle=context.driver.find_element(By.CSS_SELECTOR,"#utilityNav-circle").click
#
#
# @then('Verify Target Circle page has {expected_amount} benefit cells')
# def verify_header_links(context, expected_amount):
#     expected_amount = int(expected_amount)
#     links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
#     assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'
#
#
#
# # 3  add any Target's product into the cart, and make sure it's there
#
# ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
# ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
# SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
#
#
#
# @when('Click on Add to Cart button')
# def click_add_to_cart(context):
#     context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
#     context.driver.wait.until(
#         EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
#         message='Side navigation product name not visible'
#     )
#
#
# @when('Store product name')
# def store_product_name(context):
#     context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
#     print(f'Product stored: {context.product_name}')
#
#
# @when('Confirm Add to Cart button from side navigation')
# def side_nav_click_add_to_cart(context):
#     context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
#     sleep(3)
#
#
# @then('Verify that correct search results shown for {product}')
# def verify_results(context, product):
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text