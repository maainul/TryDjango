from django.shortcuts import render
from .models import Product
from .forms import ProductForm,RawProductForm



# Product create form 
def product_create_view(request):
	my_form = RawProductForm()
	if request.method == "POST":
		my_form = RawProductForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			Product.objects.create(**my_form.cleaned_data)
	else:
		print(my_form.errors)
	context={"form":my_form}
	return render(request,"products/product_create.html",context)
# # Product create form 
# def product_create_view(request):
# 	form = ProductForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form= ProductForm()
# 	context={"form":form}
# 	return render(request,"products/product_create.html",context)

# def product_create_view(request):
# 	print(request.GET)
# 	print(request.POST)
# 	context={}
# 	return render(request,"products/product_create.html",context)


# Product detail page 
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context={"object":obj}
	return render(request,"products/product_detail.html",context)

