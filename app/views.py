from django.contrib.auth import logout
from django.shortcuts import redirect, render
# from django.contrib.auth.decorators import login_required
from .models import post
from .forms import blog_form
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


def edit(request):
    context={'data':post.objects.all()}
    return render(request,'app/edit_blog.html',context)

def update(request,slug):
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


def delete(request,id):
    obj=post.objects.get(id=id)
    if obj.user==request.user:
        obj.delete()
        return redirect('/edit')
    return redirect('/')
        