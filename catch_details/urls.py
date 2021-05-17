from django.urls import path
from . import views

app_name = "catch_details"
urlpatterns = [
    path("catch/<int:pk>/", views.CatchView.as_view(), name="catch"),
    path("catch/<int:pk>/edit", views.CatchUpdateView.as_view(), name="catch_update"),
    path("catch/<int:pk>/delete", views.CatchDeleteView.as_view(), name="catch_delete"),
]