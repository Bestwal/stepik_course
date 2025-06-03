from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = 'https://football.kulichki.net/'
browser = webdriver.Chrome()
browser.get(link)

# Подожди, чтобы страница подгрузилась (лучше заменить на WebDriverWait)
time.sleep(2)

# Клик по "Премьер-лига"
browser.find_element(By.CSS_SELECTOR, 'a[href="/ruschamp/"]').click()

time.sleep(2)

# Найдём ссылку на "Олимп", прокрутим к ней и кликнем
olimp_link = browser.find_element(By.CSS_SELECTOR, 'a[href="/olimp/"]')
browser.execute_script("arguments[0].scrollIntoView(true);", olimp_link)
olimp_link.click()

# Пауза, чтобы увидеть результат
time.sleep(10)

# Закрыть браузер (по желанию)
# browser.quit()