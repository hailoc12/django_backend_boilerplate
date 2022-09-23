from django.contrib import admin
from bot_xsmb.bots.models import (
    BotSubcriber, BotModel, Notification, 
    BotUsage
)
from bot_xsmb.bots.lib.bot import (
    FreeViberBot, get_viber_bot_from_bot_model, set_viber_callback_hook_based_on_bot_type, 
    get_all_viber_bots
)

import os 

admin.AdminSite.site_header = 'XSMB Admin Site'
admin.AdminSite.site_title = 'XSMB Admin Site'
admin.AdminSite.index_title = ''

class BotSubcriberAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'user_provided_name', 'uid', 'avatar', 'subscription_type', 'feature_session', 'feature_step', 'bot')
    
def send_notification_to_free_viber_bots(NotificationAdmin, request, queryset):
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_BOT])
        for notification in queryset.all():
            for viber_bot in viber_bots: 
                send_notification_to_bot_subcribers(viber_bot, notification)


def send_notification_to_free_test_viber_bots(NotificationAdmin, request, queryset):
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_TEST_BOT])
        for notification in queryset.all():
            for viber_bot in viber_bots: 
                viber_bot.send_notification_to_bot_subcribers(notification)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ( 'message', )
    actions = (send_notification_to_free_viber_bots, send_notification_to_free_test_viber_bots)


def set_bot_callback_hook(BotModelAdmin, request, queryset):
    for bot_model in queryset.all():
        viber_bot = get_viber_bot_from_bot_model(bot_model)
        result = set_viber_callback_hook_based_on_bot_type(viber_bot)

class BotModelAdmin(admin.ModelAdmin):
    actions = (set_bot_callback_hook, )

class BotUsageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date')
    
admin.site.register(BotSubcriber, BotSubcriberAdmin)
admin.site.register(BotModel, BotModelAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(BotUsage, BotUsageAdmin)

