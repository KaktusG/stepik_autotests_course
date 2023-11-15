from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestForm(unittest.TestCase):
	def test_for_Page_reg1(self):
		link = "https://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element(By.XPATH, "//div[@class='first_block']/div/input[@class='form-control first']")
		input1.send_keys("FName")
		input2 = browser.find_element(By.XPATH, "//div[@class='first_block']/div/input[@class='form-control second']")
		input2.send_keys("SName")
		input3 = browser.find_element(By.XPATH, "//div[@class='first_block']/div/input[@class='form-control third']")
		input3.send_keys("Email")
	
		#Отправляем заполненную форму
		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()
		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)
	
		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Text not found")
	
	def test_for_Page_reg2(self):
		link = "https://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element(By.XPATH, "//div[@class='first_block']/div/input[@class='form-control first']")
		input1.send_keys("FName")
		input2 = browser.find_element(By.XPATH, "//div[@class='first_block']/div/input[@class='form-control second']")
		input2.send_keys("SName")
		input3 = browser.find_element(By.XPATH, "//div[@class='first_block']/div/input[@class='form-control third']")
		input3.send_keys("Email")
	
		#Отправляем заполненную форму
		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()
		# Проверяем, что смогли зарегистрироваться
		# ждем загрузки страницы
		time.sleep(1)
	
		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

		# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Text not found")

if __name__ == "__main__":
	unittest.main()
	