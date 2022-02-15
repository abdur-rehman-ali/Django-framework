from django.shortcuts import render
from .forms import InputForm

# Create your views here.
def index(request):
    form = InputForm()
    template_name='main/index.html'
    context={
        'form':form
    }
    return render(request,template_name,context)