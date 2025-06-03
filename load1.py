from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

link ='http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys('Roman')
    browser.find_element(By.NAME, 'lastname').send_keys('Galkin')
    browser.find_element(By.NAME, 'email').send_keys('samara@mai.ru')

    file = "C:\\Users\\ACER\\Desktop\\selenium_course\\loading.txt"
    browser.find_element(By.ID, 'file').send_keys(file)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()