from django.db import models

# Create your models here.
class Dungeons(models.Model):
    dungeonstname = models.CharField('地下城名称',max_length=64)  # 产品名称
    create_time = models.DateTimeField('创建时间',auto_now=True)  # 创建时间，自动获取# 当前时间
    class Meta:
        verbose_name = '地下城'
        verbose_name_plural = '地下城'
    def __str__(self):
        return self.dungeonstname