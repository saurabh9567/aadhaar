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
chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                         )  
print('Driver',driver)
driver.get("https://resident.uidai.gov.in/")
driver.implicitly_wait(15)
print('reaced at udemy')
driver.get_screenshot_as_file("c5.png")
# driver.get("https://resident.uidai.gov.in/verify")
# driver.implicitly_wait(15)
# driver.get_screenshot_as_file("c2.png")
# print('reached here')
# uid = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/div[4]/div/div/div[2]/div/div/form/div[1]/div/div[1]/input").click()
# print('uid',uid)
# driver.implicitly_wait(5)
# getcaptcha.download_captcha(driver)
# captcha_text = getcaptcha.get_captcha_text()
# captcha = driver.find_element_by_xpath('//*[@id="security_code"]')
# uid.send_keys(uid_no)
# captcha.send_keys(captcha_text)

# driver.implicitly_wait(5)
# driver.find_element_by_xpath('//*[@id="submitButton"]').click()

# elements = driver.find_element_by_xpath('//*[@id="maincontent"]/div/div[1]/div[3]')
# print(elements.text)
