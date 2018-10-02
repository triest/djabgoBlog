from django.db import models
from django.contrib.auth.models import User;

# Create your models here.
class Subscribe(models.Model):
   name=models.CharField(max_length=30,null=False);
   subscribed_user=models.OneToOneField(User, on_delete=models.PROTECT)
   owner=models.ForeignKey(User,related_name='owner', null=False, blank=True, on_delete=models.PROTECT)
   subscription = models.ManyToManyField(User,related_name='subscription')