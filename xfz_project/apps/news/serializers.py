# -*- coding:utf-8 -*-
__author__ = 'px'


from rest_framework import serializers
from .models import NewCategory, News, Comment
from apps.xfzauth.serializers import UserSerializer


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCategory
        fields = ('id', 'name')


class NewsSerializer(serializers.ModelSerializer):
    category = NewsCategorySerializer()
    author = UserSerializer()

    class Meta:
        model = News
        fields = ('id', 'title', 'desc', 'thumbnail', 'pub_time', 'category', 'author')


class CommentSerizlizer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'pub_time')

