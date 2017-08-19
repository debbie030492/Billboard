from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post



def index(request):
    posts = Post.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/index.html',{'posts':posts})

def newpost(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    text = request.POST.get('text')
    new_post = Post(author=author, title=title, text=text)
    new_post.save()
    context = {'new_post':new_post}
    return redirect('index')