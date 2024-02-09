from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import LaptopForm
from .models import Laptop
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signin_url')
def form_view(request):
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrieve_url')
    template_name='crud_app/laptop_form.html'
    context = {'form':form}
    return render (request, template_name, context)

@login_required(login_url='signin_url')
def lap_retrieve_view(request):
    objs = Laptop.objects.all()
    template_name = 'crud_app/Laptop_list.html'
    context = {'data':objs}
    return render (request, template_name, context)

def lap_delete_view(request, pk):
    obj = Laptop.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('retrieve_url')
    context = {'obj':obj}
    template_name = 'crud_app/laptop_delete_confirmation.html'
    return render(request, template_name, context)

def lap_update_view(request, pk):
    obj = Laptop.objects.get(id=pk)
    up = LaptopForm(instance=obj)
    if request.method == 'POST':
        up = LaptopForm(request.POST, instance=obj)
        if up.is_valid():
            up.save()
            return redirect ('retrieve_url')
    template_name = 'crud_app/laptop_form.html'
    context = {'form':up}
    return render (request, template_name, context)

