from django.contrib import admin
from .models import Family

# Register your models here.
class FamilyMyAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'phone', 'address']
    
admin.site.register(Family, FamilyMyAdmin)