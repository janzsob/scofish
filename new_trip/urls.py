from django.urls import path
from . import views

app_name = "new_trip"
urlpatterns = [
    path("new_trip/", views.create_trip_view, name="create_trip"),
    path("trip_details/<int:pk>/", views.TripDetailView.as_view(), name="trip_details"),
    path("trip_details/<int:pk>/new_catch/", views.NewCatchView.as_view(), name="new_catch"),
    path("catch/<int:pk>/", views.CatchView.as_view(), name="catch"),

]