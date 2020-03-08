from django.db import models
from django.core import validators


class Book(models.Model):
    class Meta:
        db_table = 't_book'
    title = models.CharField(max_length=100)
    page = models.IntegerField()
    # 为price字段添加验证器
    price = models.FloatField(validators=[validators.MaxValueValidator(limit_value=100)])


class User(models.Model):
    class Meta:
        db_table = 't_user'
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
    telephone = models.CharField(max_length=11, validators=[validators.RegexValidator(
        r'1[3456789]\d{9}')])

