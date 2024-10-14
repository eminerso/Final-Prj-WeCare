from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import Doctor_Add_Form
from .models import Doctor_Add_Model
from Randevu.models import Weekly_Randevu_Model
from django.contrib import messages
import json


# # Create your views here.

def Your_Profile_Page(request):

    if request.POST:
        form=Doctor_Add_Form(request.POST, request.FILES)
        if form.is_valid():
            name=                    form.cleaned_data.get("name")
            last_name=               form.cleaned_data.get("last_name")
            email=                   form.cleaned_data.get("email")
            tel=                     form.cleaned_data.get("tel")
            about_me=                form.cleaned_data.get("about_me")
            my_skills=               form.cleaned_data.get("my_skills")
            education=               form.cleaned_data.get("education")
            education_start_years=   form.cleaned_data.get("education_start_years")
            education_grad_years=    form.cleaned_data.get("education_grad_years")
            speciality=              form.cleaned_data.get("speciality")
            experiance_start_years=  form.cleaned_data.get("experiance_start_years")
            experiance_finish_years= form.cleaned_data.get("experiance_finish_years")
            doctor_image=            form.cleaned_data.get("doctor_image")
            new_doctor=Doctor_Add_Model(name=name, last_name=last_name, email=email, tel=tel, about_me=about_me, my_skills=my_skills, education=education,education_start_years=education_start_years, education_grad_years=education_grad_years, speciality=speciality,experiance_start_years=experiance_start_years, experiance_finish_years=experiance_finish_years,doctor_image=doctor_image)
            new_doctor.save()
        
            messages.success(request, "You have been successfully logged in.")
            return redirect("Home")
        else:
             return redirect("Your_Profile")
    form=Doctor_Add_Form()

    email=request.user.email
    doc_profile=Doctor_Add_Model.objects.filter(email=email).exists()

    Doctor_Randevu=Weekly_Randevu_Model.objects.filter(doc_email = email).values('day','patient_name','gender','patient_email',"start_time")
    
    data = []
    for randevu in Doctor_Randevu:
        data.append({
            'gender': randevu['gender'],
            'day': randevu['day'],
            'patient_name': randevu['patient_name'],
            'patient_email': randevu['patient_email'],
            'start_time': randevu['start_time'].strftime('%H:%M:%S')
        })



    context={"form":form, "doc_profile":doc_profile,"Randevus":data}
    return render(request,"your_profile.html",context)


 
