from django.urls import path
from . import views

urlpatterns = [
    path("", views.categories),  # /GET
    path("<int:pk>", views.category),  # /GET
]
