from django.urls import path
from . import views

urlpatterns = [
     
    path('getItems/', views.getItems, name='getItems'),
    path('greeting/', views.greeting, name='greeting'),
    path('base/', views.baseHTML, name='baseHTML'),
]