from django.shortcuts import render
from django.contrib.auth.forms  import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect


def index(request):
    return render(request,'signup/base.html')


def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('/')
    else:
        form=UserCreationForm()
    return render(request,'signup/signup.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('/')
    else:
        form=AuthenticationForm()
    return render(request,'signup/login.html',{'form':form})















