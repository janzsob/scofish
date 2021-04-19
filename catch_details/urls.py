from django.urls import path
from . import views

app_name = "catch_details"
urlpatterns = [
    path("catch/<int:pk>/", views.CatchView.as_view(), name="catch"),
]