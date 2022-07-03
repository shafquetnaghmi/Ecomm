from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from .models import User

class signupform(UserCreationForm):   #form to register user
    phone=forms.CharField(max_length=20, required=True, help_text='Phone number')

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','phone','password1','password2']

class VerifyForm(forms.Form):   #form to verify the code which is sent to user's mobile no
    code = forms.CharField(max_length=8, required=True, help_text='Enter code')
