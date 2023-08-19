from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
# @login_required 
def CreatePost(request):
    print(request)
    if request.user.is_authenticated and request.method == 'POST':
        print(request.POST)
        print(request.user)
        context = request.POST
        postObj = Post()
        postObj.user = request.user
        postObj.post = context['post']
        postObj.save()
        return redirect('post-list')

    return render(request, 'post/post_create.html')

def ListPost(request):    
    post_list = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts' : post_list})    



