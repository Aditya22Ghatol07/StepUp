import sys
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
driver=webdriver.Chrome()

abc=driver.get("https://www.nopcommerce.com/en/register?returnUrl=%2Fen%2Fget-started")
driver.maximize_window()
driver.find_element(By.ID,"FirstName").send_keys('hi')
time.sleep(10)
driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys('hi')
time.sleep(5)
act= "Register - nopCommere"
#print(driver.title)







