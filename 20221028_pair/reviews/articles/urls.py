from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:article_pk>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("<int:article_pk>/update/", views.update, name="update"),
    path("<int:article_pk>/comment/", views.comment_create, name="comment_create"),
    path(
        "<int:article_pk>/comment/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    path("<int:article_pk>/like/", views.like, name="like"),
    path('search/', views.search, name='search'),
    path("<int:article_pk>/delete/", views.delete, name="delete"),
    
]
