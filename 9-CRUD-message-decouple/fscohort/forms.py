from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__' 
        labels = {"first_name": "Your Name", "last_name":"Your Surname", "number":"Your Number"}