from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x_value = x_element.text

    def calc(x_value):
        return str(math.log(abs(12*math.sin(int(x_value)))))

    y = calc(x_value)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn.click()

finally:
    time.sleep(10)
    browser.quit()