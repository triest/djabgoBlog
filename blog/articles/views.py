from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

app_name='articles'

def article_list(requwest):
    articles=Article.objects.all().order_by('date')
    return render(requwest,"articles/article_list.html",{'articles':articles})

def article_detail(requwest,pk):
    article=Article.objects.get(pk=pk)
    return render(requwest,'articles/detail.html',{'article':article})
    #return HttpResponse(pk)

@login_required(login_url="/account/login")
def article_create(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST,)
        if form.is_valid():
            form.save(commit=True)
            #instance.author=request.user
            #instance.save()

            return redirect('articles:list')
    else:
        form=forms.CreateArticle()
    return render(request,'articles/article_create.html',{'form':form})
