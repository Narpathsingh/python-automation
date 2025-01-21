from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chromeoptions)
driver.get('https://secure-retreat-92358.herokuapp.com/')

firstname = driver.find_element(By.NAME, value='fName')
lastname = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')
button = driver.find_element(By.CSS_SELECTOR, value='.btn')

firstname.send_keys('Ravi')
lastname.send_keys('singh')
email.send_keys('ravisingh@gmail.com')
button.send_keys(Keys.ENTER)


