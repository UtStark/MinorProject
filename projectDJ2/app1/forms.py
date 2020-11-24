from django import forms

class StudentForm(forms.Form):
	enum = forms.IntegerField()