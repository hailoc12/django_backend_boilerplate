from django.contrib import admin
import os 

admin.AdminSite.site_header = 'Admin Site'
admin.AdminSite.site_title = 'Admin Site'
admin.AdminSite.index_title = ''


# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ( 'message', )
#     actions = (send_notification_to_free_viber_bots, send_notification_to_free_test_viber_bots)

    
# admin.site.register(BotSubcriber, BotSubcriberAdmin)

