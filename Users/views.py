from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest
from .forms import SignUp
from django.contrib.auth import login
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import messages
from wecare.utils import send_otp
from datetime import datetime
import pyotp



from django.contrib.auth import authenticate,login,logout
from .forms import Log_In


# Create your views here.
def SignUp_Page(request):
    form=SignUp(request.POST or None)


    if form.is_valid():
        email=    form.cleaned_data.get("email")
        users=User.objects.filter(email=email).exists()
        if users:
            messages.error(request," Email Is Taken" )
            return redirect("SignUp")

           
        
        firstname=form.cleaned_data.get("firstname")
        lastname= form.cleaned_data.get("lastname")
        
        password= form.cleaned_data.get("password")
        

        newUser=User.objects.create_user(username=firstname,first_name=firstname,last_name=lastname, email=email, password=password)
        newUser.username=firstname
        newUser.first_name=firstname
        newUser.last_name= lastname
        newUser.email=email
        newUser.set_password=password
        newUser.save()
        login(request, newUser)
        return redirect("Home")
    
    context={"form":form}
    return render(request,"signup.html",context)



def Login_Page(request):
   form=Log_In(request.POST or None)
   context={"form":form}
   if form.is_valid():
      email=    form.cleaned_data.get("email")  
      password= form.cleaned_data.get("password")
      user=authenticate(email=email,password =password)
      if user is None:
         messages.error(request,"Wrong Email or Password" )
         return render(request,"login.html")
      
      request.session["user_email"]=email
      send_otp(request)
      return redirect("otp")
      
   return render(request,"login.html", context)

def otp(request):
   if request.method=="POST":
      otp=request.POST['otp']

      otp_secret_key=request.session['otp_secret_key']
      otp_valid_until=request.session['otp_valid_date']
      if otp_secret_key and otp_valid_until is not None:
         valid_until=datetime.fromisoformat(otp_valid_until)
         if valid_until>datetime.now():
            totp=pyotp.TOTP(otp_secret_key, interval=60)
            if totp.verify(otp):
                email=request.session["user_email"]
                user=get_object_or_404(User,email=email)
                login(request, user)
                del request.session["otp_secret_key"]
                del request.session["otp_valid_date"]
                return redirect('Home')

   return render(request, "otp.html")





def Log_Out_Page(request):
   logout(request)
   return redirect('Login')

def Forgot_Password(request):
  
   if request.method=="POST":
      email=request.POST["email"]
      users=User.objects.filter(email=email).exists()
      if users:
         password=User.objects.filter(email=email).values_list('password')
         print(f' your passowrd{password}')
         messages.success(request,f'Your Password:{ password}' )
      else:
         messages.error(request,'Wrong Email' )



      
      


      
         


   return render(request,"forgot_password.html")




