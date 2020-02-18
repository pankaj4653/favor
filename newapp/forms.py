from django import forms
from .models import Blog, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
	blo = forms.CharField(widget=forms.Textarea)
	comment=forms.CharField(max_length=500)
	class Meta:
			model = Blog
			fields =['subject','Author','email','blo','comment',]


class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=['blog', 'comment']

class SignUpForm(UserCreationForm):
	username=forms.CharField(max_length=30)
	email=forms.EmailField(max_length=100)
	#password=forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model=User
		fields = ['username','email','password1','password2']