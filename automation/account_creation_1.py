from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main(driver):
    skip_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.Polaris-Button_r99lw.Polaris-Button--sizeLarge_61dxo")))
    skip_button.click()