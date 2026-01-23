from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import RegisterForm, EmailAuthenticationForm, ProfileForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = EmailAuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("home")

    return render(request, "accounts/login.html", {"form": form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # 1. create user
            user = user_form.save()

            # 2. create profile with real data
            profile = Profile(user=user)
            for field, value in profile_form.cleaned_data.items():
                setattr(profile, field, value)
            profile.save()

            # 3. login user
            login(request, user)

            return redirect("profile")
    else:
        user_form = RegisterForm()
        profile_form = ProfileForm()

    return render(request, "accounts/register.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })

@login_required
def profile_view(request):
    # safety: ensure profile exists (for admin-created users etc.)
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "accounts/profile.html", {
        "form": form
    })

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")  