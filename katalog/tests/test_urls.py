from django.test import SimpleTestCase
from django.urls import reverse, resolve
from katalog.views import show_catalog

class UrlsTest(SimpleTestCase):

    def test_url(self):
        url = reverse('katalog:katalog')
        self.assertEquals(resolve(url).func, show_catalog)
        