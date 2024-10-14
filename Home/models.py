from django.db import models

# Create your models here.

class Services_Model(models.Model):
    service=models.CharField( max_length=50)
    about=models.CharField(max_length=500)
    service_image=models.ImageField( upload_to="images/", blank=True)
    def __str__(self):
        return self.service


class GetInTuch(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    tel=models.CharField(max_length=30)
    message=models.CharField(max_length=200)
    def __str__(self):
       return self.name
    
