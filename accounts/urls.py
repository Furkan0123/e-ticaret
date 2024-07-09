# from django.urls import path
# from . import views


# urlpatterns = [
#     path('login/', views.user_login, name="login"),
#     path('register/', views.user_register, name="register"),
#     path('dashboard/', views.user_dashboard, name="dashboard"),
#     path('logout/', views.user_logout, name="logout"),
#     path('user/profile/', views.user_profile, name='user_profile'),
#     path('user/profile/', views.user_profile, name='user_register'),
#     path('shopping/cart/', views.shopping_cart, name='shopping_cart'),

# ]




from django.urls import path
from .views import user_login, user_register, user_dashboard, user_logout 

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('logout/', user_logout, name='logout'),
    
]


