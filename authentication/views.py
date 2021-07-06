from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.core.mail import send_mail


"""
def hello(request):
    return render(request, "hello.html", context={})
"""

def register_view(request):
    form = CreateUserForm(request.POST or None)
    print(form.errors.as_data())
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get("username")
        messages.success(request, f"Sikeres regisztráció. Jelentkezzen be!")
        return redirect("auth:login")

    context = {"form": form}
    return render(request, "authentication/register.html", context)


def login_view(request):
    if request.user.is_authenticated: # detect if user is logged in
        messages.info(request, "Már be van jelentkezve.")
        return redirect("trips_feed:feed")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("trips_feed:feed")
        else:
            messages.error(request, "A felhasználónév vagy a jelszó helytelen.")
    context= {}
    return render(request, "authentication/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("auth:login")

"""
class ContactView(FormView):
    template_name = 'authentication/contact.html'
    form_class = CreateUserForm
    #success_url = '/thanks/'
"""

def contact_view(request):
    if request.method == "POST":
        message_name = request.POST.get("name")
        message_email = request.POST.get("email")
        message_subject = request.POST.get("subject")
        message_text = request.POST.get("message")

        # send an email
        send_mail(
            message_subject, # subject
            message_text, # message
            message_email, # from
            ['bence.janzso@gmail.com'], # to
        )
        messages.success(request, f"Köszönjük az üzeneted! Hamaorsan felvesszük veled a kapcsolatot.")

        return render(request, "authentication/contact.html", )

    context = {}
    return render(request, "authentication/contact.html", context)