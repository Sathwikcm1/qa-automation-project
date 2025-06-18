# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By #NOTE: this is used to locate the element in the web page.
from selenium.webdriver.support.ui import WebDriverWait
#NOTE: WebDriverWait makes selenium wait for elements to load before interacting.
from selenium.webdriver.support import expected_conditions as EC
#NOTE: expected_conditions : predefined conditions as EC (e.g.: EC.visibility_of_element_located)
import pytest
#TODO: Testing framework to organize and run tests.

@pytest.fixture #HACK: A setup/cleanup function that runs before/after each test.
def driver():
    driver = webdriver.Firefox()
    yield driver #NOTE: Pauses execution until the test finishes, then runs driver.quit()
    driver.quit()

def test_invalid_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Using explicit waits for reliability
    wait = WebDriverWait(driver, 10)
    
    # Step 1-3: Enter credentials and submit
    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "submit").click()
    
    # Step 4: Verify error
    error = wait.until(EC.visibility_of_element_located((By.ID, "error")))
    assert "Your username is invalid!" in error.text



def test_valid_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    wait = WebDriverWait(driver,10)

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    success_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    ).text

    assert success_text == "Logged In Successfully"
