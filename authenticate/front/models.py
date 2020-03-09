from django.db import models
from django.contrib.auth.models import User


# 设置proxy模型
# proxy模型中不能添加任何其它的Field，但可以添加其他的属性
class Person(User):
    # 不能添加telephone字段
    # telephone = models.CharField(max_length=11)
    class Meta:
        proxy = True

    @classmethod
    def get_blacklist(cls):
        return cls.objects.filter(is_active=False)


