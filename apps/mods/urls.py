from django.urls import path

from .views import mod_list

urlpatterns = [
    path("", mod_list, name="mod_list"),
]