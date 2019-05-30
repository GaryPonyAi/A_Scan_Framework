from django.contrib import admin

# Register your models here.
from .models import buglist,toollist


class bugadmin(admin.ModelAdmin):
    list_display = ('bugname','pub_time','update_time',)

class tooladmin(admin.ModelAdmin):
    list_display = ('toolname','pub_time','update_time',)

admin.site.register(buglist,bugadmin)
admin.site.register(toollist,tooladmin)