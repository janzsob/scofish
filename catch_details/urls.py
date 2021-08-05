from django.urls import path
from . import views

app_name = "catch_details"
urlpatterns = [
    path("fogás/<int:pk>/", views.CatchView.as_view(), name="catch"),
    path("fogás/<int:pk>/szerkesztés/", views.CatchUpdateView.as_view(), name="catch_update"),
    path("fogás/<int:pk>/törlés/", views.CatchDeleteView.as_view(), name="catch_delete"),
]