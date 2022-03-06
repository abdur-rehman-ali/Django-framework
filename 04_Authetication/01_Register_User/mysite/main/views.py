from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    data = User.objects.all()
    template_name = 'main/index.html'
    context = {
        'data':data
    }
    return render(request,template_name,context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserCreationForm()
    else:    
        form = UserCreationForm()
    template_name = 'main/register.html'
    context = {
        'form':form
    }
    return render(request,template_name,context)

