from django.urls import path
from . import views

urlpatterns = [
    path("", views.all),
    path("add", views.add),
    path("<int:id>", views.details),
]
