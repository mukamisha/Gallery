from django.db import models

# Create your models here.

class Image(models.Model):
    img_name = models.CharField(max_length =30)
    img_description = models.CharField(max_length =30)
    # location = models.ForeignKey(Location)
    # category = models.ForeignKey(Category)
  
    def __str__(self):
        return self.first_name


    class Meta:
        ordering = ['img_name']

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name