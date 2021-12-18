from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from . import utils

def get_inputs(driver):
    email_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[id=\"0_signup_email\"]")))
    password_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[id=\"0_signup_password\"]")))
    store_name_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[id=\"0_signup_shop_name\"]")))
    sign_up_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.marketing-button.marketing-form__button")))
    return (email_input, password_input, store_name_input, sign_up_button)

def fill_form(inputs):
    (email_input, password_input, store_name_input, sign_up_button) = inputs
    email_input.send_keys(utils.random_email_generator())
    password_input.send_keys("Password123#")
    store_name_input.send_keys(utils.random_store_name_generator())
    sign_up_button.click()

def main(driver):
    fill_form(get_inputs(driver))