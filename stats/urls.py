from django.urls import path
from . import views

app_name = "stats"
urlpatterns = [
    path("statistics/<int:pk>/", views.StatView.as_view(), name="trip_stat"),

]