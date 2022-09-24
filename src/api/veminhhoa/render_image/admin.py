from django.contrib import admin
import os 
from veminhhoa.render_image.models import RenderTemplate, RenderTransaction

admin.AdminSite.site_header = 'Admin Site'
admin.AdminSite.site_title = 'Admin Site'
admin.AdminSite.index_title = ''

class RenderTemplateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description' )

class RenderTransactionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'raw_prompt')

admin.site.register(RenderTemplate, RenderTemplateAdmin)
admin.site.register(RenderTransaction, RenderTransactionAdmin)

