# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Blog(models.Model):
	subject = models.CharField(max_length=100)
	Author=models.CharField(max_length=50)
	email=models.EmailField()
	blo = models.CharField(max_length=1000)

	def __str__(self):
		return self.subject;

class Comment(models.Model):
	blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
	comment=models.CharField(max_length=100)



