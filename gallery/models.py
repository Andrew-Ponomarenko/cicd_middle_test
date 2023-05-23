from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
class Image(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    categories = models.ManyToManyField(Category,blank=True)
    created_date = models.DateField()
    age_limit = models.PositiveIntegerField()