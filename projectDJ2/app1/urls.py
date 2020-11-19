from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage,name="home"),
    path('show/', views.display,name="display"),
    path('student/',views.student,name="student")
    #write student enroll no. as argument
    
]