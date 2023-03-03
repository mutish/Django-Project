from django.db import models

# Create your models here.
class Catalogue(models.Model):
    product_name = models.CharField(max_length=30)
    product_image = models.ImageField()
    product_price = models.CharField(max_length=10)
    class Meta:
        db_table = "catalogue"