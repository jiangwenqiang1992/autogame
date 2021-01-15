from django.contrib import admin

# Register your models here.
from dungeons.models import Dungeons


class DungeonsAdmin(admin.ModelAdmin):
    list_display = [ 'dungeonstname', 'create_time','id' ]


admin.site.register(Dungeons)  # 把产品模块注册到 Django admin 后台并能显示

