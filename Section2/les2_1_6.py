from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	pic = browser.find_element(By.ID, "treasure")
	el_x = pic.get_attribute("valuex")
	print("value x: ", el_x)
	y = calc(el_x)
	#ввод значения y в поле ввода
	input = browser.find_element(By.ID, "answer")
	input.send_keys(y)
	#выбор чекбокса
	checkbx = browser.find_element(By.ID, "robotCheckbox")
	checkbx.click()
	#выбор радиобаттона
	radiobtn = browser.find_element(By.ID, "robotsRule")
	radiobtn.click()
	#клик на кнопку
	btn = browser.find_element(By.TAG_NAME, "button")
	btn.click()	

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла