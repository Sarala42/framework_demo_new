from datetime import datetime
from config import Config


def capture_screenshot(driver, testcase_name):
	str_format = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
	driver.save_screenshot(Config.screenshot_path + f"{testcase_name}_{str_format}.png")