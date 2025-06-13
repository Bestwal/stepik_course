import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


LOGIN = "hammerfallsamara@mail.ru"
PASSWORD = "patriot99"

@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_feedback_correct(browser, link):
    browser.get(link)
    wait = WebDriverWait(browser, 10)

    login_button = wait.until(EC.element_to_be_clickable((By.ID, 'ember479')))
    login_button.click()

    email_input = wait.until(EC.visibility_of_element_located((By.NAME, 'login')))
    email_input.clear()
    email_input.send_keys(LOGIN)

    password_input = browser.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(PASSWORD)

    submit_login = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_login.click()
    time.sleep(3)
    textarea = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "textarea[placeholder='Напишите ваш ответ здесь...']")
    ))
    answer = str(math.log(int(time.time())))
    textarea.clear()
    textarea.send_keys(answer)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    submit_button.click()

    feedback = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint")))

    feedback_text = feedback.text.strip()
    assert feedback_text == "Correct!", f"Ожидался текст 'Correct!', но получен '{feedback_text}' на странице {link}"
    solve_again_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "again-btn")))
    solve_again_button.click()
    time.sleep(1)