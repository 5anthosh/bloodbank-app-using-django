from django.contrib import admin
from .models import DonarDetail, Record, BloodStorage


class DonarDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'blood_group', 'city',)
    search_fields = ('city', 'name', 'blood_group')
    ordering = ['city', 'name']

admin.site.register(DonarDetail, DonarDetailAdmin)
admin.site.register(Record)
admin.site.register(BloodStorage)
