from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages


def hello(request):
    return render(request, "hello.html", context={})


def register_view(request):
    form = CreateUserForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get("username")
        messages.success(request, f"The account was created for {user}")
        return redirect("auth:login")

    context = {"form": form}
    return render(request, "authentication/register.html", context)


def login_view(request):
    if request.user.is_authenticated: # detect if user is logged in
        messages.info(request, "You're already logged in.")
        return redirect("auth:home")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("auth:home")
        else:
            messages.error(request, "Username or password is incorrect.")
    context= {}
    return render(request, "authentication/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("auth:login")
