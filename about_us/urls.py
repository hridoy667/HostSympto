from django.urls import path
from . import views

urlpatterns = [
    path('ab_us/', views.about,name='about'),
]