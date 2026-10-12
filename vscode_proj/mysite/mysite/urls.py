
from django.contrib import admin
from django.urls import path
from first_proj import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('/catalog', views.catalog_page, name='catalog'),
    path('/cart', views.cart_page, name='cart'),
    path('/contacts', views.contacts_page, name='contacts')
]
