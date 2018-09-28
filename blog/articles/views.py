from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

def article_list(requwest):
    articles=Article.objects.all().order_by('date')
    return render(requwest,"articles/article_list.html",{'articles':articles})

def article_detail(requwest,pk):
    article=Article.objects.get(pk=pk)
    return render(requwest,'articles/detail.html',{'article':article})
    #return HttpResponse(pk)