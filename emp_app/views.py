from django.shortcuts import render
from .models import Employee, Role, Department


# Create your views here.
def index(request):
    return render(request, 'index.html')


def viewemp(request):
    emp = Employee.objects.all()
    context={
        'emps': emp
    }
    return render(request, 'viewemp.html',context)


def addemp(request):
    return render(request, 'addemp.html')


def removeemp(request):
    return render(request, 'removeemp.html')


def filteremp(request):
    return render(request, 'filteremp.html')
