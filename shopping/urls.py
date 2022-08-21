from django.urls import path
from shopping import views
urlpatterns =[
    path('',views.home,name='home'),
    path('seller_place/',views.sellerinfo,name='sellerinfo'),
]