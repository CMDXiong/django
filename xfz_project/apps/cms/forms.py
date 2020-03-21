# -*- coding:utf-8 -*-
__author__ = 'px'

from django import forms
from apps.news.models import News
from apps.forms import FormMixin


class EditNewsCategory(forms.Form):
    pk = forms.IntegerField(error_messages={"required": "必须传入分类的id!"})
    name = forms.CharField(max_length=100)


class WriteNewsForm(forms.ModelForm, FormMixin):
    category = forms.IntegerField()

    class Meta:
        model = News
        exclude = ['category', 'author', 'pub_time']

