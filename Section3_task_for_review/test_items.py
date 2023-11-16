import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	
def test_should_see_btn_add( browser):
	browser.get(link)
	time.sleep(2)
	btn_add = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
	assert btn_add, "Button not found"
	