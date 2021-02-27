from django.shortcuts import render


def hello(request):
    return render(request, "authentication/hello.html", context={})
