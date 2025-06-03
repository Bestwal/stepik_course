from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
link ='https://suninjuly.github.io/alert_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_el = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x_el)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


finally:
    time.sleep(10)
    browser.quit()