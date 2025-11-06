from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # 1. Öppna sidan
    driver.get("https://www.saucedemo.com/")

    # 2. Ange användarnamn och lösenord
    driver.find_element(By.ID, "user-name").send_keys("stanggg_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # 3. Klicka på login
    driver.find_element(By.ID, "login-button").click()

    # 4. Vänta lite för att sidan ska ladda
    time.sleep(2)

    # 5. Kontrollera att rubriken "Products" visas
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products", "Inloggning misslyckades!"

    print("✅ Testet lyckades: Användaren loggades in korrekt.")

finally:
    driver.quit()
