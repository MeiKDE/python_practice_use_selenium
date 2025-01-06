from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome()
driver.get("https://www.python.org/")
print(driver.title)  # Should output "Welcome to Python.org"


# Wait for the event-widget to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".event-widget"))
)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {"time": event_times[n].text, "name": event_names[n].text}

print(events)
