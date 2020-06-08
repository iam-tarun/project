from django.contrib import admin
from .models import GroupTable, GroupUserTable
# Register your models here.
admin.site.register(GroupTable)
admin.site.register(GroupUserTable)