# -*- coding:utf-8 -*-
__author__ = 'px'

from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=16, min_length=6)

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError(message="再次密码不一致")
        return cleaned_data

    class Meta:
        model = User
        fields = "__all__"


class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']






