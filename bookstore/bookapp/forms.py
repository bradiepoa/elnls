from django.core.validators import validate_slug, validate_email
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User

		fields = ['username','email', 'password1', 'password2']



class AddbooksForm(ModelForm):
	class Meta:
		model = Book

		fields = '__all__'

class AddBKCategory(ModelForm):
	class Meta:
		model = Bookcategory

		fields = '__all__'


class SendMessage(ModelForm):
	class Meta:
		model = Chat

		fields = '__all__'