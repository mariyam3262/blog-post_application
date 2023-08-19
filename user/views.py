from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, loginForm

# views.py

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user is not None:
            login(request,user)
            return redirect('post-list')
    form = loginForm()
    return render(request, 'signin.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('user:login')


def profile(request):
    profile = profile.objects.get(username = request.user)
    print(profile)
    return render(request, 'post/post_list.html')