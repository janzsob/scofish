from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm, PasswordResetConfrimForm


app_name = "auth"
urlpatterns = [
    #path("", views.hello, name="home"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("contact/", views.contact_view, name="contact"),
    
    # urls for password reset
    path("reset_password/", auth_views.PasswordResetView.as_view(
        template_name="authentication/password_reset.html",
        success_url=reverse_lazy('auth:password_reset_done'),
        form_class=UserPasswordResetForm,
    ), name="password_reset"), # Submit email form

    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(
        template_name="authentication/password_reset_sent.html",
    ), name="password_reset_done"), # Email sent message

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('auth:password_reset_complete'),
        template_name="authentication/password_reset_form.html",
        form_class=PasswordResetConfrimForm,
    ), name="password_reset_confirm"), # Link to password in email

    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="authentication/password_reset_complete.html",
    ), name="password_reset_complete"), # Password changed message
]