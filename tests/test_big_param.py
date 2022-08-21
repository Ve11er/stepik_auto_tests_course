import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math


@pytest.mark.parametrize('site', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_param(browser, site):
    link = f"https://stepik.org/lesson/{site}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)

    answer_place = browser.find_element(By.CSS_SELECTOR, '.string-quiz__textarea')
    answer = math.log(int(time.time()))
    answer_place.send_keys(answer)

    btn = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    btn.click()

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".smart-hints__hint"), "Correct!"))

    msg = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    msg_text = msg.text
    assert "Correct!" == msg_text, f"{msg_text}"






