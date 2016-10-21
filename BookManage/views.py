from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext, Context, Template
from BookManage.models import *


# Create your views here.
def show(request):
	book_posts = book.objects.all()
	author_posts = author.objects.all()
	dic={'book_posts':book_posts,'author_posts':author_posts}
	return render(request, 'show.html',dic)


def newBook(request):
	flag=False
	if request.method == 'POST':
		authors = author.objects.all()
		for a in authors:
			if(a.Name == request.POST.get('Name')):
				flag=True
				break
		if flag == True:
			newbook=book(
				ISBN=request.POST.get('ISBN'),
				Title=request.POST.get('Title'),
				AuthorID=a.AuthorID,
				Publisher=request.POST.get('Publisher'),
				PublishDate=request.POST.get('PublishDate'),
				Price=request.POST.get('Price'),
				)
			newbook.save()
			return HttpResponseRedirect('/show/')
		else:
			newauthor=author(
				Name=request.POST.get('Name'),
				)
			newauthor.save()
			newauthor.AuthorID=newauthor.pk
			newauthor.save()
			newbook=book(
				ISBN=request.POST.get('ISBN'),
				Title=request.POST.get('Title'),
				AuthorID=newauthor.AuthorID,
				Publisher=request.POST.get('Publisher'),
				PublishDate=request.POST.get('PublishDate'),
				Price=request.POST.get('Price'),
				)
			newbook.save()
			newauthor.save()
			return HttpResponseRedirect('/addAuthor/')
	

def newAuthor(request):
	if request.method == 'POST':
		authors=author.objects.all()
		for a in authors:
			if a.Name == request.POST.get('Name'):
				a.Age=request.POST.get('Age')
				a.Country=request.POST.get('Country')
				a.save()
				return HttpResponseRedirect('/show/')



def addBook(request):
	return render(request,'addBook.html')

def addAuthor(request):
	return render(request,'addAuthor.html')

def deleteBook(request,ISBN):
	delBook=book.objects.get(ISBN=ISBN)
	delBook.delete()
	return HttpResponseRedirect('/show/')

def details(request,ISBN):
	showbook=book.objects.get(ISBN=ISBN)
	authors=author.objects.all()
	for a in authors:
		if a.AuthorID == showbook.AuthorID:
			showauthor=author.objects.get(AuthorID=a.AuthorID)
			break
	dic={'showbook':showbook,'showauthor':showauthor}
	return render_to_response('details.html',dic)

def searchName(request):
	if request.method == 'POST':
		author_result=author.objects.get(Name=request.POST.get('search_name'))
	author_result_id = author_result.AuthorID
	lst=[]
	books = book.objects.all()
	for b in books:
		if b.AuthorID==author_result_id:
			lst.append(b.Title)
	return render(request,'searchAuthor.html',{'lst':lst})

update_ISBN=0

def updateBook(request,ISBN):
	update_book=book.objects.get(ISBN=ISBN)
	global update_ISBN
	update_ISBN=ISBN
	authors = author.objects.all()
	for a in authors:
		if a.AuthorID == update_book.AuthorID:
			update_author=author.objects.get(AuthorID=a.AuthorID)
			break
	dic={'update_book':update_book,'update_author':update_author}
	return render(request,'updateBook.html',dic)

def updateAll(request):
	flag=False
	global update_ISBN
	
	if request.method == 'POST':
		try:
			books=book.objects.all()
			for b in books:
				if b.ISBN == update_ISBN:
					b.Publisher=request.POST.get('Publisher')
					b.PublishDate=request.POST.get('PublishDate')
					b.Price=request.POST.get('Price')
					b.save()
					break
			authors=author.objects.all()
			for a in authors:
				if a.Name == request.POST.get('Name'):
					flag=True
					break
			if flag:
				b.AuthorID=a.AuthorID
				b.save()
				return HttpResponseRedirect('/show/')
			else:
				newauthor=author(
					Name=request.POST.get('Name'),
					)
				newauthor.save()
				newauthor.AuthorID=newauthor.pk
				newauthor.save()
				b.AuthorID=newauthor.AuthorID
				b.save()
				return HttpResponseRedirect('/addAuthor/')
		except:
			return HttpResponseRedirect('/Error/')
	

def Error(request):
	return render(request,'error.html')



				
	




