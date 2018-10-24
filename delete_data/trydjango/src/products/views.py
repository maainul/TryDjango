from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .forms import ProductForm,RawProductForm
from django.http import Http404
def product_create_view(request):
	form = ProductForm(request.POST or None)
	
	if form.is_valid():
		form.save()

	form = ProductForm()

	context={"form": form}

	return render(request,"products/product_create.html",context)

# def product_create_view(request):
# 	my_form = RawProductForm()
# 	if request.method == "POST":
# 		my_form = RawProductForm(request.POST)
# 		if my_form.is_valid():
# 			print(my_form.cleaned_data)
# 			Product.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.errors)
# 	context={"form": my_form}
# 	return render(request,"products/product_create.html",context)


def product_detail_view(request,id):
	#obj = Product.objects.get(id=id)

	# only when we use get_object_404
	obj = get_object_or_404(Product,id = id)

	# This is Http404 error 
	# try:
	# 	obj = Product.objects.get(id=id)
	# except Product.DoesNotExist:
	# 	raise Http404

	#context={
	#	'title':obj.title,
	#	'description':obj.description,
	#	'price':obj.price,
	#	'summary':obj.summary
	#}
	context={
		"object":obj
	}

	return render(request,"products/product_detail.html",context)


def render_initial_data(request):
	#initial_data = {'title': "this is my title"}
	obj = Product.objects.get(id=4)
	form = ProductForm(request.POST or None,instance = obj)
	if form.is_valid():
		form.save()
	context={'form':form}
	return render(request,"products/product_edit.html",context)

def product_delete_view(request,id):
	#obj = Product.objects.get(id = id)
	obj = get_object_or_404(Product,id=id)
	if request.method =="POST":
		obj.delete()
		return redirect('../../')
	context={"object":obj}
	return render(request,"products/product_delete.html",context)

def product_list_view(request):
	queryset = Product.objects.all()
	context={"object_list":queryset}
	return render(request,"products/product_list.html",context)
