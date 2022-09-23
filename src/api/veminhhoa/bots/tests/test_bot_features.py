import pytest 
pytestmark = pytest.mark.django_db

from bot_xsmb.bots.lib.bot_features import (
    execute_show_result_by_date, 
    execute_show_today_good_number, 
    execute_calculate_number_statistics, 
    execute_quick_statistics, 
    execute_share_bot
)

from bot_xsmb.bots.lib.bot import (
    get_all_viber_bots
)

from bot_xsmb.bots.models import(
    BotModel
)

from bot_xsmb.bots.lib.bot_display import (
    display_free_viber_command_keyboard, 
    display_message_function, 
)

from bot_xsmb.bots.lib.bot_messages import (
    BOT_FEATURE_2_TEXT, BOT_FEATURE_2_STEP_CODES, 
    BOT_FEATURE_3_TEXT, BOT_FEATURE_3_STEP_CODES, BOT_FEATURE_3_STATISTIC_TYPE_1, BOT_FEATURE_3_STATISTIC_TYPE_2, 
    BOT_FEATURE_4_TEXT, BOT_FEATURE_4_STEP_CODES, 
    BOT_FEATURE_6_TEXT, BOT_FEATURE_6_STEP_CODES, BOT_FEATURE_6_DATE_RANGE_1, BOT_FEATURE_6_DATE_RANGE_1_VALUE, 
    BOT_FEATURE_7_TEXT, 
    YES_ANSWER
)

class TestBotFeatures():
    def test_execute_show_result_by_date_step_1(self):
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_TEST_BOT])
        viber_bot = viber_bots[0]
        viber = viber_bots[0].viber 
        subcriber = viber_bot.get_bot_subcribers()[0]
        feature_session = None 
        step_code = None 
        text = BOT_FEATURE_2_TEXT

        result = execute_show_result_by_date(viber_bot, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)
        assert (result == True)

    def test_execute_show_result_by_date_step_2(self):
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_TEST_BOT])
        viber_bot = viber_bots[0]
        viber = viber_bots[0].viber 
        subcriber = viber_bot.get_bot_subcribers()[0]
        feature_session = BOT_FEATURE_2_TEXT 
        step_code = BOT_FEATURE_2_STEP_CODES[0]['code'] 
        text = '25/1/2022'

        result = execute_show_result_by_date(viber_bot, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)
        assert (result == True)

    def test_execute_show_today_good_number(self):
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_TEST_BOT])
        viber_bot = viber_bots[0]
        viber = viber_bots[0].viber 
        subcriber = viber_bot.get_bot_subcribers()[0]
        feature_session = BOT_FEATURE_4_TEXT 
        step_code = BOT_FEATURE_4_STEP_CODES[0]['code'] 
        text = BOT_FEATURE_4_TEXT
        result = execute_show_today_good_number(viber_bot, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)
        assert(result == True)

    def test_execute_calculate_number_statistics_step_0(self):
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_TEST_BOT])
        viber_bot = viber_bots[0]
        viber = viber_bots[0].viber 
        subcriber = viber_bot.get_bot_subcribers()[0]
        feature_session = None 
        step_code = None
        text = BOT_FEATURE_6_TEXT
        result = execute_calculate_number_statistics(viber_bot, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)
        assert(result == True)

    def test_execute_calculate_number_statistics_step_1(self):
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_TEST_BOT])
        viber_bot = viber_bots[0]
        viber = viber_bots[0].viber 
        subcriber = viber_bot.get_bot_subcribers()[0]
        feature_session = BOT_FEATURE_6_TEXT 
        step_code = BOT_FEATURE_6_STEP_CODES[0]['code'] 
        text = BOT_FEATURE_6_DATE_RANGE_1
        result = execute_calculate_number_statistics(viber_bot, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)
        assert(result == True)

    def test_execute_calculate_number_statistics_step_2(self):
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_TEST_BOT])
        viber_bot = viber_bots[0]
        viber = viber_bots[0].viber 
        subcriber = viber_bot.get_bot_subcribers()[0]
        feature_session = BOT_FEATURE_6_TEXT 
        step_code = BOT_FEATURE_6_STEP_CODES[1]['code'] 
        args = {
            'date_value': 2, 
            'date_unit': 'month', 
            'number': 44, 
            'start': 0
        }
        text = '44'

        subcriber.set_feature_session(feature_session, step_code, args)
        result = execute_calculate_number_statistics(viber_bot, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)
        assert(result == True)

    def test_execute_calculate_number_statistics_step_4(self):
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_TEST_BOT])
        viber_bot = viber_bots[0]
        viber = viber_bots[0].viber 
        subcriber = viber_bot.get_bot_subcribers()[0]
        feature_session = BOT_FEATURE_6_TEXT 
        step_code = BOT_FEATURE_6_STEP_CODES[3]['code'] 
        args = {
            'date_value': 1, 
            'date_unit': 'day', 
            'number': 4, 
            'start': 0
        }
        subcriber.set_feature_session(feature_session, step_code, args)

        text = YES_ANSWER
        result = execute_calculate_number_statistics(viber_bot, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)

        assert(result == True)

    def test_execute_quick_statistic_step_0(self):
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_TEST_BOT])
        viber_bot = viber_bots[0]
        viber = viber_bots[0].viber 
        subcriber = viber_bot.get_bot_subcribers()[0]
        feature_session = None 
        step_code = None 

        text = BOT_FEATURE_3_TEXT
        result = execute_quick_statistics(viber_bot, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)

        assert(result == True)

    def test_execute_quick_statistic_step_1(self): # tan suat lo to 
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_TEST_BOT])
        viber_bot = viber_bots[0]
        viber = viber_bots[0].viber 
        subcriber = viber_bot.get_bot_subcribers()[0]
    
        feature_session = BOT_FEATURE_3_TEXT 
        step_code = BOT_FEATURE_3_STEP_CODES[0]['code'] 
        
        args = {
        }
        subcriber.set_feature_session(feature_session, step_code, args)

        text = BOT_FEATURE_3_STATISTIC_TYPE_1
        result = execute_quick_statistics(viber_bot, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)

        assert(result == True)

    def test_execute_quick_statistic_step_1_type_2(self): # tan suat giai dac biet 
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_TEST_BOT])
        viber_bot = viber_bots[0]
        viber = viber_bots[0].viber 
        subcriber = viber_bot.get_bot_subcribers()[0]
    
        feature_session = BOT_FEATURE_3_TEXT 
        step_code = BOT_FEATURE_3_STEP_CODES[0]['code'] 
        
        args = {
        }
        subcriber.set_feature_session(feature_session, step_code, args)

        text = BOT_FEATURE_3_STATISTIC_TYPE_2
        result = execute_quick_statistics(viber_bot, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)

        assert(result == True)

    def test_execute_share_bot(self): # chia se bot
        viber_bots = get_all_viber_bots(bot_types=[BotModel.BotType.FREE_TEST_BOT])
        viber_bot = viber_bots[0]
        viber = viber_bots[0].viber 
        subcriber = viber_bot.get_bot_subcribers()[0]
    
        feature_session = None
        step_code = None 
        
        text = BOT_FEATURE_7_TEXT
        result = execute_share_bot(viber_bot, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)

        assert(result == True)