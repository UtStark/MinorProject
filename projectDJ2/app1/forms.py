from django import forms

class StudentForm(forms.Form):
	Enroll_No_ = forms.IntegerField()