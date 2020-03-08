# encoding: utf-8

from .models import Book, User
from django import forms


class AddBookForm(forms.ModelForm):
    # 针对page字段进行深度验证（自定义验证器）
    def clean_page(self):
        page = self.cleaned_data.get('page')
        print(type(page))
        if page > 100:
            raise forms.ValidationError("页码不能超过100")
        return page

    class Meta:
        model = Book
        # fields和exclude必须定义一个
        # 1. 指定为__all__: 运用Book模型中所有字段
        fields = "__all__"
        # 2. 指定部分字段示例：
        # fields = ['title', 'page']
        # 3. 排除指定字段
        # exclude = ['price']
        # 4. 自定义报错信息
        error_messages = {
            'page': {
                'required': "请传入page参数",
                'invalid': "请输入一个可用的page参数"
            },
            'title': {
                'max_length': 'title不能超过100个字符'
            },
            'price': {
                'max_value': '图书价格不能超过100元'
            }
        }


class RegisterForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    def clean(self):
        # 如果来到了clean方法， 说明之前每一个字段都验证成功了
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message="两次密码输入不一致！")
        return cleaned_data

    class Meta:
        model = User
        exclude = ['password']
