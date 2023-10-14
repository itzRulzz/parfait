from django.test import TestCase
from recipe_parser import link_parser

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'search_bar': 'A new search query'})
        self.assertIn('A new search query', response.content.decode())

    def test_display_queries_with_data_from_parser(self):
        # Вызвать парсер вручную. Передать запрос на сайт с тем же текстом.
        # Сравнить выведенные представлением результаты после POST-запоса.
        parser_data = link_parser('Парфе')
        response = self.client.post('/', data={'search_bar': 'Парфе'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['results'], parser_data)
    
    '''
    def test_redirect_after_POST(self):
        response = self.client.post('/', data={'search_bar': 'A new search query'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')
    '''
