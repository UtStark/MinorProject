from django.shortcuts import render
from app1.models import Attendance
# Create your views here.
def display(request):

    show=Attendance.objects.all()
    #print(display)

    return render(request, "page1.html",{'Attendance': show})

    #write a view to show the values of a specefic d\student

    #write a form to enter value and then redirect it this view to show details with a differnt template to show value beautifully