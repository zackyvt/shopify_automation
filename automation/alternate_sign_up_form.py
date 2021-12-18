from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from json import dump
from twocaptcha import TwoCaptcha

def get_inputs(driver):
    first_name_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#account_first_name")))
    last_name_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#account_last_name")))
    password_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#account_password")))
    password_confirmation = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password-confirmation")))
    captcha_element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#h-captcha")))
    sign_up_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.ui-button.ui-button--primary.ui-button--full-width.ui-button--size-large.captcha__submit")))
    return (first_name_input, last_name_input, password_input, password_confirmation, captcha_element, sign_up_button)

solver = ""

def solve_captcha(driver, captcha_element):
    try:
        result = solver.hcaptcha(
            sitekey=captcha_element.get_attribute("data-sitekey"),
            url=driver.current_url,
        )
        driver.execute("document.getQuerySelector(\"[name=\"h-captcha-response\"]\").innerHTML=\"" + result + "\"")
        captcha_checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox")
        captcha_checkbox.click()
    except:
        input()

def fill_form(driver, inputs):
    (first_name_input, last_name_input, password_input, password_confirmation, captcha_element, sign_up_button) = inputs
    first_name_input.send_keys("John")
    last_name_input.send_keys("Smith")
    password_input.send_keys("Password123#")
    password_confirmation.send_keys("Password123#")
    solve_captcha(driver, captcha_element)
    sign_up_button = WebDriverWait(driver, 180).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ui-button.ui-button--primary.ui-button--full-width.ui-button--size-large.captcha__submit")))
    sign_up_button.click()

def main(driver, api_key):
    solver = TwoCaptcha(api_key)
    inputs = get_inputs(driver)
    fill_form(driver, inputs)