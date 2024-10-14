from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse,HttpResponseBadRequest
from Admin_Control.models import Doctor_Add_Model
from .models import Services_Model
from Blog.models import Blog_Model
import json
from .models import GetInTuch
from django.contrib import messages
from  Randevu.forms import Monday_Randevu_Form




# Create your views here.

def Home_page(request):
   
    Doctors=Doctor_Add_Model.objects.all()[:6]
    context={"Doctors":Doctors}
    return render(request,"home.html",context)



def All_Services_Page(request):
    doctors=Doctor_Add_Model.objects.all().values("name","last_name","id")
    names=list(doctors)
    servicess=Services_Model.objects.all().values("id","service","about","service_image")
    services=list(servicess)
    context={"doctors": json.dumps(names),"services":json.dumps(services)}
    return render(request,"all_services.html",context)


def ajax_req_for_doc(request, spec):
    if request.method == "GET":
        try:
            doctors = Doctor_Add_Model.objects.filter(speciality=spec)
            doctor_list = list(doctors.values("name", "email", "speciality","doctor_image"))
            return JsonResponse(doctor_list, safe=False)
        except Doctor_Add_Model.DoesNotExist:
            return JsonResponse({"error": "Doctor not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid request method")




def Service_Detail_Page(request,id,service):
    doctors=Doctor_Add_Model.objects.all().values("name","last_name","id")
    names=list(doctors)
    all_services=Services_Model.objects.all()
    service=Services_Model.objects.filter(id=id).first()
    spec_doctors=Doctor_Add_Model.objects.filter(speciality=service)
    s_img = service.service_image.url if service.service_image else ''
    context={"doctors": json.dumps(names),"service":service,"spec_doctors":spec_doctors,"all_services":all_services, "img":s_img}
    return render(request,"service_detail.html",context)

def Blog_Page(request):
    doctors=Doctor_Add_Model.objects.all().values("name","last_name","id")
    names=list(doctors)
    

    blogs=Blog_Model.objects.all()
    context={"doctors": json.dumps(names),"blogs" : blogs }
   
    return render(request,"blog.html",context)

def Contact_Page(request):
    doctors=Doctor_Add_Model.objects.all().values("name","last_name","id")
    names=list(doctors)
    

    if request.method=="POST": 
        name=     request.POST.get("name")
        email=    request.POST.get("email")
        tel=      request.POST.get("phone")
        message=  request.POST.get("message")
        newMessage=GetInTuch(name=name,tel=tel,email=email,message=message)
        newMessage.save()
        messages.success(request, "Your Message sent..Thanks")
    else:
        messages.error(request, "Something Went Wrong!!!")

    context={  "doctors": json.dumps(names)}
               
    return render(request,"contact_us.html",context)

def Doctors_Page(request):
    doctors=Doctor_Add_Model.objects.all().values("name","last_name","id")
    names=list(doctors)
    Doctors=Doctor_Add_Model.objects.all()
    context={"doctors": json.dumps(names),"Doctors":Doctors}
    return render(request,"doctors.html",context)


def Doctor_Detail_Page(request,id,day=None): 
    form=Monday_Randevu_Form()
    doctor=Doctor_Add_Model.objects.filter(id=id).first()
    doct=Doctor_Add_Model.objects.filter(id=id).first()
    list_data=doct.id
    print(F'your otp:{list_data}')
    context={"form":form,"doctor":doctor,"id":list_data}

    return render(request,"doctor_detail.html",context)


def Blog_Detail_Page(request,id):

    blog=Blog_Model.objects.filter(id=id).first()
    context={ "blog":blog}

    return render(request,"blog_detail.html",context)

def Privacy_Page(request):
    doctors=Doctor_Add_Model.objects.all().values("name","last_name","id")
    names=list(doctors)
    context={"doctors": json.dumps(names)}
    return render(request,"privacy.html",context)
def Term_Page(request):
    doctors=Doctor_Add_Model.objects.all().values("name","last_name","id")
    names=list(doctors)
    context={"doctors": json.dumps(names)}
    return render(request,"term.html",context)
def About_Page(request):
    doctors=Doctor_Add_Model.objects.all().values("name","last_name","id")
    names=list(doctors)
    Doctors=Doctor_Add_Model.objects.all()
    context={"doctors": json.dumps(names),"Doctors":Doctors}
    return render(request,"aboutus.html",context)








