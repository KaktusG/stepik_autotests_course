from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	el_x = browser.find_element(By.ID, "input_value")
	x = el_x.text
	y = calc(x)
	#ввод значения y в поле ввода
	input = browser.find_element(By.ID, "answer")
	input.send_keys(y)
	#выбор чекбокса
	checkbx = browser.find_element(By.ID, "robotCheckbox")
	checkbx.click()
	#выбор радиобаттона
	radiobtn = browser.find_element(By.ID, "robotsRule")
	#radiobtn.click()
	people_checked = radiobtn.get_attribute("checked")
	print("value of people radio: ", people_checked)
	assert people_checked is not None, "People radio is not selected by default"
	
	#клик на кнопку
	#btn = browser.find_element(By.TAG_NAME, "button")
	#btn.click()	

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла