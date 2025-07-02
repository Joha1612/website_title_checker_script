from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# launch Browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.saucedemo.com/")
time.sleep(2)

user_id = "standard_user"
user_password ="secret_sauce"

login_id = driver.find_element(By.ID,("user-name"))
login_id.send_keys(user_id)

login_password = driver.find_element(By.ID, ("password"))
login_password.send_keys(user_password)

login_button = driver.find_element(By.ID,("login-button"))
login_button.click()

assert "inventory" in driver.current_url
print("Login successful! Now on inventory page.")
time.sleep(2)
driver.quit()