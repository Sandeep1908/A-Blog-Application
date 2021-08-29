from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app/blog.html')

def login_view(request):
    return render(request,'app/login.html')


def register_view(request):
    return render(request,'app/register.html')