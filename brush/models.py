from dungeons.models import Dungeons
from django.db import models


# Create your models here.
class Checkpoint(models.Model):
    Dungeons = models.ForeignKey('dungeons.Dungeons', on_delete=models.CASCADE, null=True,
                                 verbose_name='所属副本')  # 关联副本 ID
    checkpointname = models.CharField('关卡名称', max_length=200)  # 关卡名称
    doordirection = models.CharField('门方向', max_length=200)  # 门方向
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获# 取当前时间

    class Meta:
        verbose_name = '关卡'
        verbose_name_plural = '关卡'

    def __str__(self):
        return self.checkpointname


class Actionstep(models.Model):
    Checkpoint = models.ForeignKey(Checkpoint, related_name='actionstep_checkpoint', on_delete=models.CASCADE)  # 关联关卡
    actionstep = models.DecimalField('操作步骤', max_digits=10, decimal_places=2)  # 操作步骤
    type = models.PositiveSmallIntegerField(
        choices=[(1, '移动到'), (2, '双击按键'), (3, '打怪'), (4, '鼠标点击'), (5, '键盘按键'), (6, '延迟'),(7,'键盘长按'),(8,'过门')], verbose_name='操作类型',
        default=1)  # 操作类型
    content = models.CharField('操作内容', max_length=200)  # 操作内容
    actionNum = models.PositiveSmallIntegerField(default=1, verbose_name='操作次数')
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动# 获取当前时间

    def __str__(self):
        return self.actionstep.__str__()  # 动作 1 移动到  2 移动 3 打怪 4 点击
