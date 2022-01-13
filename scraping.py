"""
This is the core of the project, this is the scraping part

This bot uses Selenium as i could not manage to use requests
"""

# libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as K
from selenium.webdriver.chrome.service import Service
import os
import time as tm


# local files
import config


# parametres
WAIT_TIME = config.WAIT_TIME


def initialise_scraping(download_location):
    """
    This function initialise the driver with all necessary options
    """

    # suppression des affichages de webdriver-manager
    os.environ["WDM_LOG_LEVEL"] = "0"
    os.environ["WDM_PRINT_FIRST_LINE"] = "False"

    # initialisation du driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    prefs = {
        "download.default_directory": download_location,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        "safebrowsing.disable_download_protection": True,
    }

    options.add_experimental_option("prefs", prefs)
    options.add_argument("headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )  # maybe shoud i've call it driver

    return browser


def connect_to_bigfoot(browser):
    """
    This function connects user to bigfoot
    """

    try:
        browser.get("https://bigfoot.ensta.fr/")
        tm.sleep(WAIT_TIME)
        browser.find_elements(By.CSS_SELECTOR, "button.pa-5")[0].click()

        tm.sleep(WAIT_TIME)
        browser.find_elements(By.CSS_SELECTOR, "input#username")[0].send_keys(
            config.username
        )
        browser.find_elements(By.CSS_SELECTOR, "input#password")[0].send_keys(
            config.password, K.ENTER
        )
        tm.sleep(WAIT_TIME)
        return True

    except Exception as e:
        print(
            "An error occured while connecting to bigfoot.\n",
            "Please verify your username and password or increase 'WAIT_TIME'",
        )
        # print(e)
        return False


def download_movie(browser, title):
    """
    This function is aimed to download a movie thanks to its title

    If the film is not on bigfoot it will return False and show the bigfoot proposition.
    This will allow to handle typos
    Else it will return True and the films infos
    """

    assert type(title) == str

    try:
        # fake search
        search = browser.find_elements(By.CSS_SELECTOR, "input")[0]
        search.send_keys(" ")
        tm.sleep(1.5 * WAIT_TIME)
        search.send_keys(K.ENTER)
        tm.sleep(WAIT_TIME)

        # clear previous serach
        button = browser.find_elements(
            By.CSS_SELECTOR,
            "button.v-icon.notranslate.v-icon--link.mdi.mdi-close",
        )[0]
        button.click()

        # real search
        search = browser.find_elements(By.CSS_SELECTOR, "input")[2]
        search.send_keys(title)
        tm.sleep(1.5 * WAIT_TIME)
        search.send_keys(K.ENTER)
        tm.sleep(WAIT_TIME)

        # extract element from table
        table = browser.find_elements(By.CSS_SELECTOR, "table")[0]
        data = table.text.split("\n")
        results = [
            {"Title": data[k], "Type": data[k + 1], "Year": data[k + 2][:4]}
            for k in range(5, len(data), 3)
        ]
        others = [elem["Title"] for elem in results if elem["Type"] == "Film"]
        tm.sleep(WAIT_TIME)

        # go through table
        found = False
        for k, res in enumerate(results):
            if res["Title"].lower() == title.lower() and res["Type"] == "Film":
                browser.find_elements(By.CSS_SELECTOR, "tr.clickable")[k].click()
                found = True
                break

        if not found:
            return False, others

        # download
        else:
            tm.sleep(WAIT_TIME)
            browser.find_elements(By.CSS_SELECTOR, "button.v-btn")[3].click()
            tm.sleep(2 * WAIT_TIME)
            return True, res

    except Exception as e:
        print(
            f"An error occured while scraping for {title}. Try to increase 'WAIT_TIME'"
        )
        # print(e)
        return None


if __name__ == "__main__":
    pass
