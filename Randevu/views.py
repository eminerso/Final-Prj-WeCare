from django.shortcuts import render,redirect
from Admin_Control.models import Doctor_Add_Model
from  .forms import Monday_Randevu_Form
from  .models import Weekly_Randevu_Model
from datetime import datetime, timedelta
import json
from django.http import JsonResponse,HttpResponseBadRequest



# Create your views here.
def App(request,id,day):
     
      try:
       doct=Doctor_Add_Model.objects.filter(id=id).first()
       
       if request.method=="GET":
           daily_Data=Weekly_Randevu_Model.objects.filter(day=day,doc_email=doct.email).values_list("start_time",flat=True)
           if not daily_Data:
             return JsonResponse({'error': 'No appointments found'}, status=404)
           daily_Data = [time.strftime('%H:%M') for time in daily_Data]
          
           return JsonResponse(daily_Data, safe=False) 
       
       return JsonResponse({'error': 'Invalid request method'}, status=400)
      
      except Exception as e:
        return JsonResponse({'error': str(e)}, status=500) 




def Appointment_Page(request,id,day):

    
    doctor=Doctor_Add_Model.objects.filter(id=id).first() 
    form=Monday_Randevu_Form()
    context={"form":form,"doctor":doctor}
    

    if request.POST:
        form=Monday_Randevu_Form(request.POST)
        if form.is_valid():
            
            doc_email=     doctor.email
            day=day
            patient_name=  form.cleaned_data.get("patient_name")
            start_time=    form.cleaned_data.get("start_time")
            time_format='%H:%M'
            time_data=datetime.strptime(start_time,time_format).time()
            start_time_datetime=datetime.combine(datetime.today(),time_data)
            
            end_time_datetime= start_time_datetime+timedelta(minutes=30)
            endof_time=  end_time_datetime.time()
            patient_email= form.cleaned_data.get("patient_email")
            gender=        form.cleaned_data.get("gender")
            tel=           form.cleaned_data.get("tel")
            message=       form.cleaned_data.get("message" )

            monday_app= Weekly_Randevu_Model(doc_email=doc_email,day=day ,patient_name=patient_name, 
                                    start_time=time_data,endof_time=endof_time,
                                    patient_email=patient_email,
                                    gender=gender,tel=tel,message=message
                                    )
            monday_app.save()
            return redirect("Doctors")
        form=Monday_Randevu_Form

    return render(request,"doctor_detail.html",context)
