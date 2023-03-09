from django.urls import path
from . import views

app_name = 'friends'
urlpatterns = [
  path("", views.index, name="index"),
  path("<int:friend_id>/show", views.show, name="show")
]