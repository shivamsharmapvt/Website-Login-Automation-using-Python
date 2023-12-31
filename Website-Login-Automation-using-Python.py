# Import the Selenium WebDriver module to automate web interactions.
from selenium import webdriver

# Import the 'By' class from Selenium's common 'by' module to specify how to locate elements.
from selenium.webdriver.common.by import By

# Import necessary modules and classes
import typing # For typing annotations

from selenium.common.exceptions import WebDriverException # Import an exception class
from selenium.webdriver.common.by import By # Import a class for locating elements by various strategies
from selenium.webdriver.remote.webdriver import WebDriver # Import WebDriver class for browser control
from selenium.webdriver.remote.webelement import WebElement # Import WebElement class for interacting with web elements
from selenium.webdriver.support.ui import WebDriverWait # Import WebDriverWait class for explicit waits
from selenium.webdriver.support import expected_conditions as EC # Import expected conditions for waits

# Import the WebDriver module from Selenium and create a connection with your Chrome browser.
browser = webdriver.Chrome("#Enter the address of the Chrome Webdriver(.exe)")

# Maximize the browser window to ensure it covers the entire screen.
browser.maximize_window()

# Navigate to the specified URL.
browser.get("#Enter the website address")

# Initialize a WebDriverWait instance with a timeout of 10 seconds
wait = WebDriverWait(browser, 10)

# Wait for the 'email' element to become clickable (interactable)
# before attempting to interact with it
username = wait.until(EC.element_to_be_clickable((By.ID, "#Enter the ID of Email field in website")))

# Input the email address "jaideep.pandher@gmail.com" into the 'email' element
username.send_keys("#Enter your email id")

# Locate the password input element by its ID and wait for it to be clickable
password = wait.until(EC.element_to_be_clickable((By.ID, "#Enter the ID of Password field in website")))

# Input the password '9910950118' into the password input field
password.send_keys('#Enter your password')

# Wait until the element with ID "login_btn" becomes clickable
login = wait.until(EC.element_to_be_clickable((By.ID, "#Enter the ID of Submit button in website")))

# Click on the "login_btn" element
login.click()
