from django.contrib import admin
from .models import Task,User,AcceptedTasks,RoleEnum
# Register your models here.
from django.contrib.auth.models import Group

admin.site.unregister(Group)
@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    # TODO: Only allow Admin users to delte
    # def has_delete_permission(self, request, obj=None):
    #     print(obj)
    #     return obj is None or obj.role == RoleEnum.A
    list_display=['owner','name']
    pass
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    readonly_fields = ('id',)
    fields=['username','password','first_name','last_name','role','email','location']
    list_display=['id','username','role']
    list_display=['id','username','role']
    list_editable = ['role']
@admin.register(AcceptedTasks)
class AcceptedTasks(admin.ModelAdmin):
    list_display=['id','user','task']
    pass
