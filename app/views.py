from django.contrib.auth import logout
from django.shortcuts import redirect, render
# from django.contrib.auth.decorators import login_required
from .models import post, profile
from .forms import blog_form
from .helper import send_confirmation
# Create your views here.

def home(request):
    obj = post.objects.all()
    return render(request, 'app/blog.html', {'obj': obj})


def login_view(request):
    return render(request, 'app/login.html')


def register_view(request):
    return render(request, 'app/register.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def see_blog(request, slug):
    context = {}
    try:
        obj = post.objects.get(slug=slug)
        context['data'] = obj
    except Exception as e:
        print(e)

    return render(request, 'app/see_blog.html', context)


def addpost(request):
    if request.user.is_authenticated:
        context={'form':blog_form}
        try:
            if request.method=='POST':
                fm=blog_form(request.POST)
                title=request.POST['title']
                image=request.FILES['image']
                user=request.user
                if fm.is_valid():
                    content=fm.cleaned_data['content']
                obj=post.objects.create(title=title,content=content,image=image,user=user) 
                obj.save()
                return redirect('/')

        except Exception as e:
            print(e)   
        
        return render(request,'app/addpost.html',context)
    else:
        return redirect('/login')


def edit(request):
    if request.user.is_authenticated:
        context={'data':post.objects.all()}
        return render(request,'app/edit_blog.html',context)
    else:
        return redirect('/login')

def update(request,slug):
    if request.user.is_authenticated:
        data=post.objects.get(slug=slug)
        fm=blog_form(instance=data)
        if request.method=='POST':
            if data.user==request.user:
                fm=blog_form(request.POST)
                title=request.POST['title']
                image=request.FILES['image']
                if fm.is_valid():
                    content=fm.cleaned_data['content']
                data.title=title
                data.image=image
                data.content=content
                data.save()
                return redirect('/')
            else:
                return redirect('/')

        return render(request,'app/update.html',{'fm':fm})
    else:
        return redirect('/login')


def delete(request,id):
    if request.user.is_authenticated:
        obj=post.objects.get(id=id)
        if obj.user==request.user:
            obj.delete()
            return redirect('/edit')
        return redirect('/')
    else:
        return redirect('/login')

def verify(request,token):
    try:
        obj=profile.objects.get(token=token)
        if obj is not None:
            obj.is_varified=True
            obj.save()
    except Exception as e:
        print(e)
    return redirect('/login')
        