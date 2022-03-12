from django.urls import path
from .import views

urlpatterns = [
   path('python',views.function),
   path('',views.function1),
   path('sample',views.function2)
]