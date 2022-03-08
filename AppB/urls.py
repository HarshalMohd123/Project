from django.urls import path
from .import views

urlpatterns = [
   path('djang',views.AppC),
   path('html',views.function),
   path('httml',views.function)
]