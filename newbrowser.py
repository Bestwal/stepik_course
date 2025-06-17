from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
link = 'http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    current_handle = browser.current_window_handle
    print(current_handle)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    browser.switch_to.window(browser.window_handles[1])
    x_el = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x_el)
    current_handle = browser.current_window_handle
    print(current_handle)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


finally:
    time.sleep(10)
    browser.quit()