from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class Collector:

    def __init__(self, driver):
        self.cursor = 0
        self.click_cursor = None
        self.money = 0
        self.grandma = 0
        self.click_grandma = None
        self.factory = 0
        self.click_factory = None
        self.mine = 0
        self.click_mine = None
        self.shipment = 0
        self.click_shipment = None
        self.value_cursor(driver)
        self.value_grandma(driver)
        self.value_factory(driver)
        self.value_money(driver)
        self.value_mine(driver)
        self.value_shipment(driver)

    def value_money(self, driver):
        money_teste = driver.find_element(By.ID, value="money")
        money = money_teste.text
        mm = money.split(",")
        self.money = "".join(mm)
        return int(self.money)

    def value_cursor(self, driver):
        value_cursor = driver.find_element(By.ID, value="buyCursor")
        cursor_teste = value_cursor.text.split()
        self.click_cursor = value_cursor
        cursor_c = cursor_teste[2]
        cursor = cursor_c.split(",")
        self.cursor = "".join(cursor)
        return int(self.cursor)

    def value_grandma(self, driver):
        value_grandma = driver.find_element(By.ID, value="buyGrandma")
        grandma_teste = value_grandma.text.split()
        self.click_grandma = value_grandma
        grandma = grandma_teste[2]
        gran = grandma.split(",")
        self.grandma = "".join(gran)

        return int(self.grandma)

    def value_factory(self, driver):
        value_factory = driver.find_element(By.ID, value="buyFactory")
        factory_teste = value_factory.text.split()
        factory = factory_teste[2]
        fac = factory.split(",")
        self.factory = "".join(fac)
        self.click_factory = value_factory
        return int(self.factory)

    def value_mine(self, driver):
        value_mine = driver.find_element(By.ID, value="buyMine")
        mine_teste = value_mine.text.split()
        self.click_mine = value_mine
        mine = mine_teste[2]
        mine_s = mine.split(",")
        self.mine = "".join(mine_s)
        return int(self.mine)

    def value_shipment(self, driver):
        value_shipment = driver.find_element(By.ID, value="buyShipment")
        shipment_teste = value_shipment.text.split()
        self.click_shipment = value_shipment
        shipment = shipment_teste[2]
        ship_s = shipment.split(",")
        self.shipment = "".join(ship_s)
        return int(self.shipment)
