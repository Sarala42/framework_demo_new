from src.registration_page import RegistrationPage
from utilities.selenium_wrapper import capture_screenshot

def test_register(driver_init):
	# rp = RegistrationPage(driver_init)
	# rp.register()
	# result = rp.is_user_registered()
	# assert result, "user registration is not successful"

	# exists = rp.is_user_already_exists()
	# assert exists, "user already exists"
	driver = driver_init
	try:
		rp = RegistrationPage(driver)
		rp.register()
		result = rp.is_user_registered()
		assert result, "user registration is not successful"

		# exists = rp.is_user_already_exists()
		# assert exists, "user already exists"

	except Exception as error:
		capture_screenshot(driver, "test_register")
		print(f"test case failed due to {error}")
		raise error