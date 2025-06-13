import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

languages = [
    ('ar', 'العربيّة', 'أضف الى سلة التسوق'),
    ('ca', 'català', 'Afegeix a la cistella'),
    ('cs', 'česky', 'Vložit do košíku'),
    ('da', 'dansk', 'Læg i kurv'),
    ('de', 'Deutsch', 'In Warenkorb legen'),
    ('en-gb', 'English', 'Add to basket'),
    ('el', 'Ελληνικά', 'Προσθήκη στο καλάθι'),
    ('es', 'español', 'Añadir al carrito'),
    ('fi', 'suomi', 'Lisää koriin'),
    ('fr', 'français', 'Ajouter au panier'),
    ('it', 'italiano', 'Aggiungi al carrello'),
    ('ko', '한국어', '장바구니 담기'),
    ('nl', 'Nederlands', 'Voeg aan winkelmand toe'),
    ('pl', 'polski', 'Dodaj do koszyka'),
    ('pt', 'Português', 'Adicionar ao carrinho'),
    ('pt-br', 'Português Brasileiro', 'Adicionar à cesta'),
    ('ro', 'Română', 'Adauga in cos'),
    ('ru', 'Русский', 'Добавить в корзину'),
    ('sk', 'Slovensky', 'Pridať do košíka'),
    ('uk', 'Українська', 'Додати в кошик'),
    ('zh-hans', '简体中文', 'Add to basket'),
]

def test_add_to_basket_button_text(browser, request):
    lang = request.config.getoption('language')

    expected_text = None
    for code, _, text in languages:
        if code == lang:
            expected_text = text
            break
    if expected_text is None:
        pytest.skip(f"Language '{lang}' is not in the languages list")

    browser.get(link)

    wait = WebDriverWait(browser, 10)

    # Выбираем язык на сайте
    select_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='language']")))
    select = Select(select_elem)
    select.select_by_value(lang)

    # Нажимаем кнопку "Выполнить"
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default[type='submit']")))
    submit_button.click()

    # Ждем, пока кнопка добавления в корзину обновится с нужным текстом
    def button_text_changed(driver):
        try:
            button = driver.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
            return expected_text in button.text
        except:
            return False

    wait.until(button_text_changed)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    button_text = button.text

    assert expected_text in button_text, f"Expected '{expected_text}' in button text, got '{button_text}'"

    wait = WebDriverWait(browser, 10)

    # Найти селект и выбрать язык
    select_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='language']")))
    select = Select(select_elem)
    select.select_by_value(lang)

    # Найти кнопку "Выполнить" и нажать её
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-default[type='submit']")))
    submit_button.click()

    # Теперь ждём, что кнопка "Добавить в корзину" обновится с правильным текстом
    def button_text_changed(driver):
        try:
            button = driver.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
            return expected_text in button.text
        except:
            return False

    wait.until(button_text_changed)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    button_text = button.text

    assert expected_text in button_text, f"Expected '{expected_text}' in button text, got '{button_text}'"