from django.contrib import admin
import os 
from veminhhoa.render_image.models import RenderTemplate

admin.AdminSite.site_header = 'Admin Site'
admin.AdminSite.site_title = 'Admin Site'
admin.AdminSite.index_title = ''

class RenderTemplateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description' )

admin.site.register(RenderTemplate, RenderTemplateAdmin)

