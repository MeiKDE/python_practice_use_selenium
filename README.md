# Python Selenium: Extract Upcoming Events from Python.org

This script uses Selenium to scrape and extract upcoming events from the Python.org website. The events are displayed in a structured dictionary format with their corresponding time and name.

## Features

- Opens the Python.org homepage.
- Waits for the events widget to load.
- Extracts event times and names from the "Upcoming Events" section.
- Prints the extracted events in a dictionary format.

## Prerequisites

### 1. Install Python and Required Libraries
Ensure you have Python installed on your system. Install the necessary Python libraries:

```bash
pip install selenium
```

### 2. Install WebDriver
- **Chrome**: Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches your Chrome browser version.
- Place the WebDriver executable in a directory included in your system's `PATH`.

### 3. Verify Installation
Check if Selenium and WebDriver are correctly installed by running a basic script to open a browser.

## How It Works

1. **Setup WebDriver**:
   The script initializes a Chrome browser using Selenium and navigates to the Python.org homepage:
   ```python
   driver = webdriver.Chrome()
   driver.get("https://www.python.org/")
   print(driver.title)
   ```

2. **Wait for Events Widget**:
   It waits for the "Upcoming Events" widget to load using Selenium's explicit waits:
   ```python
   WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, ".event-widget"))
   )
   ```

3. **Extract Events**:
   The script locates the event times and names using CSS selectors:
   ```python
   event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
   event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
   ```

4. **Create Event Dictionary**:
   It iterates through the extracted elements and creates a dictionary:
   ```python
   events = {}
   for n in range(len(event_times)):
       events[n] = {"time": event_times[n].text, "name": event_names[n].text}
   print(events)
   ```

## Example Output

```plaintext
Welcome to Python.org
{
    0: {"time": "2023-10-12", "name": "Python Meetup"},
    1: {"time": "2023-10-15", "name": "Python Hackathon"},
    2: {"time": "2023-10-20", "name": "Django Conference"}
}
```