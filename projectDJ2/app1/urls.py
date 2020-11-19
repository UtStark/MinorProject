from django.urls import path

from . import views

urlpatterns = [
    path('', views.display,name="display"),
    #write student enroll no. as argument
    
]