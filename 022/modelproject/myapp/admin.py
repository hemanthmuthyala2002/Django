from django.contrib import admin
from .models import Sample

# Register your models here.

class SampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_display_links = ('title',)
    list_filter = ('id','created_at')

admin.site.register(Sample, SampleAdmin)