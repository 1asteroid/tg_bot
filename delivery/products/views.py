from django.shortcuts import render
from .models import User, Product
from django.views import View


class UserView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, "user_list.html", {"users": users})


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "product_list.html", {"products": products})
