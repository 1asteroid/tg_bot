from django.contrib import admin
from .models import Product, User

admin.site.register([User, Product])

