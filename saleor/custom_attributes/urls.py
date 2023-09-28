from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_custom_attributes, name="list-custom-attributes"),
]