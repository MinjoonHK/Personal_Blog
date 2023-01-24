from django.urls import path
from . import views

urlpatterns = [
    path('landing/', views.landing),
    path('about_me/', views.about_me),
    path('', views.landing),
    path('Contact/', views.Contact)
]