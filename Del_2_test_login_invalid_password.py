import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_login_invalid_password(driver):
    driver.get("https://www.saucedemo.com/")

    # Ange korrekt användarnamn men fel lösenord
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    # Vänta på felmeddelande
    error = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
    )

    assert "Username and password do not match" in error.text
    assert driver.current_url == "https://www.saucedemo.com/"

    # Paus så du hinner se felmeddelandet
    time.sleep(10)
