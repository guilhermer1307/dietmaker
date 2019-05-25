from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	CHOICES = ('ALUNO', 'PROFESSOR')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	user_type = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())

	class Meta:
		model = User
		fiels = ('username', 'email', 'user_type', 'password1', 'password2')

