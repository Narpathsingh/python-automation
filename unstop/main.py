from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_experimental_option('detach', True)

driver = webdriver.Chrome(chromeoptions)


driver.get('https://unstop.com/auth/login')
time.sleep(10)

# submit email
emailvalue = driver.find_element(By.NAME, value='email')
# insert value
# dummy mail to login = ksswccldetxdegklhe@ytnhy.com
emailvalue.send_keys('ksswccldetxdegklhe@ytnhy.com')
# print(emailvalue)
# password field
passvalue = driver.find_element(By.NAME, value='password')
passvalue.send_keys('Bangalore@098')
# print(passvalue.text)
# print(passvalue)
# submit button

button = driver.find_element(By.CSS_SELECTOR, value='.submit_btn')
button.click()

# goto job portal
jobportal = driver.get('https://unstop.com/job-portal')
time.sleep(5)
post = driver.find_element(By.CSS_SELECTOR, value='.waves-effect')
post.click()
print(post.text)


# login

# driveclick = driver.find_element(By.CSS_SELECTOR, value='.ng-star-inserted div')
# driveclick.click()
# before quit
# waittime = time.sleep(10)
# to accept cookie

# cookie = driver.find_element(By.CSS_SELECTOR, value='.GTM_ACCEPT_COOKIE')
# print(cookie)

# driver.quit()

