from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
     path('signup/', views.register_user, name='signup'),  
    path('logout/', views.logout_view, name='logout'),
    path('productDetails/', views.product_details, name='productDetails'),
    path('api/', include('books.api_urls')), 
    

]
