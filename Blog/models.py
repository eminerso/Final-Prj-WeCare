from django.db import models

# Create your models here.
class Blog_Model(models.Model):
    blog=models.CharField( max_length=100)
    blog_content=models.CharField(max_length=1500)
    blog_image=models.ImageField(upload_to="images/",blank=True)