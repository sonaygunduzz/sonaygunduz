from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, FileInput, Select
from django import forms

from home.models import UserProfile


class SearchForm(forms.Form):
   query = forms.CharField(label='search', max_length=100)

class SignUpForm(UserCreationForm):
   username = forms.CharField(max_length=30, label='User Name')
   email = forms.EmailField(max_length=50, label='Email')
   first_name = forms.CharField(max_length=100, help_text='First Name', label='First Name')
   last_name = forms.CharField(max_length=100, help_text='Last Name', label='Last Name')


   class Meta:
      model = User
      fields = ('username', 'email','first_name','last_name', 'password1', 'password2')

class UserUpdateForm(UserChangeForm):
   class Meta:
      model = User
      fields = ('username', 'email', 'first_name', 'last_name')
      widgets ={
         'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
         'email': EmailInput(attrs ={'class': 'input', 'placeholder': 'email'}),
         'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
         'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),

      }
CITY = [
   ('Istanbul','Istanbul'),
   ('Ankara', 'Ankara'),
   ('İzmir', 'İzmir'),

]

class ProfileUpdateForm(forms.ModelForm):
   class Meta:
      model = UserProfile
      fields = ('phone', 'address', 'city', 'country', 'image')
      widgets = {
         'phone' : TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
         'address' : TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
         'city' : Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
         'country' : TextInput(attrs={'class': 'input', 'placeholder': 'country'}),
         'image' : FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
      }