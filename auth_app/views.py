from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def sighup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_url')
    template_name = 'auth_app/signup_form.html'
    context = {'form' : form}
    return render(request, template_name, context)


def signin_view(request):
    if request.method == 'POST':
        un = request.POST.get('uname')
        pw = request.POST.get('passw')

        user = authenticate(username=un, password=pw)
        print(f"user----{user}")

        if user is not None:
            login(request, user)
            return redirect('retrieve_url')

    template_name = 'auth_app/signin_form.html'
    context = {}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('signin_url')
