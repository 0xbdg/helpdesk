from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from .forms import LoginForm, ProblemForm, UpdateProfile,ChangePasswordForm
from .models import Ticket, User
# Create your views here.

@login_required
def index(request):
    form = ProblemForm(data=request.POST)
    user = User.objects.get(username=request.user.get_username())
    ticket = Ticket.objects.all()
    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data["title"]
            desc = form.cleaned_data["description"]
            date = form.cleaned_data["date"]

            Ticket(client=user, problem=title, description=desc, status="process", date=date).save()
            return redirect("index")
    
    return render(request, "pages/index.html", context={"form":form, "tickets":ticket})

def signin(request):
    if request.user.is_authenticated:
        return redirect("index")

    form = LoginForm(data=request.POST)

    if form.is_valid():
        login(request, form.get_user())
        return redirect("index")

    return render(request, "pages/account/login.html", context={"form":form})

@login_required
def profile(request):
    if request.method == "POST":
        form = UpdateProfile(data=request.POST, instance=request.user)
        form2 = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
        
        elif form2.is_valid():
            user = form2.save()
            update_session_auth_hash(request,user)
            return redirect("password_change_done")

    else:
        form = UpdateProfile(instance=request.user)
        form2 = ChangePasswordForm(user=request.user)
    
    return render(request, "pages/account/settings.html", context={"form":form,"form2":form2})

@login_required
def signout(request):
    logout(request)
    return redirect("login")