import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def select_random_from_dropdown(xpath, driver):
    dropdown_element = driver.find_element(By.XPATH, xpath)
    select = Select(dropdown_element)
    options = select.options
    random_choice = random.choice(options)
    select.select_by_visible_text(random_choice.text)