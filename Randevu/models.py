from django.db import models



# Create your models here.
class Weekly_Randevu_Model(models.Model):
    doc_email=     models.EmailField( max_length=30 ,default="emin@mm.nn")
    day=           models.CharField(  max_length=50 ,default="Monday")
    patient_name=  models.CharField(  max_length=50 ,default="Emin")
    start_time=    models.TimeField(  default='09:01:10')
    endof_time=    models.TimeField(  default='09:01:10')
    gender=        models.CharField(  max_length=10)
    patient_email= models.EmailField( max_length=30)
    tel=           models.CharField(  max_length=50)
    message=       models.CharField(  max_length=250, blank=True,default="Control")
    created_at =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name
    