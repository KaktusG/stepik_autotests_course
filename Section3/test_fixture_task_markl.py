import pytest

class TestMainPage():
    # номер 1
	@pytest.mark.xfail
	@pytest.mark.smoke
	def test_guest_can_login(self):
		print("\n task 1")
		assert True
	
	# номер 2
	@pytest.mark.regression
	def test_guest_can_add_book_from_catalog_to_basket(self):
		print("\n task 2")
		assert True


class TestBasket():
	# номер 3
	@pytest.mark.skip(reason="not implemented yet")
	@pytest.mark.smoke
	def test_guest_can_go_to_payment_page(self):
		print("\n task 3")
		assert True

    # номер 4
	@pytest.mark.smoke
	def test_guest_can_see_total_price(self):
		print("\n task 4")
		assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
	@pytest.mark.smoke
	def test_guest_can_add_book_to_basket(self):
		print("\n task 5")
		assert True

    # номер 6
	@pytest.mark.regression
	def test_guest_can_see_book_price(self):
		print("\n task 6")
		assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
	print("\n task 7")
	assert True
	