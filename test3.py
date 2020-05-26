from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://nytimes.com')
print(driver.title)









# from selenium import webdriver
# driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
# driver.get("http://google.com")
# driver.implicitly_wait(15)
# driver.get_screenshot_as_file("c10.png")
