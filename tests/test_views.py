from django.test import TestCase
from restaurant.models import  Menu

class MenuViewTest(TestCase):
 def setUp(self):
  Menu.objects.create(title = 'Item1', price = 6, inventory = 100)
  Menu.objects.create(title = 'Item2', price = 3.50, inventory =100)
  Menu.objects.create(title = 'Item3', price = 4.6, inventory =100)
  
 def test_getall(self):
  all_menus = Menu.objects.all()
  
  self.assertEqual(all_menus.count(), 3)
  