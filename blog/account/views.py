from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def singup_view(request):
    return render(request,'account/login.html')

def login_view(request):

    if request.method=='POST':
        form=AuthenticationForm(data=request.POST);
        if(form.is_valid()):
            return redirect('articles:list')

    else:
        form=AuthenticationForm();
        return render(request,'account/login.html',{'form':form})

