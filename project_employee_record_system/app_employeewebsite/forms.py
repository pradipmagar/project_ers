from django import forms
from .models import Employee

class EmployeeCreateForm(forms.ModelForm):
    """ Form class for Employee creation """
    
    class Meta:
        fields = "__all__"
        # fields = ("Full_Name", "Contact")
        model = Employee