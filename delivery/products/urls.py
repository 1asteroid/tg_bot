from django.urls import path
from .views import UserView, ProductView

urlpatterns = [
    path("users/", UserView.as_view(), name='user_list'),
    path("products/", ProductView.as_view(), name='product_list')
]