from django.test import TestCase, Client
from django.urls import reverse, resolve
from mywatchlist.views import show_movie, show_json, show_xml

class UrlsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.movie_url = reverse('mywatchlist:show_movie')
        self.xml_url = reverse('mywatchlist:show_json')
        self.json_url = reverse('mywatchlist:show_xml')

    def test_html_url(self):
        response = self.client.get(self.movie_url)
        self.assertEqual(response.status_code, 200)

    def test_xml_url(self):
        response = self.client.get(self.xml_url)
        self.assertEqual(response.status_code, 200)

    def test_json_url(self):
        response = self.client.get(self.json_url)
        self.assertEqual(response.status_code, 200)
