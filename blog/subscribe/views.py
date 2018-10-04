from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from inspect import getmembers
from pprint import pprint
from .models import Subscribe
from django.forms import modelform_factory
from .models import Subscribe
from . import forms
from django.contrib.auth.models import User;

# Create your views here.
@login_required(login_url="/account/login")
def main(request):
    current_user = request.user
    #получаем инстанс subscribe авторизованного пользователя
    subscribe=Subscribe.objects.get(owner=current_user)
    users = subscribe.subscription.all()

    #

    return render(request,'test.html',{'users':users})

