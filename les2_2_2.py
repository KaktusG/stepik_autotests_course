from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/selects1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	num1 = browser.find_element(By.ID, "num1").text
	num2 = browser.find_element(By.ID, "num2").text
	sum = str(sum((int(num1),int(num2))))
	print("sum: ", sum)
	dropdwn = Select(browser.find_element(By.ID, "dropdown"))
	dropdwn.select_by_value(sum)
	browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла