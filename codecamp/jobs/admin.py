from django.contrib import admin

from jobs.models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title','minimum_experience','company')

admin.site.register(Job,JobAdmin)

