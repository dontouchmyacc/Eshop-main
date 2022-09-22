from ast import Or
from django.contrib import admin

from store.models.favorite import Favorites
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields=['name',]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name'] 

class OrderAdmin(admin.ModelAdmin):
    list_display= ('product','customer','quantity', 'price', 'address','phone','date','status')
    search_fields= ['phone',]

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order,OrderAdmin)
admin.site.register(Favorites)


# username = ilyas, email = aist07pvl@gmail.com, password = 123
