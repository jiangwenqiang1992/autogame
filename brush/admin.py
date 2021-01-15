from django.contrib import admin

from brush.models import Checkpoint,Actionstep


class ActionstepAdmin(admin.TabularInline):
    list_display=['actionstep','type','content','create_time','id','checkpoint']
    model = Actionstep
    extra=1

class CheckpointAdmin(admin.ModelAdmin):
    list_display = ['Dungeons', 'checkpointname', 'doordirection','create_time','id']
    inlines = [ActionstepAdmin]

admin.site.register(Checkpoint,CheckpointAdmin)