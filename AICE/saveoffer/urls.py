from django.urls import path ,include
from django.contrib import admin
from . import views

urlpatterns=[
    path('test', views.save_offer),
    path('<int:pk>/', views.Offer_Detail)
]