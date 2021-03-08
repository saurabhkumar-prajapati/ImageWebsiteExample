from django.contrib import admin

# Register your models here.
from .models import Newuser
@admin.register(Newuser)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','event_name','image','date','location')
