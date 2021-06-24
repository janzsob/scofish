from django.urls import path
from . import views

app_name = "user_profile"
urlpatterns = [
    path("profile/<int:pk>/", views.ProfileView.as_view(), name="profile"),
    path("trips/<int:pk>/", views.UserTripsView.as_view(), name="user_trips"),
    path("catches/<int:pk>/", views.UserCatchesView.as_view(), name="user_catches"),
    #path("hookbait/create/", views.HookBaitCreateView.as_view(), name="hookbait_create"),
    #path("profile/<int:pk>/hookbait/update/", views.HookBaitUpdateView.as_view(), name="hookbait_update"),
]