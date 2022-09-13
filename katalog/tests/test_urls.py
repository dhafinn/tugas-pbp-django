from django.test import SimpleTestCase
from django.urls import reverse, resolve
from katalog.views import show_catalog

class UrlsTest(SimpleTestCase):

    def test_url(self):
        url = reverse('katalog:katalog')
        self.assertEquals(resolve(url).func, show_catalog)


# Reference
# https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2    