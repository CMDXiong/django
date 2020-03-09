from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, telephone, username, password, **kwargs):
        if not telephone:
            raise ValueError('必须要传递手机号码')
        if not password:
            raise ValueError('必须要传递密码')
        user = self.model(telephone=telephone, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone=telephone, username=username, password=password, **kwargs)

    def create_superuser(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone=telephone, usernane=username, password=password, **kwargs)


class MyUser(AbstractUser):
    telephone = models.CharField(max_length=11, unique=True)
    school = models.CharField(max_length=100)

    # USERNAME_FIELD指定的字段，为以后authenticate验证的字段
    USERNAME_FIELD = 'telephone'

    # 重新定义Manager对象，在创建user的时候使用telephone和password
    objects = UserManager()