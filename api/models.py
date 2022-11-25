from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(
        null=True, blank=True, help_text='Give some info about the Product')
    price = models.FloatField(blank=True, null=True)
    category_id = models.ForeignKey('Categorys', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Categorys(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(
        null=True, blank=True, help_text='Give some info about the Category') 