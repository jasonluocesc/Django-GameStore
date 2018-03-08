from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Game
from django.forms import ModelForm
from decimal import Decimal

class SignUpForm(UserCreationForm):
	self_description = forms.CharField(max_length=200, required = False, widget = forms.Textarea, label = "self-description", initial="I'm cool!!", help_text="Introduce yourself with short sentences")
	email = forms.EmailField(max_length=254, required=True, help_text='A valid email address is required for activating your account.')
	is_developer = forms.BooleanField(initial = False,required=False)
	is_gamer = forms.BooleanField(initial = True,required=False)
	class Meta(UserCreationForm.Meta):
		fields = ('username', 'first_name', 'last_name', 'email')
		help_texts={
			'first_name':'optional',
			'last_name':'optional',
		}

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class ProfileForm(forms.Form):
	self_description = forms.CharField(max_length=200, required = False, widget = forms.Textarea, label = "Self-description", help_text="Introduce yourself with short sentences")
	is_developer = forms.BooleanField(required=False)
	is_gamer = forms.BooleanField(required=False)
	first_name = forms.CharField(max_length=20, required = False, label = "First Name")
	last_name = forms.CharField(max_length=20, required = False,  label = "Last Name")
	photo = forms.ImageField(required = False)
	
class AddgameForm(ModelForm):
	#the form is from game model
	class Meta:
		model = Game
		fields = ['name','description','price','url','image']

class EditgameForm(ModelForm):
	#the form is from game model
	class Meta:
		model = Game
		fields = ['description','price','url','image','valid']
