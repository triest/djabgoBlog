from django.contrib import admin
from .models import Article
#from .models import Subscribe
# Register your models here.
from blog.subscribe import Subscribe

admin.site.register(Article)
admin.site.register(Subscribe)