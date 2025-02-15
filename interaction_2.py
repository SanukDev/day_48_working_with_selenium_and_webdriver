from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ---
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# ---
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# ---
box_first_name = driver.find_element(By.NAME, value="fName")
box_last_name = driver.find_element(By.NAME, value="lName")
box_email = driver.find_element(By.NAME, value="email")

# ---
box_first_name.send_keys("Samuel", Keys.ENTER)
box_last_name.send_keys("Melo", Keys.ENTER)
box_email.send_keys("smelo@panacopy.com.br", Keys.ENTER)
