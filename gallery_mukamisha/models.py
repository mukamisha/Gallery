from django.db import models

class Image(models.Model):
    img_name = models.CharField(max_length =30)
    img_description = models.CharField(max_length =30)
    # email = models.EmailField()
# Create your models here.
