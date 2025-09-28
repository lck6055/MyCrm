from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import UserSignUp


# Create your views here.
def home(request):
    return render(request,'website/home.html')



def login_def(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Please provide both username and password')
    return render(request, 'website/login.html')

def logged_out(request):
    logout(request)
    return redirect('login')

#signup
def registered(request):
    if request.method == 'POST':
        form = UserSignUp(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,'Account Successfully Created')
            return redirect('login')
    else:
        form = UserSignUp()
    return render(request, 'website/register.html', {'form': form})