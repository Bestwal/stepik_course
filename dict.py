from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    num1_el = browser.find_element(By.CSS_SELECTOR, "#num1")
    num1 = int(num1_el.text)
    num2_el= browser.find_element(By.CSS_SELECTOR, "#num2")
    num2 = int(num2_el.text)
    x = num1 + num2
    select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    select.select_by_value(str(x))
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()


finally:
    time.sleep(10)
    browser.quit()