from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        first_name.send_keys("Ivan")
        second_name = browser.find_element(By.CSS_SELECTOR, ".second_class > .form-control.second")
        second_name.send_keys("Pupkin")
        email = browser.find_element(By.CSS_SELECTOR, ".third_class > .form-control.third")
        email.send_keys("test@test.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text is not equal")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        first_name.send_keys("Ivan")
        second_name = browser.find_element(By.CSS_SELECTOR, ".second_class > .form-control.second")
        second_name.send_keys("Pupkin")
        email = browser.find_element(By.CSS_SELECTOR, ".third_class > .form-control.third")
        email.send_keys("test@test.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text is not equal")


if __name__ == "__main__":
    unittest.main()
