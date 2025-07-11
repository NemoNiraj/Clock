from selenium import webdriver
from selenium.webdriver.common.by import By
import time

start_time = time.time()

for _ in range(2):
    # Set up the browser (make sure you have the correct driver installed)
    driver = webdriver.Chrome()

    # Open the specified URL
    url = 'https://www.google.com'  # Replace with your actual URL
    driver.get(url)

    # Wait for 10 seconds
    time.sleep(10)

    # Click the login button (replace 'login' with the actual ID or selector if needed)
    # login_button = driver.find_element(By.ID, 'login')
    # login_button.click()

    # Optionally, wait after clicking login
    #time.sleep(30)

    # Close the browser after both runs
    driver.quit()
    #time.sleep(600)  # Wait for 10 minutes before next iteration

end_time = time.time()
print(f"Program ran for {end_time - start_time:.2f} seconds.")