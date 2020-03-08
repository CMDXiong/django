
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        # error_messages = {
        #     'thumbnial': {
        #         'invalid_extension': '请上传正确格式的图片！',
        #         'invalid_image': '请上传正确格式的图片！'
        #     }
        # }
