from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# launch Browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#open Google
driver.get("https://www.pondit.com/")
time.sleep(2)

#print Titel
print(driver.title)

#close the browser
driver.quit()