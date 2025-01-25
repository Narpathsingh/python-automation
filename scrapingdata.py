from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_experimental_option('detach',True)

driver = webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/Main_Page')

# searching throught css slector, 2nd element in the list

# Eventrecord = driver.find_element(By.CSS_SELECTOR, value='#articlecount li:nth-child(2) a')
# print(Eventrecord)

# click the link
# clickrecord = Eventrecord.click()

# another method to click
# clickbymethod = driver.find_element(By.LINK_TEXT, value='Content portals')
# clickbymethod.click()

# send or type keys in search box

search = driver.find_element(By.NAME, value='search')
search.send_keys('python',Keys.ENTER)

# search.send_keys('python')
# # import keys class to tap in any keyboard keys


driver.quit()
