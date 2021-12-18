# Shopify Automation Script

A web automation script to automate creating a Shopify account; creating a Shopify Store; adding & removing Shopify Applications to the store. 

Written in Python with the Selenium library, runs on the Chrome webdriver.

## Features:

- Create a Shopify account
- Create a Shopify Store
- Add Shopify Applications to Shopify Store
- Remove Shopify Applications from Shopify Store

## Installation:

1. Install the latest stable version of [Google Chrome](https://www.google.com/chrome/).

2. Install the latest stable version of [Python3](https://www.python.org/downloads/)

3. Install [Git](https://git-scm.com/downloads)

4. Clone and `cd` into the repository

```
git clone https://github.com/PythonBay/Shopify_Automation_Script
cd Shopify_Automation_Script
```

5. Install the dependencies using `pip`

```
pip install -r requirements.txt
```

6. Modify the `.env` file and add your 2captcha API key (turn 100% recognition on)

```
API_KEY = "ENTER_2CAPTCHA_API_KEY_HERE"
```

## Usage

The script will create a new shopify account and store and then add the specified shopify apps before deleting them.

The URL to the shopify apps that will be added can be specified in a text file. (`shopify_apps.txt`)

The script can be run like this:

Parameters:

```
python3 main.py [file path to shopify apps url list] [number of times to run automation]
```

Example Usage:

```
python3 main.py shopify_apps.txt 2
```

The command above will run the automation for 2 times with the `shopify_apps.txt` file.

The `shopify_apps.txt` file is a list of shopify app URLs which will be added to the generated user accounts.

Example `shopify_apps.txt` file

```
https://apps.shopify.com/cooki-gdpr
https://apps.shopify.com/facebook
https://apps.shopify.com/awtomatic
```