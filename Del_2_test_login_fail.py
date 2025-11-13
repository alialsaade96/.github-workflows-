from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    service = Service()  # You can specify the path to chromedriver if needed
    options = webdriver.ChromeOptions()
    # Make sure the browser window opens
    # options.add_argument("--headless")  # ← Leave this line commented out
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_login_fail(driver):
    driver.get("https://www.saucedemo.com/")
    
    # Enter correct username but wrong password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    # Wait for error message to appear
    error = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
    )

    # Confirm the error message is displayed
    assert "Username and password do not match" in error.text or "Epic sadface" in error.text
