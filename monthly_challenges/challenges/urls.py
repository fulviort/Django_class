from django.urls import path
from . import views

# we have different ways of connecting urls, dynamic way with a main name, or 1 by 1.

urlpatterns = [
    path("test1", views.test1),
    path("test2", views.test2),
    path("test3", views.test3),
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]