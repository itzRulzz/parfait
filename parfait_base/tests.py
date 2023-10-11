from django.test import TestCase

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'search_bar': 'A new search query'})
        self.assertIn('A new search query', response.content.decode())

    def test_can_display_queries(self):
        # Представление сохраняет текст юзера из POST-запроса и
        # возвращает страницу уже с его использованем.
        response = self.client.post('/', data={'search_bar': 'A new search query'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['ten'], ['A new search query'] * 10)

    def test_redirect_after_POST(self):
        response = self.client.post('/', data={'search_bar': 'A new search query'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')
