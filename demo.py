from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://demowebshop.tricentis.com/")

driver.find_element("link text", "Log in").click()
driver.save_screenshot("ss1.png")
driver.close()


"""
driver.get_screenshot_as_file(file.png)
driver.get_screenshot_as_base64() -> bytecode
driver.get_screenshot_as_png() -> bytecode
"""