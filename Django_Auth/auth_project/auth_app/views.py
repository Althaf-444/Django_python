from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.
def register_viwe(request):
    if request.method == "POST":
      form = RegisterForm(request.POST)
      if form.is_valid():
          user_name = form.cleaned_data.get("username")
          password = form.cleaned_data.get("password")
          user = User.objects.create_user(usename=user_name,password= password)
          login(request , user)
          return redirect('home')
      else:
          form = RegisterForm()
          return render(request , 'accounts/register.html',{'form':form})


def login_viwe(request):
    if request.method == 'POST':
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = user_name , password = password  )
        

def logout_viwe(request):
    pass

@login_required
def home(request):
    pass