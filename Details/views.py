from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from Signup.models import employee
def details(request):
    o1 = employee.objects.all()
    return render(request,"details.html",{'o1':o1})
def home(request):
   return render(request, "./home.html")