from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def article_list(requwest):
    return render(requwest,"articles/article_list.html")