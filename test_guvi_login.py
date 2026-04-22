
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 1) Validate URL of login button to be "https://www.guvi.in/sign-in/"
def test_validate_url_guvi_login_button(driver):
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    driver.find_element(By.ID, "login-btn").click()
    print(driver.current_url)
    driver.assertion.current_url = "https://www.guvi.in/sign-in/"

# 2) Validate that the Username and Password input boxes is visible and enabled
def test_validate_username_password_input_boxes(driver):
    driver.get("https://www.guvi.in/sign-in/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//input[@type='email']").is_displayed()
    print("email address input box is visible")
    driver.find_element(By.ID, "email").send_keys("poojaraghuraman.297@gmail.com")
    print("email address input box is enabled")
    driver.find_element(By.XPATH, "//input[@type='password']").is_displayed()
    print("password input box is visible")
    driver.find_element(By.ID, "password").send_keys("1@Vegetass")
    print("password input box is enabled")

# 3) Validate Submit button is working properly
def test_validate_submit_button(driver):
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    driver.find_element(By.ID, "login-btn").click()
    print("Login page url is:" ,driver.current_url)
    driver.find_element(By.ID, "email").send_keys("poojaraghuraman.297@gmail.com")
    driver.find_element(By.ID, "password").send_keys("1@Vegetass")
    driver.find_element(By.CSS_SELECTOR, "#login-btn").click()
    WebDriverWait(driver , 2).until(EC.url_changes("https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F"))
    print("After login page URL is:" ,driver.current_url)
    assert driver.current_url == "https://www.guvi.in/"

def test_validate_submit_button_negative_scenario(driver):
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    driver.find_element(By.ID, "login-btn").click()
    print("Login page url is:" ,driver.current_url)
    driver.find_element(By.ID, "email").send_keys("poojaraghurama.297@gmail.com")
    driver.find_element(By.ID, "password").send_keys("1@Vegeta")
    driver.find_element(By.CSS_SELECTOR, "#login-btn").click()
    error_message = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='invalid-feedback is-invalid']")))
    assert error_message.text == "Incorrect Email or Password"
