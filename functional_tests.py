from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import requests

class MainTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    # Удовлетворенный, Коля уходит спать.
    def tearDown(self):
        self.browser.quit()

    def test_can_load_a_page_correctly(self):
        # Коля услышал о веб-приложении, которое помогает не тратить время
        # на поиск рецептов. Он переходит на главную страницу сайта.
        self.browser.get('http://localhost:8000')

        # Он видит, что во вкладке есть упоминание рецептов.
        self.assertIn('рецепты', self.browser.title)

        # Коля обращает внимание на логотип, красующийся по центру страницы.
        logo = self.browser.find_element('id', 'id_logo')
        logo_link = logo.get_attribute('src')
        req = requests.get(logo_link)
        self.assertEqual(req.status_code, 200)

        # Коля также подмечает приятный сероватый фон сайта.
        body = self.browser.find_element('tag name', 'body')
        body_style = body.get_attribute('style')
        self.assertIn(body_style, 'background-color: rgb(246, 246, 246);')

        # Коля видит строку для ввода запроса.
        search_bar = self.browser.find_element('id', 'id_new_search')
        self.assertNotEqual(search_bar, None)

        # В строке ввода написано: "Введите название блюда..."
        search_bar_text = search_bar.get_attribute('placeholder')
        self.assertEqual(search_bar_text, 'Введите название блюда...')

    def test_can_retrieve_recipes(self):
        # Он вводит "Парфе" в текст-бокс (Коля любит французскую кухню).
        search_bar = self.browser.find_element('id', 'id_new_search')
        search_bar.send_keys('Парфе')

        # Коля нажимает Enter, ему выводится список рецептов этого блюда с разных сайтов.
        search_bar.send_keys(Keys.ENTER)
        time.sleep(1)
        

        # Коле интересно, сбросятся ли найденные ссылки при обновлении страницы.
        # Коля замечает, что для него сгенерирован персональный URL.

        # На всякий случай он обновляет сайт и
        # с радостью замечает, что все ссылки остались на месте.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
