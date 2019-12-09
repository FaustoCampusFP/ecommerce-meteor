from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default='N/A')
    size = models.CharField(max_length=100, default='N/A')
    color = models.CharField(max_length=100, default='N/A')
    price = models.IntegerField()
    image = models.ImageField(upload_to='shoes', default='shoes/no-disponible.png')

    def __str__(self):
        return self.title
