from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math
import os

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	browser.find_element(By.NAME, "firstname").send_keys("Inan")
	browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
	browser.find_element(By.NAME, "email").send_keys("mail@mail.com")
	btn_upload = browser.find_element(By.ID, "file")
	current_dir = os.path.abspath(os.path.dirname(__file__))
	print(current_dir)
	print(os.path.abspath(__file__))
	file_path = os.path.join(current_dir, 'file.txt')
	btn_upload.send_keys(file_path)
	browser.find_element(By.TAG_NAME, "button").click()
	
finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла