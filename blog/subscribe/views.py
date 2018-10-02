from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from inspect import getmembers
from pprint import pprint

from django.forms import modelform_factory
from . import forms
from django.contrib.auth.models import User;

# Create your views here.
@login_required(login_url="/account/login")
def main(request):
    current_user = request.user
    #print(getmembers(current_user))
    #print (vars(current_user))
    #subscrive=Subscribe.objects.all();
   # subscribe=Subscribe.objects.all();
    #form = forms.SunscribeForm()
    return render(request,'test.html',{'user':current_user,'form':form})

