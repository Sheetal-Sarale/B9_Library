from django.forms import fields
from .models import Employee
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        Model = Employee
        fields = "__all__"