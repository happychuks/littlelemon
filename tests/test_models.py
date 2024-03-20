from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
 def test_get_item(self):
  item = Menu.objects.create(title = 'Fried Rice', price = 4.5, inventory = 50)
  itemstr = item.get_item()
  
  self.assertEqual(itemstr, 'Fried Rice : 4.5')
  