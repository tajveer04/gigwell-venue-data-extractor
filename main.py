import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
from pathlib import Path
from getpass import getpass

# Ask for the user's own login details before opening the browser.
email = input("Gigwell email: ").strip()
password = getpass("Gigwell password: ")

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://discover.gigwell.com/auth/login")

# Open CSV file for writing
output_file = Path(__file__).resolve().parent / "gigwell.csv"
with open(output_file, mode="w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "name", "address", "email", "phone", "capacity", "avg",
        "directory_first", "directory_first_title", "directory_first_phone", "directory_first_email",
        "directory_second", "directory_second_title", "directory_second_phone", "directory_second_email",
        "directory_third", "directory_third_title", "directory_third_phone", "directory_third_email",
        "directory_forth", "directory_forth_title", "directory_forth_phone", "directory_forth_email",
        "directory_fifth", "directory_fifth_title", "directory_fifth_phone", "directory_fifth_email",
        "directory_sixth", "directory_sixth_title", "directory_sixth_phone", "directory_sixth_email",
        "directory_seventh", "directory_seventh_title", "directory_seventh_phone", "directory_seventh_email"
    ])

    # Login
    try:
        login_email = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
        login_email.send_keys(email)
    except Exception as e:
        print(f"Error finding email input: {e}")

    try:
        login_password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        login_password.send_keys(password)
    except Exception as e:
        print(f"Error finding password input: {e}")

    try:
        login = driver.find_element(By.XPATH, "//button[normalize-space()='Log In With Email']")
        login.click()
    except Exception as e:
        print(f"Error clicking login button: {e}")

    # Wait for page to load
    time.sleep(5)

    # Enter keywords and set filters
    try:
        find_keyword = driver.find_element(By.XPATH, "//input[@placeholder='Type to add keyword...']")
        keywords = ["-nightclub", "-bar", "-restaurant", "-club"]

        for keyword in keywords:
            find_keyword.send_keys(keyword)
            find_keyword.send_keys(Keys.ENTER)
            time.sleep(1)

        time.sleep(5)  # Extra wait to ensure keywords are added
    except Exception as e:
        print(f"Error adding keywords: {e}")

    # Set minimum capacity
    # try:
    #     capacity = driver.find_element(By.XPATH, "//input[@placeholder='Min']")
    #     capacity.clear()
    #     capacity.send_keys("200")
    #     time.sleep(5)
    # except Exception as e:
    #     print(f"Error setting capacity: {e}")

    # Clear location filter
    try:
        location_clear = driver.find_element(By.XPATH, "//i[@class='gw-icon-times small']")
        location_clear.click()
    except Exception as e:
        print(f"Error clearing location filter: {e}")

    # Wait for venues to load
    time.sleep(5)

    # Function to process venues on the current page
    def process_venues():
        try:
            venues = driver.find_elements(By.XPATH, "//div/ul[@class='venue-portal-search-results-list list-unstyled']/li")
            for venue in venues:
                try:
                    venue.click()
                except Exception as e:
                    print(f"Error clicking venue: {e}")
                    continue
