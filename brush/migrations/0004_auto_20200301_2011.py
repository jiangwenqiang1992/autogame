# Generated by Django 2.2.10 on 2020-03-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brush', '0003_auto_20200228_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionstep',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, '移动到'), (2, '双击按键'), (3, '打怪'), (4, '点击'), (5, '单击按键'), (6, '延迟')], default=1, verbose_name='操作类型'),
        ),
    ]
