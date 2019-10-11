from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()    

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name 

    def save_category(self):
        self.save()

    


class Image(models.Model):
    img =  models.ImageField(upload_to = 'image/')
    img_name = models.CharField(max_length =30)
    img_description = models.TextField()
    location = models.ForeignKey(Location)
    Category = models.ForeignKey(Category)
  
    def __str__(self):
        return self.img_name


    class Meta:
        ordering = ['img_name']

  