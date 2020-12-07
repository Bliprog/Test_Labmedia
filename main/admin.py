from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(PayInfo)
class PayInfoAdmin(admin.ModelAdmin):
    pass