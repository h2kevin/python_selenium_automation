from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] .sc-d0f8f0a6-2")# homework lesson 5 number 2
SELECTED_COLOR = (By.CSS_SELECTOR, ".sc-68a8cd0e-0")# homework lesson 5 number 2


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['grey', 'dark khaki', 'navy/tan', 'stone/gey', 'white/gum', 'white/navy/red',
                       'white/sand/tan', 'black/gum'] # homework lesson 5 number 2
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for color in colors:
        print(color)
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color text', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print('actual_colors list: ', actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
