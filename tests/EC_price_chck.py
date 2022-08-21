import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    btn = browser.find_element(By.ID, "book")
    btn.click()

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
