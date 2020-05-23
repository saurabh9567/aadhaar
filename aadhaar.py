from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import captcha


uid_no = '541789209718'
getcaptcha = captcha.GetCaptcha()
options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
driver.get("https://resident.uidai.gov.in/verify")
driver.implicitly_wait(20)
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
# for element in elements:
#     print(element.text)
#     # print element.get_attribute('data-value')






# driver.find_element_by_xpath('/html/body/nav/a[3]').click()         

# un = driver.find_element_by_xpath('//*[@id="username"]')
# pw = driver.find_element_by_xpath('//*[@id="password"]')

# un.send_keys('saurabhverma956@gmail.com')
# pw.send_keys()

# driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[4]/button').click()

