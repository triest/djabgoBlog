from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from subscribe.models import Subscribe;
from . import forms
# Create your views here.

#app_name='articles'

def article_list(requwest):
    articles=Article.objects.all().order_by('-date')
    return render(requwest,"articles/article_list.html",{'articles':articles})

def article_detail(requwest,id):
    article=Article.objects.get(pk=id)
    return render(requwest,'articles/detail.html',{'article':article})
    #return HttpResponse(pk)

@login_required(login_url="/account/login")
def article_create(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST,)
        if form.is_valid():
            instance=form.save(commit=True)
            instance.author=request.user
            instance.save()
            return article_list(request)
          #  return redirect('articles:list')
    else:
        form=forms.CreateArticle()
    return render(request,'articles/article_create.html',{'form':form})

def article_create2(request):
    form = forms.CreateArticle()
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, )
        if form.is_valid():
            instance =form.save(commit=True)
            instance.author=request.user
            instance.save()
            article_list(request)

    else:
        form = forms.CreateArticle()

    return render(request, 'articles/article_create2.html', {'form': form})


@login_required(login_url="/account/login")
def sunscribe(request,id):
    #return article_list(request);
    #id -id пользователя
    user=User.objects.get(pk=id) #article author
    #ищем подпису с ютим пользователем
    #article=Article.objects.get(pk=id)
    try:
        sunscribe1=Subscribe.objects.get(owner=request.user)
    except Subscribe.DoesNotExist:
        sunscribe1 = Subscribe();
        sunscribe1.name=request.user; #задаем имя
        sunscribe1.owner = request.user
   # if sunscribe1==None:
    #
   # sunscribe1 = Subscribe()
   # sunscribe1.owner=request.user; #задаем владельцы
    sunscribe1.save();
    return article_list(request);
   # print("ok");
   # return articl
# e_list(request)