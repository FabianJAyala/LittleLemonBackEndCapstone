from django.test import TestCase;
from restaurant.models import Menu;
import json;

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Lemonade", price=2.49, inventory=30)
    def test_getall(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)
        serialized_data = json.loads(response.content)
        expected_data = [
            {
                'id': 1,
                "title": "Lemonade",
                "price": "2.49",
                "inventory": 30,
            },
        ]
        self.assertEqual(serialized_data, expected_data)