from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main(driver):
    WebDriverWait(driver, 200).until(EC.title_contains("Authorize"))
    install_app_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ui-button.ui-button--primary")))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    install_app_button.click()