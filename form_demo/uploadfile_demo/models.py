from django.db import models


class Article(models.Model):
    class Meta:
        db_table = 't_article'
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnial = models.FileField(upload_to='files')

