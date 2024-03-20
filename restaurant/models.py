from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255, verbose_name='Full Name')
    no_of_guests = models.IntegerField(verbose_name='Number of Guest')
    bookingDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    title = models.CharField(max_length=255, verbose_name='Item Name')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price $')
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title}: ${self.price}'
 
    def get_item(self):
        return f'{self.title} : ${self.price}'
    

