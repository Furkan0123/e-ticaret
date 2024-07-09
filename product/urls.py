from django.urls import path
from . import  views
from .views import  add_to_cart, cart_detail , remove_from_cart , payment_view, success_view, error_view

urlpatterns = [
    path('', views.product_list, name='product'),
    path('<slug:category_slug>/<int:product_id>', views.product_detail, name= 'product_detail'),
    path('<slug:category_slug>/<int:product2_id>/detail2/', views.product_detail2, name='product_detail2'),
    path('<slug:category_slug>/<int:product3_id>/detail3/', views.product_detail3, name='product_detail3'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('payment/', payment_view, name='payment'),
    path('success/', success_view, name='success'),
    path('error/', error_view, name='error'),

]
