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
        self.browser.get('http://localhost:8000')
        
        # Он вводит "Парфе" в текст-бокс (Коля любит французскую кухню).
        search_bar = self.browser.find_element('id', 'id_new_search')
        search_bar.send_keys('Парфе')

        # Коля видит, что до нажатия Enter никаких ссылок нету.
        table = self.browser.find_element('id', 'id_queries_table')
        queries = table.find_elements('tag name', 'tr')
        self.assertEqual(queries, [])

        # Коля нажимает Enter, ему выводится список 10-и рецептов этого блюда с разных сайтов.
        search_bar.send_keys(Keys.ENTER)
        time.sleep(1)

        # Переобъявляем новый контент таблицы после отправки запроса.
        table = self.browser.find_element('id', 'id_queries_table')
        queries = table.find_elements('tag name', 'tr')

        self.assertNotEqual(queries, [])
        self.assertEqual(len(queries), 10, f'Запросов выведено не 10. Вот запросы: {queries}')
        
        queries_text = [row.text for row in queries]
        
        self.assertTrue(
            all(('http' in row or 'https' in row) for row in queries_text)
        )
        # Проверить то, что каждый tr имеет атрибут a href.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
