import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/")
# assert "Python" in driver.title
search_bar = driver.find_element(By.ID, "search2")
search_bar.send_keys(f"python{Keys.RETURN}")
driver.find_element(By.ID, "accept-choices").click()
time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, ".w3-right.w3-btn").click()
# time.sleep(5)
driver.close()
