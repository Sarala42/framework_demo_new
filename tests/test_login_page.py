# test cases related to login module
# test cases related to login module
# imports -> inbuilt module, installed libraries, local modules
import email

import password
import pytest
from config import Config
from selenium.common.exceptions import NoSuchElementException
from src.login_page import LoginPage, driver
from utilities.excel_lib import read_locators
from utilities.selenium_wrapper import capture_screenshot

# def test_login_with_valid_credentials():
# 	lp = LoginPage()

credentials = [
	("steve_jobs@gmail.com", "steve123"),
	("abc@gmail.com", "abc123"),
	("", "steve123"), ("steve_jobs@gmail.com", ""),
	(" ", " ")]

# parametrize the test case
# def test_login_with_valid_credentials(driver_init):
@pytest.mark.parametrize("email, password", credentials)
def test_login(driver_init, email, password):
	driver = driver_init
	try:
		lp = LoginPage(driver)
		lp.login(email, password)
		result = lp.is_user_logged_in()
		assert result, "Invalid user"
		print("user logged in successfully")
		lp.logout()

	except Exception as error:
		capture_screenshot(driver, "test_login")
		print(f"test case failed due to {error}")
		raise error

# 	lp = LoginPage(driver)
# 	lp.login("steve_jobs@gmail.com", "steve123")
# 	result = lp.is_user_logged_in()
# 	assert result, "Invalid user"
# 	print("user logged in successfully")
# 	lp.logout()
#
#
# def test_login_with_invalid_credentials(driver_init):
# 	lp = LoginPage(driver_init)
# 	lp.login("abc@gmail.com", "abc123")
# 	result = lp.is_user_logged_in()
# 	assert result, "Invalid user"
# 	print("user logged in successfully")
# 	lp.logout()



# def test_login_with_valid_credentials(driver_init):
# 	driver = driver_init
# 	lp = LoginPage(driver)
# 	lp.login("steve_jobs@gmail.com", "steve123")
# 	result = lp.is_user_logged_in()
# 	assert result, "Invalid user"
# 	print("user logged in successfully")
# 	lp.logout()


# def test_login_with_invalid_credentials(driver_init):
# 	lp = LoginPage(driver_init)
# 	lp.login("abc@gmail.com", "abc123")
# 	result = lp.is_user_logged_in()
# 	assert result, "Invalid user"
# 	print("user logged in successfully")
# 	lp.logout()


# test login with blank email and some password
# test login with blank email and password