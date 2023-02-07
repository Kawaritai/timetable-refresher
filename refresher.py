from selenium.webdriver.common.by import By

from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

import time

edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.add_experimental_option("detach", True)

# Create Edge driver instance
driver = Edge(executable_path='edgedriver_win64\msedgedriver.exe', options=edge_options)

# Go to mytimetable login
print("Go to myTimetable login")
driver.get('https://mytimetable.anu.edu.au/odd/student')

# Security 100%
USERNAME="OPTUS"
PASSWORD="OPTUS123"

# Wait for login to load fully
print("Waiting for login to load fully")
time.sleep(15)

# Click "Username and Password button"
print("Click Username and Password option")
up_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[1]/div/div[6]/a/div")
print(up_button)
up_button.click()   

# Enter login details and submit
print("Enter login details and submit")
username = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[1]/div/form/div[1]/div/input")
username.send_keys(USERNAME)
password = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[1]/div/form/div[2]/div/input")
password.send_keys(PASSWORD)
submit_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div/div[1]/div/form/button[1]")
submit_button.click()

# Wait for timetable page to load
print("Waiting for timetable page to load fully")
time.sleep(5)

print("Beginning refresh loop")
i = 1
while True:
    driver.refresh()

    print()
    print(f"Refreshed {i}")
    alert = driver.find_element(By.XPATH, "//*[@id='home-tpl']/div[2]/div[2]")
    print(alert.get_attribute("innerHTML"))
    print()

    time.sleep(10)
    i += 1