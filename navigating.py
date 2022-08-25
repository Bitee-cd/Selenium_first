from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service('C:\Program Files (x86)\chromedriver.exe')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://awajis.com/all-nigerian-gsm-numbers-and-networks/')

try:
    link = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Home"))
    )
    link.click()
except:
    driver.quit()


