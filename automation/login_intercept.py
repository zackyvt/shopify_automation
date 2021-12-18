from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main(driver):
    try:
        account_choose = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ui-button.ui-button--transparent.ui-button--full-width.ui-button--size-large.account-picker__item")))
        account_choose.click()
    except: 
        pass