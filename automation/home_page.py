from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main(driver):
    driver.get("https://www.shopify.com/")
    sign_up_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#MainNavSignupButton")))
    cookie_button(driver)
    sign_up_button.click()

def cookie_button(driver):
    try:
        cookie_ok_button = driver.find_element(By.CSS_SELECTOR, ".marketing-button.marketing-button--small.marketing-button--skin-light.js-dismiss-btn")
        cookie_ok_button.click()
    except:
        pass