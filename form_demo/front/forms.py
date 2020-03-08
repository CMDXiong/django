# encoding:utf-8

from django import forms
from django.core import validators
from .models import User


class BaseForm(forms.Form):
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key, message_dicts in errors.items():
            messages = []
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors


# Django中表单渲染功能示例
class MessageBoardForm(BaseForm):
    title = forms.CharField(max_length=100, min_length=2, label="标题",
                            error_messages={"min_length": "最少不能少于2个字符！"})
    content = forms.CharField(widget=forms.Textarea, label="内容")
    email = forms.EmailField(label="邮箱")
    reply = forms.BooleanField(required=False, label="是否回复")


# 常用验证器使用示例
class MyForm(BaseForm):
    phone = forms.CharField(validators=[validators.RegexValidator(r'1[3456789]\d{9}', message="请输入正确格式的手机号码")])
    # email = forms.EmailField(validators=[validators.EmailValidator(message="请输入正确格式的邮箱")])
    email = forms.EmailField(error_messages={"invalid":"请输入正确格式的邮箱"})
    # price = forms.FloatField(error_messages={"invalid": "请输入浮点类型"})


# 自定义验证器示例
class RegisterForm(BaseForm):
    username = forms.CharField(max_length=100)
    telephone = forms.CharField(validators=[validators.RegexValidator(
        r'1[3456789]\d{9}', message="请输入正确格式的手机号码")])
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    # 针对telephone字段，再进行一层验证,当调用is_valid函数时，会自动调用以clean_字段的函数进行验证
    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone)
        if exists:
            raise forms.ValidationError(message="%s已经被注册!" % telephone)
        # 如果验证没有问题，一定要记得把telephone返回回去
        return telephone

    def clean(self):
        # 如果来到了clean方法， 说明之前每一个字段都验证成功了
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message="两次密码输入不一致！")
        return cleaned_data



