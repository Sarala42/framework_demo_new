# automation script
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from utilities.excel_lib import read_locators

c_options = webdriver.ChromeOptions()
c_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=c_options)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)

locators_path = r"C:\Users\saral\PycharmProjects\framework_demo_new\file_data\Locators.xlsx"
from config import Config

# class LoginPage:
#
# 	def click_login_link(self):
# 		driver.find_element("link text", "Log in").click()
#
# 	def enter_email(self):
# 		driver.find_element("id", "Email").send_keys("abc@gmail.com")
#
# 	def enter_password(self):
# 		driver.find_element("id", "Password").send_keys("abc123")
#
# 	def click_remember_me(self):
# 		driver.find_element("id", "RememberMe").click()
#
# 	def click_login_btn(self):
# 		driver.find_element("xpath", '//input[@value="Log in"]').click()


class LoginPage:
	# locators = read_locators(locators_path, "login_objects")
	locators = read_locators(Config.locators_path, Config.login_obj_sheet)

	def __init__(self, driver):
		self.driver = driver

	def login(self, email, password):
		# driver.find_element("link text", "Log in").click()
		# driver.find_element("id", "Email").send_keys(email)
		# driver.find_element("id", "Password").send_keys(password)
		# driver.find_element("id", "RememberMe").click()
		# driver.find_element("xpath", '//input[@value="Log in"]').click()
		# driver.find_element(*self.locators["login_link"]).click()
		# driver.find_element(*self.locators["email_txt"]).send_keys(email)
		# driver.find_element(*self.locators["password_txt"]).send_keys(password)
		# driver.find_element(*self.locators["remember_checkbox"]).click()
		# driver.find_element(*self.locators["login_btn"]).click()
		self.driver.find_element(*self.locators["login_link"]).click()
		self.driver.find_element(*self.locators["email_txt"]).send_keys(email)
		self.driver.find_element(*self.locators["password_txt"]).send_keys(password)
		self.driver.find_element(*self.locators["remember_checkbox"]).click()
		self.driver.find_element(*self.locators["login_btn"]).click()

	def is_user_logged_in(self):
		try:
			# driver.find_element("link text", 'Log out')
			# driver.find_element(*self.locators["logout_link"])
			self.driver.find_element(*self.locators["logout_link"])
			# print("user logged in successfully")
			return True

		except NoSuchElementException as error:
			# print("Invalid user")
			return False

	def logout(self):
		# driver.find_element("link text", 'Log out').click()
		# driver.find_element(*self.locators["logout_link"]).click()
		self.driver.find_element(*self.locators["logout_link"]).click()


# lp = LoginPage()
# lp.login()
# lp.is_user_logged_in()
# driver.close()