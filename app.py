from selenium import webdriver
from selenium.webdriver.common.by import By

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chromeoptions)
# driver.get('https://www.flipkart.com/tvs-and-appliances-new-clp-store?fm=neo%2Fmerchandising&iid=M_9de8518e-2609-4c91-8c6c-fa1e59ca6a87_1_VMDN1VE1AUK9_MC.8TVKUWT87M16&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_TVs%2B%26%2BAppliances_8TVKUWT87M16&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L0_view-all&cid=8TVKUWT87M16')
# price = driver.find_element(By.CLASS_NAME, value='Nx9bqj')
# search = driver.find_element(By.NAME, value='q')
# print(search.tag_name)
# print(price.text)
driver.get('https://www.python.org')
# button = driver.find_element(By.ID, value='submit')
# documentation = driver.find_element(By.CSS_SELECTOR, value='.slide-copy a')
# xpathfile = driver.find_element(By.XPATH, value='//*[@id="container"]/li[5]/ul/li[6]/a')
# print(xpathfile.text)
# print(documentation.text)
# print(button.size)
eventtime = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
eventvalue = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')    
event = {}
for n in range(len(eventtime)):
    event[n]={
        'eventtime':eventtime[n].text,
        'eventvalue':eventvalue[n].text
    }
print(event)
driver.quit()


