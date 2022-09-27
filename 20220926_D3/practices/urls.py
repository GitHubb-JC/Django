from django.urls import path
from . import views

urlpatterns = [
    path("is-odd-even/<int:_number>", views.index),
    path("index/", views.ping),
    path("pong/", views.pong),
    path("calculate/<int:a>/<int:b>", views.calc),
]
