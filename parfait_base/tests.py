from django.test import TestCase

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    