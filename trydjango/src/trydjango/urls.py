from django.contrib import admin
from django.urls import path
from pages.views import home_view,contact_view,social_view,about_view
from products.views import product_detail_view,product_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),
    path('about/',about_view),
    path('social/',social_view),
    path('contact/',contact_view),
    path('create/',product_create_view),
    path('detail/',product_detail_view),
]

