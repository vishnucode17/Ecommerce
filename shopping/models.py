from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Store(models.Model):
    seller_store_name = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)
    def __str__(self):
        return self.seller_store_name
class Product(models.Model):
    product_category=[
        ('elec','Electronics'),
        ('fas','Fashion'),
        ('app','Home and Appliances'),
        ('book','Books and Magazines'),
    ]
    store_name=models.ForeignKey(Store,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    Category=models.CharField(max_length=255,choices=product_category)
    product_info=models.CharField(max_length=516)
    price=models.IntegerField()
    product_img=models.ImageField(upload_to='product_images/')
    def __str__(self):
        return self.product_name