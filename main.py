from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

def get_options():
    options = ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("window-size=1400,1500")
    return options

def main(cycles, api_key, shopify_apps):
    options = get_options()
    service = Service(ChromeDriverManager().install())
    print("")
    for i in range(cycles):
        driver = webdriver.Chrome(service = service, options = options)
        print("Starting cycle #" + str(i + 1))
        try:
            run_service(driver, api_key, shopify_apps)
            print("Finished cycle #" + str(i + 1))
        except Exception as e:
            print(e)
            continue
        finally:
            print("")

def standard_flow(driver, shopify_apps):
    automation.account_creation_1.main(driver)
    automation.account_creation_2.main(driver)

    WebDriverWait(driver, 200).until(lambda driver: driver.current_url.endswith("admin"))
    admin_url = driver.current_url

    for shopify_app in shopify_apps:
        automation.app_page.main(driver, shopify_app)
        
        WebDriverWait(driver, 200).until(lambda driver: "apps" not in driver.current_url)
        if("choose" in driver.current_url or True):
            automation.login_intercept.main(driver)
        automation.app_authorization.main(driver)
        
        driver.get(admin_url + "/apps")
        automation.delete_app.main(driver)

def captcha_flow(driver, api_key):
    automation.alternate_sign_up_form.main(driver, api_key)
    WebDriverWait(driver, 200).until(lambda driver: driver.current_url.endswith("/admin/account_setup"))

import automation

def run_service(driver, api_key, shopify_apps):
    automation.home_page.main(driver)
    automation.sign_up_form.main(driver)
    WebDriverWait(driver, 200).until(lambda driver: driver.current_url != "https://www.shopify.com/")
    if(driver.current_url != "https://accounts.shopify.com/store-signup/setup"):
        captcha_flow(driver, api_key)
    standard_flow(driver, shopify_apps)