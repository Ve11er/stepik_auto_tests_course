import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    name.send_keys("Test")

    surname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    surname.send_keys("Testov")

    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys("test@test.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn.click()

finally:
    time.sleep(10)
    browser.quit()