
from django.contrib import admin
from django.urls    import path
from Home.views     import Home_page,Term_Page,Privacy_Page,About_Page,ajax_req_for_doc,Contact_Page, All_Services_Page, Blog_Page, Service_Detail_Page,Doctor_Detail_Page,Blog_Detail_Page, Doctors_Page
from Users.views    import SignUp_Page,Login_Page,Log_Out_Page,otp,Forgot_Password
from Randevu.views import Appointment_Page,App
from Admin_Control.views  import Your_Profile_Page

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",                                    Home_page,           name="Home"),
    path("otp/",                                otp,                 name="otp"),
    path("signup/",                             SignUp_Page,         name="SignUp"),
    path("login/",                              Login_Page,          name="Login"),
    path("logout/",                             Log_Out_Page,        name="Logout"),
    path("forgot_password/",                    Forgot_Password,    name="Forgot_Password"),
    path("your_profile/",                       Your_Profile_Page,   name="Profile"),
    path("contact/",                            Contact_Page,        name="Contact_Us"),
    path("allservices/",                        All_Services_Page,   name="All_Services"),
    path("aboutus/",                            About_Page,          name="About_Us"),
    path("privacy/",                            Privacy_Page,        name="Privacy"),
    path("terms/",                              Term_Page,           name="Terms"),
    path('allservices/allservices/<str:spec>/', ajax_req_for_doc, name='All_Service_Doctors'),
    path("service_detail/<int:id>/<str:service>", Service_Detail_Page, name="Service_Detail"),
    path("blog/",                               Blog_Page,           name="Blog"),
    path("doctors/",                            Doctors_Page,        name="Doctors"),
    path("doctor_detail/<int:id>",              Doctor_Detail_Page,  name="Doctor_Detail"),
    path("appointment/<int:id>/<str:day>/",     Appointment_Page,    name="appointment"),
    path("doctor_detail/<int:id>/<str:day>/",   App,    name="App"),
    path("blog_detail/<int:id>",                Blog_Detail_Page,    name="Blog_Detail"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
