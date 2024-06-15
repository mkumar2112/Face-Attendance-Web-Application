"""
URL configuration for FaceAttendence project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import Home, face_attendance, Add_face_attendance, contact, loginuser, Today_Present, All_Present, createuser , AboutUs, logoutuser


urlpatterns = [
    path('Home', Home ), # Home Page
    path('loggedIn/attendance', face_attendance , name='attendance'),
    path('loggedIn/Addemp', Add_face_attendance , name='Add_employee'), #Add Employee
    path('loggedIn/contact', contact, name='ContactUs' ), #Contact Page
    path('logging', loginuser , name='loginuser'), #Loging User
    path('createuser', createuser , name='createuser'), #CreateUser
    path('loggedIn/Today', Today_Present, name='today_present' ), # Today Presents Employees
    path('loggedIn/Total', All_Present , name='all_present'), # Total employee Present
    path('loggedIn/AboutUs', AboutUs ,name='about_us'), # About Us Page
    path('logout', logoutuser ,name='logout'), #Log out User
]







