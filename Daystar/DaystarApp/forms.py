from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BabyRegForm(ModelForm):
    class Meta:
        model = BabyReg
        fields =  '__all__'

class BabyAttendanceForm(ModelForm):
    class Meta:
        model = BabyAttendance
        fields =  '__all__'

  #sitter forms      
class SitterForm(ModelForm):
    class Meta:
        model = Sitter
        fields = '__all__'
        widgets={
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class SitterAttendanceForm(ModelForm):
    class Meta:
        model = SitterAttendance
        fields = '__all__'
        widgets = {
            'timeIn': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'timeOut': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DollForm(ModelForm):
    class Meta:
        model = Doll
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SalesrecordForm(ModelForm):
    class Meta:
        model = Salesrecord
        fields = '__all__'
        widgets = {
            'sale_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
class BabyCheckoutForm(forms.ModelForm):
    class Meta:
        model = BabyAttendance
        fields = ['B_name', 'timeOut']
        widgets = {
            'timeOut': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
class SitterCheckoutForm(forms.ModelForm):
    class Meta:
        model = SitterAttendance
        fields = ['S_name', 'timeOut']
        widgets = {
            'timeOut': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }