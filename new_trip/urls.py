from django.urls import path
from . import views

app_name = "new_trip"
urlpatterns = [
    path("new_trip/", views.create_trip_view, name="create_trip"),

]