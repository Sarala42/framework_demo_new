import pytest
from selenium import webdriver
from config import Config


@pytest.fixture
def driver_init():
	browser = Config.browser

	if browser.lower() == "chrome":
		c_options = webdriver.ChromeOptions()
		c_options.add_experimental_option("detach", True)
		driver = webdriver.Chrome(options=c_options)

	elif browser.lower() == "firefox":
		driver = webdriver.Firefox()

	else:
		driver = webdriver.Edge()

	driver.get(Config.url)
	driver.maximize_window()
	# driver.implicitly_wait(10)
	driver.implicitly_wait(5)

	yield driver

	driver.close()