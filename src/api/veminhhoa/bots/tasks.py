from config import celery_app
from bot_xsmb.bots.lib.bot_messages import BOT_MESSAGES
from bot_xsmb.bots.lib.bot import FreeViberBot
from bot_xsmb.bots.models import (
    Notification, BotModel 
)
from bot_xsmb.bots.lib.utils import get_weekday_translation
import django 
import datetime 
import os 

from bot_xsmb.kq_xo_so.models import (
    get_latest_xsmb_result,
)

from bot_xsmb.bots.lib.bot import (
    get_all_viber_bots
)

from bot_xsmb.kq_xo_so.analysis import (
    calculate_good_number_today
)

from bot_xsmb.bots.lib.bot_display import (
    display_free_viber_command_keyboard
)

@celery_app.task()
def remind_subcribers_to_check_result():
    viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_BOT])
    #viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_BOT])
    
    prize = 'XỔ SỐ MIỀN BẮC (truyền thống)'
    incoming_time = '2 giờ'
    now = django.utils.timezone.now()
    result_date = '18:15, {0}, {1}'.format(get_weekday_translation(now), now.strftime('%d/%m/%Y'))
    
    remind_notification = Notification(
        message = BOT_MESSAGES['REMIND_ON_RECEIVING_RESULT'].format(incoming_time, prize, result_date)
    )

    xsmb_so_dep = calculate_good_number_today()

    for viber_bot in viber_bots: 
        viber_bot.send_notification_to_bot_subcribers(remind_notification)
        if xsmb_so_dep: 
            viber_bot.send_xsmb_so_dep_to_bot_subcribers(
                xsmb_so_dep, display_command_keyboard=True, display_command_keyboard_function=display_free_viber_command_keyboard
            )
        
    return True 

@celery_app.task()
def send_latest_xo_so_result_to_subcribers():
    viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_BOT])
    
    latest_result = get_latest_xsmb_result()
    for viber_bot in viber_bots: 
        viber_bot.send_xsmb_result_to_bot_subcribers(latest_result)
    
    return True 