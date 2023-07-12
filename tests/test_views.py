from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setup(self):
        created_item = Menu.objects.create(title='Ice Cake', price=15, inventory='10')
        retrieved_item = Menu.objects.get(title='Ice Cake')        
        self.assertDictEqual(created_item, retrieved_item)
