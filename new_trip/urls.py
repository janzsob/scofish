from django.urls import path
from . import views

app_name = "new_trip"
urlpatterns = [
    path("új_horgászat/", views.CreateTripView.as_view(), name="create_trip"),
    path("horgászat/<int:pk>/", views.TripDetailView.as_view(), name="trip_details"),
    path("horgászat/<int:pk>/új_fogás/", views.NewCatchView.as_view(), name="new_catch"),
    path("horgászat/<int:pk>/szerkesztés/", views.TripUpdateView.as_view(), name="edit_trip"),
    path("ajax/load-hookbaits/", views.load_hookbaits, name="ajax_load_hookbaits"), # for ajax
]