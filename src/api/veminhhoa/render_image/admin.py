from django.contrib import admin
import os 
from veminhhoa.render_image.models import RenderTemplate, RenderTransaction
from veminhhoa.render_image.models import Book, Author, Order

admin.AdminSite.site_header = 'Admin Site'
admin.AdminSite.site_title = 'Admin Site'
admin.AdminSite.index_title = ''

class RenderTemplateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description' )

class RenderTransactionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'raw_prompt')

class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

admin.site.register(RenderTemplate, RenderTemplateAdmin)
admin.site.register(RenderTransaction, RenderTransactionAdmin)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Order, OrderAdmin)

