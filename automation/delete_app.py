from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main(driver):
    delete_app_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Polaris-Button_r99lw.Polaris-Button--destructive_zy6o5.Polaris-Button--plain_2z97r")))
    delete_app_button.click()

    delete_app_confirmation = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Polaris-Button_r99lw.Polaris-Button--primary_7k9zs.Polaris-Button--destructive_zy6o5")))
    delete_app_confirmation.click()

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Polaris-Banner_z4w8k.Polaris-Banner--statusSuccess_pc5rl.Polaris-Banner--withinPage_kguwn")))