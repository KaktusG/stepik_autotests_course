from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math
import os

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	x = browser.find_element(By.ID, "input_value").text
	input = browser.find_element(By.ID, "answer")
	input.send_keys(calc(x))
	checkbx = browser.find_element(By.ID, "robotCheckbox")
	browser.execute_script("return arguments[0].scrollIntoView(true);", checkbx)
	checkbx.click()
	radiobtn = browser.find_element(By.ID, "robotsRule")
	radiobtn.click()
	button = browser.find_element(By.TAG_NAME, "button")
	button.click()
	
	current_dir = os.path.abspath(os.path.dirname(__file__))
	print(current_dir)
	print(os.path.abspath(__file__))
	file_path = os.path.join(current_dir, 'file.txt')

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла