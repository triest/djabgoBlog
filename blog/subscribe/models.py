from django.db import models
from django.contrib.auth.models import User;

# Create your models here.
class Subscribe(models.Model):
   name=models.CharField(max_length=30,null=False);
  # subscribed_user=models.OneToOneField(User, on_delete=models.PROTECT)# владелец
   owner=models.ForeignKey(User,related_name='owner', null=False, blank=True, on_delete=models.PROTECT)# владелец подписки
   subscription = models.ManyToManyField(User,null=True,related_name='subscription') #те, на кого он пдписалса