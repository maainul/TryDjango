from django.shortcuts import render
from django.http import HttpResponse

def home_view(request,*arg,**kwarg):
	#return HttpResponse("<h1>Hello world</h1>")
	return render(request,"home.html",{})

def about_view(request,*arg,**kwarg):
	my_context ={
		"my_text":"this is text",
		"my_number":123,
		"my_list":[1,12,34,54,33]
	}
	return render(request,"about.html",my_context)

def contact_view(request,*arg,**kwarg):
	return render(request,"contact.html",{})

def social_view(request,*arg,**kwarg):
	return render(request,"social.html",{})
	
