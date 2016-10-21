from __future__ import unicode_literals

from django.db import models

# Create your models here.
class book(models.Model):
	ISBN = models.CharField(max_length=20)
	Title = models.CharField(max_length=50)
	AuthorID = models.IntegerField()
	Publisher = models.CharField(max_length=50)
	PublishDate = models.DateField()
	Price = models.FloatField()

class author(models.Model):
	AuthorID = models.IntegerField(blank=True,null=True)
	Name = models.CharField(max_length=20,blank=True)
	Age = models.IntegerField(blank=True,null=True)
	Country = models.CharField(max_length=30,blank=True)

