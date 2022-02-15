from django.shortcuts import render
from .forms import InputForm

# Create your views here.
def index(request):
    form = InputForm(label_suffix=' ',auto_id='main_%s')
    form.order_fields(['name','password','reg'])
    template_name='main/index.html'
    context={
        'form':form
    }
    return render(request,template_name,context)