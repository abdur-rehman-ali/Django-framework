from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponseRedirect
from .forms import registration


# Create your views here.

def success(request):
    template_name = 'main/success.html'
    return render(request,template_name)

def home(request):
    if request.method == 'POST':
        form = registration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            context ={
                'name':name
            }
            return render(request,'main/success.html',context)
            # return HttpResponseRedirect('/success/')
    else:
        form  = registration()
    template_name = 'main/index.html'
    context={
        'form':form,
    }
    return render(request,template_name,context)