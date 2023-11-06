from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        Username=request.POST['username']
        Email=request.POST['email']
        password1=request.POST['password']
        user=User.objects.create(username=Username,email=Email,password=password1)
        user.save()
        print("user created")
        return redirect('/')
    else:
        return render(request,'signUp.html')

