from selenium import webdriver
driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
driver.get("http://google.com")
driver.implicitly_wait(15)
driver.get_screenshot_as_file("c10.png")
