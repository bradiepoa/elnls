from django.shortcuts import render,redirect

from django.http import HttpResponse
# messages
from django.contrib import auth, messages
# login below
from django.contrib.auth import authenticate,login,logout
from . models import *
from .forms import *

# Create your views here.


# admin overall
def Homeview(request):

	msg = Chat.objects.filter(Message_To="administor")

	booklst = Book.objects.all()

	totalbks = booklst.count()

	totalpdf = Book.objects.filter(Status='pdf').count()

	totalreserved = Book.objects.filter(Status='reserve').count()

	category = Bookcategory.objects.all().count() 

	context = {'booklst':booklst, 'totalbks':totalbks, 'category':category, 
	'totalpdf':totalpdf, 'totalreserved':totalreserved, 'msg':msg}

	return render(request, 'bookapp/admin/index.html', context)

# adding a book==================================
def AddBookFormView(request):

	form = AddbooksForm()
	if request.method=='POST':
		form = AddbooksForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get('Title')
			messages.success(request, name + '  Book added submitted successfully.')
			return redirect('bookapp:dashboardpage')

	context = {'form':form}
	return render(request, 'bookapp/admin/addbookform.html', context)

# updating a book=========================
def UpdateBook(request, upd_bk):

	booklst = Book.objects.get(id=upd_bk)
	form = AddbooksForm(instance=booklst)

	if request.method == "POST":
		form = AddbooksForm(request.POST, request.FILES ,instance=booklst)
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get('Title')
			messages.success(request, name + ' Updated successfully...!')
			return redirect('bookapp:dashboardpage')

	context = {'form':form}
	return render(request, 'bookapp/admin/addbookform.html', context)

def DeleteBook(request,del_bk):

	booklst = Book.objects.get(id=del_bk)

	if request.method =="POST":
		booklst.delete()
		messages.success(request,' Deleted successfully...!')
		return redirect('bookapp:dashboardpage')

	context = {'item':booklst}
	return render(request, 'bookapp/admin/delete_book.html',context)

def BkCategory(request):

	category = Bookcategory.objects.all()

	context ={'category':category}
	return render(request, 'bookapp/admin/bkcategory.html', context)

def AddBookCategory(request):

	form = AddBKCategory()
	if request.method =="POST":
		form = AddBKCategory(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Category Added successfully..!!')
			return redirect('bookapp:dashboardpage')

	context = {'form':form}
	return render(request , 'bookapp/admin/addbookcategory.html', context)

def UpdateBkCategory(request, upd_bkc):

	category = Bookcategory.objects.get(id=upd_bkc)
	form = AddBKCategory(instance=category)

	if request.method == "POST":
		form = AddBKCategory(request.POST, instance=category)
		if form.is_valid():
			form.save()
			namex = form.cleaned_data.get('name')
			messages.success(request, namex + ' Updated successfully...!')
			return redirect('bookapp:Bkcategorypage')

	context = {'form':form}
	return render(request , 'bookapp/admin/addbookcategory.html', context)


def ChatDetails(request):

	msg = Chat.objects.filter(Message_To="administor")

	booklst = Book.objects.all()

	totalbks = booklst.count()

	totalpdf = Book.objects.filter(Status='pdf').count()

	totalreserved = Book.objects.filter(Status='reserve').count()

	category = Bookcategory.objects.all().count() 

	context = {'booklst':booklst, 'totalbks':totalbks, 'category':category, 
	'totalpdf':totalpdf, 'totalreserved':totalreserved, 'msg':msg}
	return render(request, 'bookapp/admin/chat.html',context)


# end of admin overall============================================================



# publisher==========================================================
def Homelbview(request):

	booklst = Book.objects.all()

	totalbks = booklst.count()

	totalpdf = Book.objects.filter(Status='pdf').count()

	totalreserved = Book.objects.filter(Status='reserve').count()

	category = Bookcategory.objects.all().count() 

	context = {'booklst':booklst, 'totalbks':totalbks, 'category':category, 'totalpdf':totalpdf, 'totalreserved':totalreserved}


	return render(request, 'bookapp/publisher/indexlb.html', context)

# students====================================================
def Homestview(request):

	booklst = Book.objects.filter(Status="pdf")

	totalbks = booklst.count()

	totalpdf = Book.objects.filter(Status='pdf').count()

	totalreserved = Book.objects.filter(Status='reserve').count()

	category = Bookcategory.objects.all().count() 

	context = {'booklst':booklst, 'totalbks':totalbks, 'category':category, 'totalpdf':totalpdf, 'totalreserved':totalreserved}

	return render(request, 'bookapp/students/indexst.html', context)

def LogoutUser(request):
	logout(request)
	return redirect('bookapp:loginpage')

def Loginview(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request,user)
			if user.is_admin  or user.is_superuser:
				return redirect('bookapp:dashboardpage')
			elif user.is_publisher:
				return redirect('bookapp:dashlibrarian')
			else:
				return redirect('bookapp:studentbookpage')
		else:
			messages.info(request, "Invalid Username or Password")
			return redirect('bookapp:loginpage')
	return render(request, 'bookapp/login.html')


def Registeriew(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			messages.success(request,'Account was Created for ' + user)
			return redirect('bookapp:loginpage')

	context = {'form':form}
	return render(request, 'bookapp/register.html',context)