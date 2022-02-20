from django.shortcuts import render
from .forms import registration


# Create your views here.
def home(request):
    data = ""
    if request.method == 'POST':
        form = registration(request.POST)
        if form.is_valid():
            data = form.cleaned_data
    else:
        form  = registration()
    template_name = 'main/index.html'
    context={
        'form':form,
        'data':data,
    }
    return render(request,template_name,context)