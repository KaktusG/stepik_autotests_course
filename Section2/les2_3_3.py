from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math
import os

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	browser.find_element(By.TAG_NAME, "button").click()
	alert = browser.switch_to.alert
	alert.accept()
	x =  browser.find_element(By.ID, "input_value").text
	input = browser.find_element(By.ID, "answer")
	input.send_keys(calc(x))
	browser.find_element(By.TAG_NAME, "button").click()
	
finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла