from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from subscribe.models import Subscribe;
from . import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

#app_name='articles'

def article_list(request):
    articles=Article.objects.all().order_by('-date')
    return render(request,"articles/article_list.html",{'articles':articles})

def article_detail(request,id):
    article=Article.objects.get(pk=id)
    # тут будет проверка на то, подписан ли, по

    answer = "sub"
    try:
        sunscribe = Subscribe.objects.get(owner=request.user, sunscribe=article.author);
    except:
        answer = "not_sub"



    return render(request,'articles/detail.html',{'article':article,'answer':answer})
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
    user=User.objects.get(pk=id) #article author
    try:
        sunscribe1=Subscribe.objects.get(owner=request.user)
    except Subscribe.DoesNotExist:
        sunscribe1 = Subscribe.objects.create(name='something', owner=request.user)
    sunscribe1.subscription.add(user)
    sunscribe1.save();
    # получаем статью по id

    return article_list(request);
   # print("ok");
   # return articl
# e_list(request)


#сигнал для отправки сообщений при добавлении поста пользоватеем (или через админку)

@receiver(post_save, sender=Article) #при добавлении статьи
def handle_new_job(sender, **kwargs):
    post = kwargs.get('instance') ; #пост, который добавили
    avtor=post.author # автор поста
    #теперь надо получить подписки, где в подписанных знач
    subscribe=Subscribe.objects.get( avtor in 'subscription') # список подписок, где есть этот автор

    # теперь в цикле обходим выбранные подписки, и направляем их владельцам mail
    for item in sunscribe:
        user=sunscribe.owner;
        send_mail(
            'New article',
            'Message.',
            'from@example.com',
            ['john@example.com', 'jane@example.com'],
        )

def testmail(requwest):
  #  post = kwargs.get('instance');  # пост, который добавили
  #  avtor = post.author  # автор поста
    # теперь надо получить подписки, где в подписанных знач
   # subscribe = Subscribe.objects.get(avtor in 'subscription')  # список подписок, где есть этот автор

    # теперь в цикле обходим выбранные подписки, и направляем их владельцам mail

    send_mail(
            'New article',
            'Message.',
            'sakura-testmail@sakura-city.info',
           ['triest21@gmail.com'],
            fail_silently=False,
        )
