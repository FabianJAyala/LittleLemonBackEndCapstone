from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id=10,title="Lemonade", price=3.50, inventory=40)
        self.assertEqual(item.title, "Lemonade")
        self.assertEqual(item.price, 3.50)