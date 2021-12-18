from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main(driver, shopify_app_url):
    driver.get(shopify_app_url)
    add_app_button = WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".marketing-button.ui-app-store-hero__cta-button")))
    add_app_button.click()