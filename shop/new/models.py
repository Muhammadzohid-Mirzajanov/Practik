from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Kategoriya ismi")
    photo = models.ImageField(upload_to='photos/',verbose_name='categoriya rasmi')

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.TimeField()
    photo = models.ImageField(upload_to='photos/')
    description = models.TextField()

    def __str__(self):
        return self.name
    


