from django.shortcuts import render
from .models import Product

def product_detail_view(request):
	obj = Product.objects.get(id=1)
	#context={
	#	'title':obj.title,
	#	'description':obj.description,
	#	'price':obj.price,
	#	'summary':obj.summary
	#}
	context={
		"object":obj
	}

	return render(request,"product/detail.html",context)