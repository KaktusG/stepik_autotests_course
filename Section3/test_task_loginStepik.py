import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "https://stepik.org/lesson/236895/step/1"

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestLogin():
	def test_login(self, browser, links):
		browser.get(links)
		time.sleep(3)
		login_btn = browser.find_element(By.CLASS_NAME, "navbar__auth_login")
		login_btn.click()
		email_input = browser.find_element(By.NAME, "login")
		email_input.send_keys("ya.ekaterina.g@gmail.com")
		password_input = browser.find_element(By.NAME, "password")
		password_input.send_keys("StepikKatyaCource")
		btn_signin = browser.find_element(By.CLASS_NAME, "sign-form__btn")
		btn_signin.click()
		time.sleep(5)
		
		#WebDriverWait(browser, 5).until(
		#	EC.visibility_of_element_located((By.CLASS_NAME, "again-btn"))
		#).click()
		
		answer_field = browser.find_element(By.CLASS_NAME, "string-quiz__textarea")
		answer_field.clear()
		answer = math.log(int(time.time()))
		print("/nanswer=", answer)
		answer_field.send_keys(answer)
		btn_send = WebDriverWait(browser, 5).until(
			EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
		)
		btn_send.click()
		time.sleep(3)
		message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
		print ("\n Text=", message.text)
	
	
	
	
	
	
	
	