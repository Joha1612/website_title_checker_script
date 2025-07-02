from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ✅ Browser Setup Function
def open_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(1)
    return driver

# ✅ Test 1: Login using only IDs
def test_login_by_id(username, password):
    print("🔍 Test: Login by ID")
    driver = open_browser()

    # Fill inputs by ID
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    assert "inventory" in driver.current_url, "❌ Login failed using ID"
    print("✅ Login successful using ID\n")
    driver.quit()

# ✅ Test 2: Login using only XPath
def test_login_by_xpath(username, password):
    print("🔍 Test: Login by XPath")
    driver = open_browser()

    # Fill inputs by XPath
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    time.sleep(2)

    assert "inventory" in driver.current_url, "❌ Login failed using XPath"
    print("✅ Login successful using XPath\n")
    driver.quit()

# ✅ Run Both Tests
if __name__ == "__main__":
    test_login_by_id("standard_user", "secret_sauce")
    test_login_by_xpath("standard_user", "secret_sauce")
