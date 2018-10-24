from pages import views
from django.contrib import admin
from django.urls import path
from pages.views import home_view,about_view,social_view,contact_view
from products.views import (
    product_detail_view,
    product_create_view,
    render_initial_data,
    product_delete_view,
    product_list_view
    )

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.home_view, name='home'),

	path('about/',about_view),
	path('contact/',contact_view),
	path('social/',social_view),

    path('product/<int:id>',product_detail_view),
    path('create/',product_create_view),
    path('edit/',render_initial_data),
    path('product/<int:id>/delete/',product_delete_view),
     path('products/',product_list_view),
]
