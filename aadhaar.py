from selenium import webdriver from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
start_url = "https://duckgo.com"
driver.get(start_url)
print(driver.page_source.encode("utf-8"))
driver.quit()






# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# import time
# import captcha
# CHROME_PATH = '/usr/bin/google-chrome-stable'
# CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
# WINDOW_SIZE = "1920,1080"

# uid_no = '541789209718'
# getcaptcha = captcha.GetCaptcha()
# # chrome_options = Options()  
# # chrome_options.add_argument("--headless")  
# # chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--proxy-server='direct://'")
# chrome_options.add_argument("--proxy-bypass-list=*")
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--allow-running-insecure-content')
# chrome_options.binary_location = CHROME_PATH

# driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
#                           chrome_options=chrome_options
#                          )  
# print('Driver',driver)
# driver.get("https://resident.uidai.gov.in/verify")
# driver.implicitly_wait(10)
# driver.get_screenshot_as_file("capture1.png")
# uid = driver.find_element_by_id("uidno")
# getcaptcha.download_captcha(driver)
# captcha_text = getcaptcha.get_captcha_text()
# captcha = driver.find_element_by_xpath('//*[@id="security_code"]')

# uid.send_keys(uid_no)
# captcha.send_keys(captcha_text)

# driver.implicitly_wait(5)
# driver.find_element_by_xpath('//*[@id="submitButton"]').click()

# elements = driver.find_element_by_xpath('//*[@id="maincontent"]/div/div[1]/div[3]')
# print(elements.text)

















# driver.get("https://www.google.com")
# driver.get_screenshot_as_file("capture.png")
# driver.close()













# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# import time
# import captcha


# uid_no = '541789209718'
# getcaptcha = captcha.GetCaptcha()
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
# driver.get("https://resident.uidai.gov.in/verify")
# driver.implicitly_wait(20)
# uid = driver.find_element_by_xpath('//*[@id="uidno"]')
# getcaptcha.download_captcha(driver)
# captcha_text = getcaptcha.get_captcha_text()
# captcha = driver.find_element_by_xpath('//*[@id="security_code"]')

# uid.send_keys(uid_no)
# captcha.send_keys(captcha_text)

# driver.implicitly_wait(5)
# driver.find_element_by_xpath('//*[@id="submitButton"]').click()

# elements = driver.find_element_by_xpath('//*[@id="maincontent"]/div/div[1]/div[3]')
# print(elements.text)


