from django.urls import path
from django.contrib import admin
from . import views

admin.site.site_header = "GTBIT Administration"
admin.site.site_title = "RFID Attendance System"
admin.site.index_title = "Welcome "

urlpatterns = [
    path('', views.homepage,name="home"),
    path('show/', views.display,name="display"),
    path('student/',views.student,name="student")
    #write student enroll no. as argument
    
]