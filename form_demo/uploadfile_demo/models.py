from django.db import models
from django.core import validators


class Article(models.Model):
    class Meta:
        db_table = 't_article'
    title = models.CharField(max_length=100)
    content = models.TextField()
    # thumbnial = models.FileField(upload_to='media')
    # thumbnial = models.FileField(upload_to='%Y/%m/%d')
    thumbnial = models.FileField(upload_to='%Y/%m/%d', validators=[validators.FileExtensionValidator(
        ['txt', 'pdf'], message="thumbnial必须为txt或者pdf文件")])

