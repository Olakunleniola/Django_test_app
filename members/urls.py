from django.urls import path
from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("mychildren/", views.members, name="members"),
    path("mychildren/details/<str:name>", views.details, name="details"),
    path("testing/", views.test, name="test"),
]
