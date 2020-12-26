from django.shortcuts import render
from app1.models import Attendance
from .forms import StudentForm
# Create your views here.
def display(request):

    show=Attendance.objects.all()

    return render(request, "page1.html",{'Attendance': show})

def homepage(request):

    return render(request, 'project.html')

def student(request):
	if request.method == 'POST':

		form = StudentForm(request.POST)
		if form.is_valid():

			enum=form.cleaned_data['enum']
			data= Attendance.objects.get(enum=enum)

			print(data.name)

			return render(request, 'attendance.html',{'data':data})

	form=StudentForm()

	return render(request, 'stulogin.html', {'form':form})


    #write a view to show the values of a specefic d\student

    #write a form to enter value and then redirect it this view to show details with a differnt template to show value beautifully