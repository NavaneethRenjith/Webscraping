# Log In to Facebook

from selenium import webdriver
import time
import getpass

email = input("Enter email/phone : ")
password = getpass.getpass(prompt="Enter password : ")

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Navaneeth R\programs\web scraping\projects\chromedriver_win32\chromedriver.exe"
)
driver.get("https://www.facebook.com/")

input_email = driver.find_element_by_id("email")
input_email.send_keys(email)
input_pass = driver.find_element_by_id("pass")
input_pass.send_keys(password)
btn = driver.find_element_by_id("u_0_b")

time.sleep(5)
btn.click()

