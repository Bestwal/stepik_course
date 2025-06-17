from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
link = 'https://SunInJuly.github.io/execute_script.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_el = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x_el)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, 'robotsRule').click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()