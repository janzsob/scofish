from django.urls import path
from . import views

app_name = "trips_feed"
urlpatterns = [
    path("horgászatok/", views.FeedView.as_view(), name="feed"),
    path("", views.HomeView.as_view(), name="home"),
]