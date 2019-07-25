import datetime

from django.db import models

from lib.mixin import ModelMixin
# Create your models here.

class User(models.Model):
    SEX = (
        ('female', 'female'),
        ('male', 'male')
    )
    phonenum = models.CharField(max_length=32, unique=True, verbose_name='手机号')
    nickname = models.CharField(max_length=128, unique=True, verbose_name='昵称')
    sex = models.CharField(max_length=8, choices=SEX, verbose_name='性别')
    birth_year = models.IntegerField(default=2000, verbose_name='出生年')
    birth_month = models.IntegerField(default=1, verbose_name='出生月')
    birth_day = models.IntegerField(default=1, verbose_name='出生日')
    avatar = models.CharField(max_length=256, verbose_name='个人形象')
    location = models.CharField(max_length=64, verbose_name='常居地')

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'<User {self.nickname}>'

    @property
    def age(self):
        """根据出生年月日,计算年龄"""
        now = datetime.datetime.now()
        birthday = datetime.datetime(year=self.birth_year,
                month=self.birth_month, day=self.birth_day)
        return (now - birthday).days // 365

    @property
    def profile(self):
        # 第一次进来应该创建user对应的profile
        if not hasattr(self, '_profile'):
            # print('getting  profile from database...')
            self._profile, _ = Profile.objects.get_or_create(id=self.id)
        return self._profile

    def to_dict(self):
        return {
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'sex': self.sex,
            'age': self.age,
            'avatar': self.avatar,
            'location': self.location,
        }


class Profile(models.Model, ModelMixin):
    SEX = (
        ('female', 'female'),
        ('male', 'male')
    )
    location = models.CharField(max_length=64, verbose_name='目标城市')
    min_distance = models.IntegerField(default=0, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=100, verbose_name='最大查找范围')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=50, verbose_name='最大交友年龄')
    dating_sex = models.CharField(max_length=16, choices=SEX, verbose_name='匹配的性别')
    vibration = models.BooleanField(default=True, verbose_name='开启震动')
    only_matche = models.BooleanField(default=True, verbose_name='不让为匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='自动播放视频')

