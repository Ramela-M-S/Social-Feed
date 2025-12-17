from django.shortcuts import render, redirect
from .forms import RegistrationForm
# Create your views here.
def register_view(request):
    form = RegistrationForm(request.POST)
    if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            print("Form Errors:", form.errors)
    else:
        form = RegistrationForm()
    
    return render(request, "register/register.html",{"form":form})