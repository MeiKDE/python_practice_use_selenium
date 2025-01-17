from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")
print(driver.title)  # Should output "Welcome to Python.org"

# Hone in on anchor tag using CSS selectors
# Xpath //*[@id="articlecount"]/a[1]
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)


# article_count.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)
