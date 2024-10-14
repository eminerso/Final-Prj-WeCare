from django.db import models

# Create your models here.
class Doctor_Add_Model(models.Model):
    name=                   models.CharField(  max_length= 20)
    last_name=              models.CharField(  max_length= 20)
    email=                  models.EmailField( max_length= 30)
    tel=                    models.CharField(  max_length= 20)
    about_me=               models.TextField(  max_length= 600)
    my_skills=              models.TextField(  max_length= 600)
    education=              models.CharField(  max_length= 60)
    education_start_years=  models.DateField()
    education_grad_years=   models.DateField()
    speciality=             models.CharField(  max_length= 80)
    experiance_start_years= models.DateField()
    experiance_finish_years=models.DateField()
    doctor_image=           models.ImageField( upload_to="images/", blank=True)
    def __str__(self):
        return self.name





















# from django.db import models

# class Doctor_Add_Model(models.Model):
#     name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=70)
#     tel = models.CharField(max_length=20)
#     about_me = models.TextField(max_length=6000)
#     my_skills = models.TextField(max_length=6000)
#     education = models.CharField(max_length=100)
#     education_start_years = models.DateField()
#     education_grad_years = models.DateField()
#     speciality = models.CharField(max_length=100)
#     experiance_start_years = models.DateField()
#     experiance_finish_years = models.DateField()
#     doctor_image = models.ImageField(upload_to="images/", blank=True)

#     def __str__(self):
#         return self.name

