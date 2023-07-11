from django.shortcuts import render, redirect
from .models import blog
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'frontend/home.html')

def user_home(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        post_image = request.FILES['post_image']
        _blog = blog.objects.create(author=request.user.secretary, title = title, description = description, image = post_image)
        _blog.save()
        print('saved')
        messages.success(request, "Blog post added successfully")
        return redirect('user_home')
    else:
        blogs = blog.objects.all()

    context = {
        'blogs' : blogs
    }
    return render(request, 'backend/user.html', context)


def gallery(request):
    blogs = blog.objects.all()

    context = {
        'blogs' : blogs
    }
    return render(request, 'frontend/gallery.html', context)



def my_blog(request):
    blogs = blog.objects.all()

    context = {
        'blogs' : blogs
    }
    return render(request, 'frontend/blog.html',context)

def delete(request, id):
    blog.objects.get(pk=id).delete()
    return redirect('user_home')