from django.contrib import admin
from .models import User
# Register your models here.
class AdminArea(admin.ModelAdmin):
    list_display = ('fio','data_rojdeniya','pol','resultn')

admin.site.register(User,AdminArea)