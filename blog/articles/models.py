from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=30);
    description=models.TextField();
    date=models.DateTimeField(auto_now_add=True);
   # author=models.

    def __str__(self):
        return self.title;