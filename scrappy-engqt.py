import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

def init_driver():
    driver = webdriver.PhantomJS()
    # driver = webdriver.Firefox()
    # driver.wait = WebDriverWait(  driver, 5)
    return driver


def lookup(driver):
    driver.get("http://enqt.de/m7Ey9JxAg1jf9zb9/index.php")
    try:
        print('Searching Speichern&Messung button begin')
        button = driver.wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "body > div > div.content.content--messparameter > form > div.buttons.text-center > button")))
        print('Searching Speichern&Messung button done')
        button.click()

        print('Searching Messung starten button begin')
        button = driver.wait.until(EC.element_to_be_clickable(
        (By.ID, "messung-starten")))
        print('Searching Messung starten button done')
        button.click()

        time.sleep(10)

        print('Searching Messung stop button begin')
        button = driver.wait.until(EC.element_to_be_clickable(
        (By.ID, "messung-stoppen")))
        print('Searching Messung stop button done')
        button.click()

        print('Searching Ergebnisse stop button begin')
        button = driver.wait.until(EC.element_to_be_clickable(
        (By.ID, "results")))
        print('Searching Ergebnisse stop button done')
        button.click()

        print('Searching Messdatn herunterladen button begin')
        button = driver.wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".buttons > a:nth-child(1)")))
        print('Searching Messdatn herunterladen button done')
        button.click()

    except TimeoutException:
        print("Box or Button not found in google.com")


if __name__ == "__main__":
    driver = init_driver()
    print('Begin scrapping')
    lookup(driver)
    print('Scrapping done')
    # time.sleep(5)
    # driver.quit()

unittest.main()
