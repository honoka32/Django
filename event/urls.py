from django.urls import path

from . import views

urlpatterns = [
    path("/event", views.index, name="index"),
]
