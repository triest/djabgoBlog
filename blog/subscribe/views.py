from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from inspect import getmembers
from pprint import pprint
from .models import Subscribe
from django.forms import modelform_factory
from .models import Subscribe
from .models import Read
from . import forms
from django.contrib.auth.models import User;
from articles.models import Article

# Create your views here.
@login_required(login_url="/account/login")
def main(request):
    current_user = request.user
    #получаем инстанс subscribe авторизованного пользователя
    subscribe=Subscribe.objects.get(owner=current_user)
    users = subscribe.subscription.all()
    articles=Article.objects.all()
    #теперь фильтруем
    list=[x for x in articles if x.author  in users]

    return render(request,'test.html',{'users':users,'articles':list})


def article_detail(request,id):
    article=Article.objects.get(pk=id)
    # тут будет проверка на то, подписан ли, по

    answer = "sub"
    try:
        sunscribe = Subscribe.objects.get(owner=request.user, sunscribe=article.author);
    except:
        answer = "not_sub"


    return render(request,'detail.html',{'article':article,'answer':answer})

def mark_readed(request,id):
    #id -идентификатор статьи
    user =request.user # подписант
    try:
        reader = Read.objects.get(owner_reader=request.user)  #проверяем, есть ли обьект
    except Read.DoesNotExist:
        reader = Read.objects.create(owner_reader=request.user)
    #добавляем пост в прочитанные
#    reader.articles_readed.add=Article.objects.get(pk=id)
   # reader.save();
    return main(request)