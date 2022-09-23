import time 

from bot_xsmb.bots.models import (
    BotSubcriber, 
    get_subcriber_from_uid, 
)

from bot_xsmb.bots.models import (
    Notification, 
    BotUsage, 
    BotModel
)

from bot_xsmb.bots.lib.bot_display import (
    display_xsmb_result, display_guide_on_auto_alert_feature, 
    display_xsmb_good_number_today, 
    display_number_statistic, 
    display_feature_6_date_range_command_keyboard, 
    display_feature_3_statistic_type_command_keyboard, 
    display_feature_3_invalid_statistic_type, 
    display_loto_freq_statistic, 
    display_giai_dac_biet_freq_statistic, 
    display_share_bot_information, 
    display_unlock_feature_successfully, 
    display_require_unlock_feature
)

from bot_xsmb.bots.lib.bot_messages import (
    BOT_FEATURE_1_TEXT, BOT_FEATURE_1_STEP_CODES, 
    BOT_FEATURE_2_ASK_FOR_DATE_INPUT, BOT_FEATURE_2_TEXT, BOT_FEATURE_2_STEP_CODES, BOT_FEATURE_2_INVALID_DATE_INPUT, 
    BOT_FEATURE_2_FAIL_TO_GET_RESULT, 
    BOT_FEATURE_3_TEXT, BOT_FEATURE_3_STEP_CODES, BOT_FEATURE_3_STATISTIC_TYPE_1, BOT_FEATURE_3_STATISTIC_TYPE_2, BOT_FEATURE_3_STATISTIC_TYPE_EXIT, 
    BOT_FEATURE_4_TEXT, BOT_FEATURE_4_STEP_CODES, 
    BOT_FEATURE_6_TEXT, BOT_FEATURE_6_STEP_CODES, 
    BOT_FEATURE_6_ASK_FOR_DATE_RANGE_INPUT, BOT_FEATURE_6_INVALID_DATE_RANGE_INPUT, BOT_FEATURE_6_ASK_FOR_NUMBER_INPUT, BOT_FEATURE_6_INVALID_NUMBER_INPUT,
    BOT_FEATURE_6_CAN_NOT_CALCULATE_NUMBER_STATISTIC, BOT_FEATURE_6_DATE_RANGE_1, BOT_FEATURE_6_DATE_RANGE_2, BOT_FEATURE_6_DATE_RANGE_3, BOT_FEATURE_6_DATE_RANGE_4, 
    BOT_FEATURE_6_DATE_RANGE_1_VALUE, BOT_FEATURE_6_DATE_RANGE_2_VALUE, BOT_FEATURE_6_DATE_RANGE_3_VALUE, BOT_FEATURE_6_DATE_RANGE_4_VALUE, 
    BOT_FEATURE_6_DATE_RANGE_1_UNIT, BOT_FEATURE_6_DATE_RANGE_2_UNIT, BOT_FEATURE_6_DATE_RANGE_3_UNIT, BOT_FEATURE_6_DATE_RANGE_4_UNIT, 
    BOT_FEATURE_7_TEXT, BOT_FEATURE_7_STEP_CODES,
    YES_ANSWER,
)

from bot_xsmb.kq_xo_so.models import (
    XoSoMienBac, 
    XSMB_So_Dep, 
    get_latest_xsmb_result,
    get_yesterday_xsmb_result
)

from bot_xsmb.crawler.business import (
    get_xsmb_specific_date_result
)

from bot_xsmb.kq_xo_so.analysis import (
    calculate_good_number_today, 
    calculate_number_statistic, 
    calculate_loto_freq, 
    calculate_giai_dac_biet_freq
)

import datetime 
import django 

def require_unlock_feature(viber, uid):
    subcriber = get_subcriber_from_uid(uid)
    
    if not subcriber.get_unlock_all_features(): 
        display_require_unlock_feature(viber, uid)
        return False 
    return True 


def log_subcriber_usage(bot_model, subcriber, feature):
    if bot_model:
        if bot_model.bot_type not in [BotModel.BotType.FREE_TEST_BOT]:
            BotUsage.objects.create(
                bot=bot_model, 
                subcriber=subcriber, 
                feature=feature
            )
    else:
        print("Warning: bot_model is None")
    return True 

def execute_show_lastest_result(bot_model, viber, subcriber, feature_session=None, feature_code=None, text=None, display_command_function=None):
    """Show the lastest result feature - FEATURE1"""
    uid = subcriber.uid 
    subcriber.start_feature_session(BOT_FEATURE_1_TEXT, BOT_FEATURE_1_STEP_CODES[0]['code'])

    # log usage
    log_subcriber_usage(bot_model, subcriber, BOT_FEATURE_1_TEXT)
    
    # start feature session 
    latest_result = get_latest_xsmb_result()
    display_xsmb_result(viber, uid, latest_result)

    display_command_function(viber, uid, hide_message=True)
    
    # end feature session 
    subcriber.finish_feature_session()

    return True 

def alert_all_subcribers_of_xsmb_result(viber_bot, xsmb_result):
    viber = viber_bot.viber 
    for subcriber in BotSubcriber.objects.all():
        try: 
            uid = subcriber.uid 
            display_xsmb_result(viber, uid, xsmb_result)
            # display_guide_on_auto_alert_feature(viber, uid)
        except Exception as e:
            print(e)

def execute_show_result_by_date(bot_model, viber, subcriber, feature_session=None, feature_code=None, text=None, display_command_function=None, display_message_function=None):
    """Get the result by date - FEATURE 2"""
    uid = subcriber.uid 

    if not require_unlock_feature(viber, uid):
        return True 

    if not feature_session: # start using feature 
        display_message_function(viber, uid, message=BOT_FEATURE_2_ASK_FOR_DATE_INPUT)
        subcriber.start_feature_session(BOT_FEATURE_2_TEXT, BOT_FEATURE_2_STEP_CODES[0]['code'])
        log_subcriber_usage(bot_model, subcriber, BOT_FEATURE_2_TEXT)

    else: # being in feature session 
        if feature_code == BOT_FEATURE_2_STEP_CODES[0]['code']: # pass step 1
            try:
                crawl_date = datetime.datetime.strptime(text.strip(), '%d/%m/%Y')
                subcriber.set_feature_session(feature_code, BOT_FEATURE_2_STEP_CODES[1]['code'])
                xsmb_result = XoSoMienBac.objects.filter(
                    ngay_trao_giai = crawl_date
                ).first()

                if xsmb_result:
                    display_xsmb_result(viber, uid, xsmb_result)
                    # subcriber.finish_feature_session()
                else:
                    display_message_function(viber, uid, message=BOT_FEATURE_2_FAIL_TO_GET_RESULT)    
                # subcriber.finish_feature_session()
            except ValueError:
                display_message_function(viber, uid, message=BOT_FEATURE_2_INVALID_DATE_INPUT)
                display_message_function(viber, uid, message=BOT_FEATURE_2_ASK_FOR_DATE_INPUT)
    
    display_command_function(viber, uid, hide_message=True)
    return True 

def execute_show_today_good_number(bot_model, viber, subcriber, feature_session=None, feature_code=None, text=None, display_command_function=None, display_message_function=None):
    """So dep hom nay - FEATURE 4"""
    uid = subcriber.uid 

    if not require_unlock_feature(viber, uid):
        return True 

    subcriber.start_feature_session(BOT_FEATURE_4_TEXT, BOT_FEATURE_4_STEP_CODES[0]['code'])
    log_subcriber_usage(bot_model, subcriber, BOT_FEATURE_4_TEXT)

    # start using session
    xsmb_so_dep = calculate_good_number_today()
    if xsmb_so_dep: 
        display_xsmb_good_number_today(viber, uid, xsmb_so_dep)

    # end feature session 
    subcriber.finish_feature_session()
    
    display_command_function(viber, uid, hide_message=True)
    return True 

def _execute_display_number_statistic(viber, subcriber, number_statistic, args, display_header):
    uid = subcriber.uid 
    display_state, new_start = display_number_statistic(viber, uid, number_statistic, display_header=display_header, start=args['start'])
    if display_state == 1: # wait yes/no question for continue displaying
        args['start'] = new_start 
        subcriber.set_feature_session(BOT_FEATURE_6_TEXT, BOT_FEATURE_6_STEP_CODES[3]['code'], args)
        return False 
    elif display_state == 2: # ok 
        subcriber.finish_feature_session()
        return True 
    else:
        pass 
        return False 

def _translate_date_value(date_value, date_unit):
    if date_unit == "day":
        return "{0} ngày".format(date_value)
    elif date_unit == 'month':
        return "{0} tháng".format(date_value)
    elif date_unit == 'year':
        return "{0} năm".format(date_value)
    else:
        return 'Không rõ kết quả'

def execute_calculate_number_statistics(bot_model, viber, subcriber, feature_session=None, feature_code=None, text=None, display_command_function=None, display_message_function=None):
    """Do ket qua - FEATURE 6"""
    uid = subcriber.uid 

    if not require_unlock_feature(viber, uid):
        return True 

    if not feature_session: # start using feature 
        display_feature_6_date_range_command_keyboard(viber, uid, message=BOT_FEATURE_6_ASK_FOR_DATE_RANGE_INPUT)
        subcriber.start_feature_session(BOT_FEATURE_6_TEXT, BOT_FEATURE_6_STEP_CODES[0]['code'])
        log_subcriber_usage(bot_model, subcriber, BOT_FEATURE_6_TEXT)
        return True

    else: # being in feature session 
        if feature_code == BOT_FEATURE_6_STEP_CODES[0]['code']: # pass step 1
            date_value = 0 
            date_unit = 'day'
            args = subcriber.get_feature_args()
            
            if text == BOT_FEATURE_6_DATE_RANGE_1:
                date_value = BOT_FEATURE_6_DATE_RANGE_1_VALUE
                date_unit = BOT_FEATURE_6_DATE_RANGE_1_UNIT
            elif text == BOT_FEATURE_6_DATE_RANGE_2:
                date_value = BOT_FEATURE_6_DATE_RANGE_2_VALUE
                date_unit = BOT_FEATURE_6_DATE_RANGE_2_UNIT                
            elif text == BOT_FEATURE_6_DATE_RANGE_3:
                date_value = BOT_FEATURE_6_DATE_RANGE_3_VALUE
                date_unit = BOT_FEATURE_6_DATE_RANGE_3_UNIT                
            elif text == BOT_FEATURE_6_DATE_RANGE_4:
                date_value = BOT_FEATURE_6_DATE_RANGE_4_VALUE
                date_unit = BOT_FEATURE_6_DATE_RANGE_4_UNIT                                
            else:
                display_message_function(viber, uid, message=BOT_FEATURE_6_INVALID_DATE_RANGE_INPUT)
                subcriber.finish_feature_session()
                display_command_function(viber, uid, hide_message=True)
                return True 
            args['date_value'] = date_value
            args['date_unit'] = date_unit
            subcriber.set_feature_session(BOT_FEATURE_6_TEXT, BOT_FEATURE_6_STEP_CODES[1]['code'], args)
            display_message_function(viber, uid, message=BOT_FEATURE_6_ASK_FOR_NUMBER_INPUT)
            return True 

        elif feature_code == BOT_FEATURE_6_STEP_CODES[1]['code']: # pass step 2
            args = subcriber.get_feature_args()
            if text.isdigit():
                number = int(text)
                args['number'] = number 
                args['start'] = 0
                subcriber.set_feature_session(BOT_FEATURE_6_TEXT, BOT_FEATURE_6_STEP_CODES[2]['code'], args)
                number_statistic = calculate_number_statistic(args['date_value'], args['date_unit'], args['number'])
                if number_statistic: 
                    finish = _execute_display_number_statistic(viber, subcriber, number_statistic, args, display_header=True)
                    if finish: 
                        pass 
                    else: 
                        return True
                else:
                    message = BOT_FEATURE_6_CAN_NOT_CALCULATE_NUMBER_STATISTIC.format(number, _translate_date_value(args['date_value'], args['date_unit']))
                    display_message_function(viber, uid, message=message)
                    subcriber.finish_feature_session()
            else:
                display_message_function(viber, uid, message=BOT_FEATURE_6_INVALID_NUMBER_INPUT)
                subcriber.finish_feature_session()

        elif feature_code == BOT_FEATURE_6_STEP_CODES[3]['code']: # pass step 3: continue/stop displaying
            args = subcriber.get_feature_args()
            start = args['start']
            if text == YES_ANSWER:
                number_statistic = calculate_number_statistic(args['date_value'], args['date_unit'], args['number'])
                if number_statistic: 
                    finish = _execute_display_number_statistic(viber, subcriber, number_statistic, args, display_header=True)
                    if finish:
                        pass 
                    else: 
                        return True
                else:
                    display_message_function(viber, uid, message=BOT_FEATURE_6_CAN_NOT_CALCULATE_NUMBER_STATISTIC)
                    subcriber.finish_feature_session()
            else:
                subcriber.finish_feature_session()
        else:
            pass 

    display_command_function(viber, uid, hide_message=True)
    return True 

def execute_quick_statistics(bot_model, viber, subcriber, feature_session=None, feature_code=None, text=None, display_command_function=None, display_message_function=None):
    uid = subcriber.uid 

    if not require_unlock_feature(viber, uid):
        return True 

    if not feature_session: # start using feature 
        display_feature_3_statistic_type_command_keyboard(viber, uid)
        subcriber.start_feature_session(BOT_FEATURE_3_TEXT, BOT_FEATURE_3_STEP_CODES[0]['code'])
        log_subcriber_usage(bot_model, subcriber, BOT_FEATURE_3_TEXT)
        return True
    else: #being in feature session 
        if feature_code == BOT_FEATURE_3_STEP_CODES[0]['code']: # got statistic type input 
            args = subcriber.get_feature_args()
            if text == BOT_FEATURE_3_STATISTIC_TYPE_1: 
                args['type'] = BOT_FEATURE_3_STATISTIC_TYPE_1
                subcriber.set_feature_session(BOT_FEATURE_3_TEXT, BOT_FEATURE_3_STEP_CODES[1]['code'], args)
                result = calculate_loto_freq()
                display_loto_freq_statistic(viber, uid, result)
                subcriber.finish_feature_session()
                return True 
            elif text == BOT_FEATURE_3_STATISTIC_TYPE_2: 
                args['type'] = BOT_FEATURE_3_STATISTIC_TYPE_2
                subcriber.set_feature_session(BOT_FEATURE_3_TEXT, BOT_FEATURE_3_STEP_CODES[1]['code'], args)
                result = calculate_giai_dac_biet_freq()
                display_giai_dac_biet_freq_statistic(viber, uid, result)
                subcriber.finish_feature_session()
            elif text == BOT_FEATURE_3_STATISTIC_TYPE_EXIT: # quay lai 
                subcriber.finish_feature_session()
            else:
                display_feature_3_invalid_statistic_type(viber, uid)
                subcriber.finish_feature_session()

    display_command_function(viber, uid, hide_message=True)
    return True 

def execute_share_bot(bot_model, viber, subcriber, feature_session=None, feature_code=None, text=None, display_command_function=None, display_message_function=None):
    uid = subcriber.uid 
    if not feature_session: # start using feature 
        subcriber.start_feature_session(BOT_FEATURE_7_TEXT, BOT_FEATURE_7_STEP_CODES[0]['code'])
        log_subcriber_usage(bot_model, subcriber, BOT_FEATURE_7_TEXT)
        display_share_bot_information(viber, uid)
        subcriber.finish_feature_session()
    else:
        pass
    
    if not subcriber.get_unlock_all_features():
        subcriber.set_unlock_all_features()
        time.sleep(1)
        display_unlock_feature_successfully(viber, uid)

    display_command_function(viber, uid, hide_message=True)
    return True 


    

