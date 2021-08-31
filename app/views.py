from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request,'app/blog.html')

def login_view(request):
    return render(request,'app/login.html')


def register_view(request):
    return render(request,'app/register.html')

def logout_view(request):
    logout(request)
    return redirect('/login')