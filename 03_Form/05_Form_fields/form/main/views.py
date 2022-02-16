from django.shortcuts import render
from .forms import formFields

# Create your views here.
def index(request):
    form = formFields()
    template_name = 'main/index.html'
    context = {
        'form':form
    }
    return render(request,template_name,context)