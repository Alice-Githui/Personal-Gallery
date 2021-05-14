from django.db import models

# Create your models here.

class Location(models.Model):
    name=models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Image(models.Model):
    image= models.ImageField()
    image_name=models.CharField(max_length=400)
    description=models.CharField(max_length=400)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

