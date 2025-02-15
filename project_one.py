from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Reach the site
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

title = driver.find_elements(By.CLASS_NAME, value="shrubbery")
menu = title[1].find_elements(By.TAG_NAME, value="a")
date_tag = title[1].find_elements(By.TAG_NAME, value="time")
dates = [x.text for x in date_tag]
title_at = [x.text for x in menu]
final_challenge = {}
cont = 0
for date in dates:
    final_challenge.update({cont: {"time": date, "name": title_at[cont+1]}})
    cont += 1

print(final_challenge)

