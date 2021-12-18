from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import utils

def fill_form(driver, inputs):
    (first_name_input, last_name_input, address_input, apartment_input, city_input, post_code_input, phone_number_input, country_select, enter_store_button) = inputs
    first_name_input.send_keys("John")
    last_name_input.send_keys("Smith")
    address_input.send_keys("75 53rd Drive Vineland, NJ 08360")
    apartment_input.send_keys("-")
    city_input.send_keys("New Jersey")
    post_code_input.send_keys("08360")
    phone_number_input.send_keys(utils.random_phone_num_generator())
    country_select.select_by_visible_text("United States")
    province_select = get_province_select(driver)
    province_select.select_by_visible_text("New Jersey")
    enter_store_button.click()

def get_inputs(driver):
    first_name_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name=\"account_setup[firstName]\"]")))
    last_name_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name=\"account_setup[lastName]\"]")))
    address_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name=\"account_setup[address1]\"]")))
    apartment_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name=\"account_setup[address2]\"]")))
    city_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name=\"account_setup[city]\"]")))
    post_code_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name=\"account_setup[zip]\"]")))
    phone_number_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name=\"account_setup[phone]\"]")))
    country_select = Select(WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name=\"account_setup[country]\"]"))))
    enter_store_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label=\"Enter my store\"]")))
    return (first_name_input, last_name_input, address_input, apartment_input, city_input, post_code_input, phone_number_input, country_select, enter_store_button)

def get_province_select(driver):
    province_select = Select(WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name=\"province\"]"))))
    return province_select

def main(driver):
    inputs = get_inputs(driver)
    fill_form(driver, inputs)
