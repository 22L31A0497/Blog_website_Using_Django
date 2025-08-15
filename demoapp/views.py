from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog,Blog1
# Create your views here.
from datetime import datetime
from django.core.management import call_command

# def home(request):
#     return HttpResponse("This is my first app")
    
# def fapp(request):
#     return HttpResponse("This is another function from the Django app")

def blogpage(request):
    post = Blog.objects.all()
    return render(request,"base.html",{'post':post})

# def blogVideo(request):
#     post= Blog1.objects.all()
#     return render(request, "index.html",{'post':post})

def blogVideo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")
        video = request.FILES.get("video")
        description = request.POST.get("description")
        author = request.POST.get("author")

        Blog1.objects.create(
            title=title,
            image=image,
            video=video,
            description=description,
            author=author,
            created_at=datetime.now()
        )
        return redirect('blogvideo')  # reload the page after save

    post = Blog1.objects.all().order_by("-created_at")
    return render(request, "index.html", {'post': post})

from django.shortcuts import get_object_or_404, redirect

def delete_blog(request, pk):
    blog = get_object_or_404(Blog1, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blogvideo')  # your listing page
# demoapp/views.py


def run_migrations(request):
    call_command('migrate')
    return HttpResponse("Migrations completed!")
