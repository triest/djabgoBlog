from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from inspect import getmembers
from pprint import pprint
from articles.models import Subscribe;
from django.forms import modelform_factory
from django import forms
from django.contrib.auth.models import User;
from . import models


class SunscribeForm(forms.ModelForm):
    # add a field to select a car
  #  users = forms.ModelChoiceField(Users.objects.all())

    class Meta:
        model = models.Subscribe
        fields = ['name','owner', 'Subscribers']

        def __init__(self, *args, **kwargs):
            brand = kwargs.pop("brand")
            super(IngredientForm, self).__init__(*args, **kwargs)
            self.fields["Subscribers"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["Subscribers"].help_text = ""
            self.fields["'Subscribers'"].queryset = Users.objects.all()
