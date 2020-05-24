from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import captcha
CHROME_PATH = '/usr/bin/google-chrome-stable'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

uid_no = '541789209718'
getcaptcha = captcha.GetCaptcha()
chromeOptions = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chromeOptions.add_argument("--test-type");
# chromeOptions.add_argument("--disable-gpu");
# chromeOptions.add_argument("--no-first-run");
# chromeOptions.add_argument("--no-default-browser-check");
# chromeOptions.add_argument("--ignore-certificate-errors");
# chromeOptions.add_argument("--start-maximized");
chromeOptions.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                         )  

driver.get("https://resident.uidai.gov.in/verify")
driver.implicitly_wait(10)
uid = driver.find_element_by_xpath('//*[@id="uidno"]')
getcaptcha.download_captcha(driver)
captcha_text = getcaptcha.get_captcha_text()
captcha = driver.find_element_by_xpath('//*[@id="security_code"]')

uid.send_keys(uid_no)
captcha.send_keys(captcha_text)

driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="submitButton"]').click()

elements = driver.find_element_by_xpath('//*[@id="maincontent"]/div/div[1]/div[3]')
print(elements.text)

















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


