from django.contrib import admin
from bot_xsmb.kq_xo_so.models import (
    XoSoMienBac, 
    XSMB_Quick_Statistic_Loto, 
    XSMB_Quick_Statistic_Giai_Dac_Biet, 
    XSMB_So_Dep
)

from bot_xsmb.bots.lib.bot import (
    FreeViberBot, get_all_viber_bots
)
from bot_xsmb.bots.models import (
    BotModel
)
from bot_xsmb.bots.lib.bot_features import (
    alert_all_subcribers_of_xsmb_result
)

from bot_xsmb.crawler.tasks import (
    crawl_xsmb_today_result, 
    crawl_xsmb_latest_results
)

from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
import os 

def alert_subcribers_on_free_viber_bot1(XoSoMienBacAdmin, request, queryset):
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_BOT])
        for xsmb_result in queryset.all():
            for viber_bot in viber_bots: 
                alert_all_subcribers_of_xsmb_result(viber_bot, xsmb_result)

def append_xsmb_history_result(XoSoMienBacAdmin, request, queryset):
    crawl_xsmb_latest_results.delay(number=20, sleep_between_crawl=10)

def append_xsmb_latest_result(XoSoMienBacAdmin, request, queryset):
    crawl_xsmb_today_result.delay()


class XoSoMienBacAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass 
    #list_display = ('_',)
    search_fields = ['ngay_trao_giai']
    ordering = ('-ngay_trao_giai', )
    actions = (alert_subcribers_on_free_viber_bot1, append_xsmb_latest_result, append_xsmb_history_result)


        
admin.site.register(XoSoMienBac, XoSoMienBacAdmin)
# admin.site.register(XSMB_Quick_Statistic_Loto)
# admin.site.register(XSMB_Quick_Statistic_Giai_Dac_Biet)
# admin.site.register(XSMB_So_Dep)


