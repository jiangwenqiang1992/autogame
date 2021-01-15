# Generated by Django 3.0.6 on 2020-05-31 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brush', '0005_auto_20200526_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionstep',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, '移动到'), (2, '双击按键'), (3, '打怪'), (4, '鼠标点击'), (5, '键盘按键'), (6, '延迟'), (7, '键盘长按')], default=1, verbose_name='操作类型'),
        ),
    ]
