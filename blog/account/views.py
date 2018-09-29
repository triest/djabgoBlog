from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout;
# Create your views here.

def singup_view(request):
    return render(request,'account/login.html')

def login_view(request):

    if request.method=='POST':
        form=AuthenticationForm(data=request.POST);
        if(form.is_valid()):
            user=form.get_user();
            login(request,user)
            return redirect('articles:list')

    else:
        form=AuthenticationForm();
        return render(request,'account/login.html',{'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')
