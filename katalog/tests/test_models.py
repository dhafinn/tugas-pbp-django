from django.test import TestCase
from katalog.models import CatalogItem

class TestModels(TestCase):
    def setUp(self):
        self.catalogTest = CatalogItem.objects.create(
            item_name = 'Kering Kentang',
            item_price = 30000,
            item_stock = 15,
            description = 'Cemilan olahan kentang yang asin dan pedas',
            rating = 10,
            item_url = 'https://www.tokopedia.com/tatasnacks/kering-kentang-mustofa-original'
        )

    def test_catalog_item_dummy(self):
        self.assertEqual(
            self.catalogTest, 
            CatalogItem.objects.get(item_name = 'Kering Kentang')
        )
