from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to website
driver.get("https://secure-retreat-92358.herokuapp.com/")
print(driver.title)

# Hone in on anchor tag using CSS selectors
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email_address = driver.find_element(By.NAME, value="email")

first_name.send_keys("Mei")
print(first_name)
last_name.send_keys("Zhang")
print(last_name)
email_address.send_keys("dsflsdk@gmail.com")
print(email_address)

# Sign Up class name "btn btn-lg btn-primary btn-block"
sign_up_btn = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_up_btn.click()
