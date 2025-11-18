from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {"form": form})


class UserLoginView(LoginView):
    template_name = 'user/login.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
