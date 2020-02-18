# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import BlogForm, SignUpForm, CommentForm
from .models import Blog

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate



def LogIn(request):
	return render(request,'index.html')

def SignUp(request):
	return render(request,'signup.html')

def thanks(request):
	return render(request,'thanks.html')


def get_data(request):
	if (request.method=="POST"):	
			form = BlogForm(request.POST)
			form1=CommentForm(request.POST)
			if(form.is_valid() and form.is_valid()):
				name = form.cleaned_data['subject']
				author = form.cleaned_data['Author']
				form.save()
				form1.save()
				return render(request,'thanks.html', {'name':name , 'author':author})
	else:
		form=BlogForm()
		form1=CommentForm()

	return render(request,'name.html',{'form':form, 'form1':form1})


# def sign_up(request):
# 	if(request.method == "POST"):
# 		form = SignUpForm(request.POST)
# 		if(form.is_valid()):
# 			form.save()
# 			user1 = form.cleaned_data.get('username')
# 			password1 = form.cleaned_data.get('password')
# 			user =authenticate(username=user1, password=password1)
# 			login(request,user)
# 			return redirect('http://127.0.0.1:7000/')
# 	else:
# 		form = SignUpForm()
		
# 	return render(request,'signup2.html',{'form':form})


def sign_up(request):
	if(request.method == "POST"):
		form = SignUpForm(request.POST)
		if(form.is_valid()):
			form.save()
			user1 = form.cleaned_data.get('username')
			password1 = form.cleaned_data.get('password')
			user =authenticate(username=user1, password=password1)
			login(request,user)
			return redirect('http://127.0.0.1:7000/')
	else:
		form = SignUpForm()
		
	return render(request,'signup2.html',{'form':form})


def homepage(request):
	return render(request,'home.html')

