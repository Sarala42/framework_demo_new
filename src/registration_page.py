from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from utilities.excel_lib import read_locators
from config import Config

c_options = webdriver.ChromeOptions()
c_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=c_options)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)

class RegistrationPage:
	pass
	locators = read_locators(Config.locators_path, Config.reg_obj_sheet)

	def __init__(self, driver):
		self.driver = driver

	def register(self):
		self.driver.find_element(*self.locators["register_link"]).click()
		self.driver.find_element(*self.locators["male_rdo_btn"]).click()
		self.driver.find_element(*self.locators["firstname_txt"]).send_keys("tom")
		self.driver.find_element(*self.locators["lastname_txt"]).send_keys("cruise")
		self.driver.find_element(*self.locators["email_txt"]).send_keys("tomcruise123@yahoo.com")
		self.driver.find_element(*self.locators["password_txt"]).send_keys("tom123")
		self.driver.find_element(*self.locators["confirm_pwd_txt"]).send_keys("tom123")
		self.driver.find_element(*self.locators["register_btn"]).click()

	def is_user_registered(self):
		try:
			self.driver.find_element(*self.locators["result_txt"])
			return True

		except NoSuchElementException:
			return False

	def is_user_already_exists(self):
		try:
			self.driver.find_element(*self.locators["user_exists_txt"])
			return False

		except NoSuchElementException:
			return True