from django import forms
from datetime import datetime
  
  
class Monday_Randevu_Form(forms.Form):
      gender_choices=[("Male","Male"),("Female","Female")]
      time_choices=[("09:00","09:00"),("09:30","09:30"),("10:00","10:00")
                    ,("10:30","10:30"),("11:00","11:00"),("12:00","12:00")
                    ,("12:30","12:30")]

      
      patient_name=   forms.CharField(    label="Your name"   ,        max_length=50)
      start_time=     forms.ChoiceField(  label="times",               choices=time_choices, widget=forms.Select( attrs={"id":"time_options"}) )
      gender=         forms.ChoiceField(  label="Gender",              choices=gender_choices,widget=forms.Select )
      patient_email=  forms.EmailField(   label="Your email",          max_length=30)
      tel=            forms.CharField(    label="Tel" ,                max_length=50)
      message=        forms.CharField(    label="Message For Doctor" , max_length=250)

      
