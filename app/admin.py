from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Efile)
class EfileAdmin(admin.ModelAdmin):
    list_display = ['title','date','complete']
