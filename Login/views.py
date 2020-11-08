from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.



def login(request):
    if request.method == 'POST':
     username1 = request.POST['username']
     password1 = request.POST['password']
     x = auth.authenticate(username=username1,password =password1)
     if x is not None:
         return redirect('details')
     else:
         print("Try again")
         return redirect(login)
    else:
     return render(request, "./login.html")
def home(request):
    return render(request,"./home.html")
def signup(request):
   return render(request, "./signup.html")
def details(request):
   return render(request, "./details.html")