from django.shortcuts import render
from store.models.product import Products
from store.models.favorite import Favorites
from store.models.customer import Customer
from django.shortcuts import redirect
# Create your views here.
def add_to_favorite(request, product_id):
    user = request.user if request.user.is_authenticated else None
    if request.method == 'GET':
        product = Products.objects.get(pk=product_id)

        user = request.user

        favorite = Products.objects.get()
        if favorite:
            Products.objects.clear()


        if product:
            Favorites.objects.create(user=user, product=product)

    else:
        pass

    next_page = request.META.get('HTTP_REFERER', 'product_list')
    return redirect(next_page)