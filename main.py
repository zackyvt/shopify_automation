from sys import modules
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

import os
from dotenv import load_dotenv

def get_options():
    options = ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("window-size=1400,1500")
    return options

def main(cycles):
    options = get_options()
    service = Service(ChromeDriverManager().install())
    print("")
    for i in range(cycles):
        driver = webdriver.Chrome(service = service, options = options)
        print("Starting cycle #" + str(i + 1))
        try:
            run_service(driver)
            print("Finished cycle #" + str(i + 1))
        except Exception as e:
            print(e)
            continue
        finally:
            print("")

shopify_apps = []

def import_shopify_apps(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def standard_flow(driver):
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

def captcha_flow(driver):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    automation.alternate_sign_up_form.main(driver, api_key)
    WebDriverWait(driver, 200).until(lambda driver: driver.current_url.endswith("/admin/account_setup"))

import automation

def run_service(driver):
    automation.home_page.main(driver)
    automation.sign_up_form.main(driver)
    WebDriverWait(driver, 200).until(lambda driver: driver.current_url != "https://www.shopify.com/")
    if(driver.current_url != "https://accounts.shopify.com/store-signup/setup"):
        captcha_flow(driver)
    standard_flow(driver)

import sys

if __name__ == "__main__":
    shopify_apps = import_shopify_apps(sys.argv[1])
    print("Running for " + sys.argv[2] + " cycles on file " + sys.argv[1])
    main(int(sys.argv[2]))