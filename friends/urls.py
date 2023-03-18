from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'friends'
urlpatterns = [
  path("", views.index, name="index"),
  path("create", views.create, name="create"),
  path("save", views.save, name="save"),
  path("<int:friend_id>/show", views.show, name="show"),
  path("<int:friend_id>/delete", views.delete, name="delete"),
  path("<int:friend_id>/edit", views.edit, name="edit"),
  path("<int:friend_id>/update", views.update, name="update")
]