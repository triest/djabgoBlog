from django.db import models
from django.contrib.auth.models import User;

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=30);
    description=models.TextField();
    date=models.DateTimeField(auto_now_add=True);
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title;

    def snipped(self):
        return self.description[:50]+'...'