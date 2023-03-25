
# Create your models here.
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class test(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

    class Meta:
        verbose_name = 'my model'


class Product_test(models.Model):
    product_name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)
    
    def __str__(self) :
        return self.product_name
    
class Product_price(models.Model):
    product = models.ForeignKey(Product_test, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0) 
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)