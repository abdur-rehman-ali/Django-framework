from django.shortcuts import render
from .forms import registration


# Create your views here.
def home(request):
    form  = registration()
    template_name = 'main/index.html'
    context={
        'form':form
    }
    return render(request,template_name,context)