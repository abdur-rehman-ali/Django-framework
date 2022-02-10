from django.shortcuts import render
from .models import studentRegistration
# Create your views here.
def main(request):
    student_data = studentRegistration.objects.all()
    template_name = 'main/index.html'
    context = {
        'data':student_data,
    }
    return render(request,template_name,context)