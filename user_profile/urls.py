from django.urls import path
from . import views

app_name = "user_profile"
urlpatterns = [
    path("profil/<int:pk>/", views.ProfileView.as_view(), name="profile"),
    path("horgászatok/<int:pk>/", views.UserTripsView.as_view(), name="user_trips"),
    path("fogások/<int:pk>/", views.UserCatchesView.as_view(), name="user_catches"),
    #path("hookbait/create/", views.HookBaitCreateView.as_view(), name="hookbait_create"),
    path("profil/<int:pk>/csalik/", views.HookBaitUpdateView.as_view(), name="hookbaits"),
]