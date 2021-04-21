from django.contrib import admin

from brush.models import Checkpoint,Actionstep


class ActionstepAdmin(admin.TabularInline):
    list_display=['actionstep','type','content','create_time','id','checkpoint']
    model = Actionstep
    extra=1


class CheckpointAdmin(admin.ModelAdmin):
    list_display = ['Dungeons', 'checkpointname', 'doordirection','create_time','id']
    inlines = [ActionstepAdmin]
    change_form_template = 'admin/extras/case_change_form.html'


admin.site.register(Checkpoint,CheckpointAdmin)