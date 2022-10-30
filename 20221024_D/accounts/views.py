from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("reviews:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "reviews:index")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("reviews:index")


@login_required
def profil(request, user_pk):
    if request.user.pk == user_pk:
        user = User.objects.get(pk=user_pk)
        context = {
            "user": user,
        }
        return render(request, "accounts/profil.html", context)
    else:
        return redirect("accounts:index")


def follow(request, user_pk):
    if request.user.pk == user_pk:
        messages.success(request, "스스로 팔로우 할 수 없습니다 ㅜㅠ")
        return redirect("accounts:index")
    else:
        user = User.objects.get(pk=user_pk)
        if request.user in user.followings.all():
            user.followings.remove(request.user)
            return redirect("accounts:index")
        else:
            user.followings.add(request.user)
            return redirect("accounts:index")
