from config import celery_app


# @celery_app.task()
# def send_latest_xo_so_result_to_subcribers():
#     viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_BOT])
    
#     latest_result = get_latest_xsmb_result()
#     for viber_bot in viber_bots: 
#         viber_bot.send_xsmb_result_to_bot_subcribers(latest_result)
    
#     return True 