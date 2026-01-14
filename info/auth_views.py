from django.shortcuts import render, redirect


def register(request):
    return render(request, "auth/register.html")


def login(request):
    return render(request,"auth/login.html")


def logout(request):
    return redirect('login')

