from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#treasure").get_attribute('valuex')
    option1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    option2 = browser.find_element(By.CSS_SELECTOR, '.check-input').click()
    option3 = browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()