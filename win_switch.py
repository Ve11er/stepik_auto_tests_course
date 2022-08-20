from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x_value = x_element.text

    def calc(x_value):
        return str(math.log(abs(12 * math.sin(int(x_value)))))

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(calc(x_value))

    btn2 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    btn2.click()


finally:
    time.sleep(10)
    browser.quit()