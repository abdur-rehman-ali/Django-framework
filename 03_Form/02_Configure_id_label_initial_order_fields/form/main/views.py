from django.shortcuts import render
from .forms import studentRegistration

# Create your views here.


def home(request):
    initial_values={
        'name':'Ali joiya',
        'reg':2018030
    }
    form = studentRegistration(auto_id=False, initial=initial_values)
    form1 = studentRegistration(auto_id='main_%s', label_suffix='#')
    form2 = studentRegistration(auto_id='main', label_suffix='')
    form2.order_fields(['reg','name'])
    template_name = 'main/index.html'
    context = {
        'form': form,
        'form1': form1,
        'form2': form2,
    }
    return render(request, template_name, context)
