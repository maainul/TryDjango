from django.shortcuts import render
from django.http import HttpResponse

def home_view(request,*arg,**kwarg):
	return render(request,"pages/home.html",{})

	#return HttpResponse("<h1>Mainul</h1>")

def about_view(request,*arg,**kwarg):
	context = {
		"items"	:	[1,2,3,4]
	}
	return render(request,"pages/about.html",context)
	#return HttpResponse("<h1>About</h1>")


def social_view(request,*arg,**kwarg):
	return render(request,"pages/social.html",{})
	#return HttpResponse("<h1>social</h1>")

def contact_view(request,*arg,**kwarg):
	return render(request,"pages/contact.html",{})

	#return HttpResponse("<h1>contact</h1>")