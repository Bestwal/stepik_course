from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = " https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    option1 = browser.find_element(By.CSS_SELECTOR, ".form-check-input")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, ".form-check-input[id='robotsRule']")
    option2.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()





finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()