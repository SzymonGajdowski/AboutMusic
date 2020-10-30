from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('post/', views.detail_view, name='detail_view'),
    path('about/', views.about_view, name='about_view'),
    path('contact/', views.contact_view, name='contact_view'),
]