from selenium import webdriver
from selenium.webdriver.common.by import By
from collector import Collector
import datetime

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

coll = Collector(driver)
# ---
big_cookie = driver.find_element(By.ID, value="cookie")

# Money ---
# Cursor -----
# Grandma ----
# Factory ----
# Mine ----
# Shipment ----

while True:
    big_cookie.click()

    money = coll.value_money(driver)
    cursor = coll.value_cursor(driver)
    grandma = coll.value_grandma(driver)
    factory = coll.value_factory(driver)
    mine = coll.value_mine(driver)
    shipment = coll.value_shipment(driver)

    if money > 0:
        if mine > (shipment / 2):
            coll.click_shipment.click()
        elif factory > (mine / 3):
            coll.click_mine.click()
        elif grandma > (factory / 3):
            coll.click_factory.click()
        elif cursor > (grandma / 3) or money == grandma:
            coll.click_grandma.click()
        else:
            coll.click_cursor.click()


