import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser():
	print("\n start browser for test...")
	browser = webdriver.Chrome()
	yield browser
	# этот код выполнится после завершения теста
	print("\n quit browser")
	return browser

@pytest.fixture(autouse=True)
def prepare_data():
	print()
	print("preparing some critical data for every test")


class TestMainPage1():
	#вызываем фикстуру в тесте, передав ее как параметр
	def test_guest_should_see_login_link(self, browser):
		# не передаём как параметр фикстуру prepare_data, но она все равно выполняется		
		browser.get(link)
		browser.find_element(By.CSS_SELECTOR, "#login_link")
	
	def test_guest_should_see_basket_link_on_the_main_page(self, browser):
		browser.get(link)
		browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

