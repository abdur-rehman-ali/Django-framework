from django.shortcuts import render
from .forms import studentRegistration

# Create your views here.
def home(request):
    form = studentRegistration()
    template_name = 'main/index.html'
    context={
        'form':form
    }
    return render(request,template_name,context)