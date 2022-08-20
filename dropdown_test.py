import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(By.CSS_SELECTOR, '[id="num1"]')
    x_element2 = browser.find_element(By.CSS_SELECTOR, '[id="num2"]')
    x_element1 = int(x_element1.text)
    x_element2 = int(x_element2.text)
    x_value = x_element1 + x_element2

    select = Select(browser.find_element(By.CSS_SELECTOR, '[id="dropdown"]'))
    select.select_by_value(str(x_value))

    btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn.click()


finally:
    time.sleep(10)
    browser.quit()
