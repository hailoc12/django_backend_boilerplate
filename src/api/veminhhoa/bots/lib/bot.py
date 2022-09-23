from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

from typing import List 


from viberbot.api.messages import (
    TextMessage,
    ContactMessage,
    PictureMessage,
    VideoMessage, 
    KeyboardMessage
)

from bot_xsmb.bots.models import (
    BotModel, 
    create_bot_subcriber_from_viber_user_profile, unsubcribe_bot, 
    check_subcribed_bot, set_user_provided_name, set_subcribed_bot, get_user_provided_name, 
    get_subcriber_from_uid
)

from bot_xsmb.bots.lib.bot_messages import (
    BOT_MESSAGES, VIBER_COMMAND_KEYBOARD_FREEUSER, VIBER_COMMAND_KEYBOARD_START_USING_BOT, 
    BOT_FEATURE_1_TEXT, BOT_FEATURE_2_TEXT, BOT_FEATURE_3_TEXT, BOT_FEATURE_4_TEXT, 
    # BOT_FEATURE_5_TEXT,
    BOT_FEATURE_6_TEXT, BOT_FEATURE_6_STEP_CODES, 
    BOT_FEATURE_7_TEXT, 
    BOT_FEATURE_1_STEP_CODES, BOT_FEATURE_2_STEP_CODES
)

from bot_xsmb.bots.lib.bot_features import (
    execute_show_lastest_result, execute_show_result_by_date, execute_show_today_good_number, 
    execute_calculate_number_statistics, execute_quick_statistics, execute_share_bot
)



from bot_xsmb.bots.lib.bot_display import (
    send_welcome_after_subcribe_free_viber_bot, 
    display_free_viber_command_keyboard, 
    display_unrecognized_command, 
    display_free_viber_in_development_feature, 
    display_bot_notification, 
    display_xsmb_result, 
    display_message_function, 
    display_xsmb_good_number_today
)

import json 
import os 

class Bot():
    def __init__(self, request_data):
        pass 

    def execute_request(self):
        pass 

class ViberBot(Bot):
    def __init__(self, bot_name:str='', viber_token:str='', bot_type=BotModel.BotType.FREE_BOT, bot_model=None): 
        bot_configuration = BotConfiguration(
	        name='KQ XSMB',
	        avatar='',
	        auth_token=viber_token
        )
        self.bot_type = bot_type 
        self.bot_name = bot_name 
        self.auth_token = viber_token
        self.viber = Api(bot_configuration)     
        self.bot_model = bot_model

    def verify_request_belong_to_this_bot(self, request):
        data_in_bytes = request.body
        return self.viber.verify_signature(data_in_bytes, request.headers.get('X-Viber-Content-Signature'))

    def set_callback_hook(self, url:str):
        print(self.get_bot_info())
        try: 
           self.viber.set_webhook(url, [ViberConversationStartedRequest, ViberMessageRequest, ViberSubscribedRequest, ViberUnsubscribedRequest])
           return True 
        except Exception as e:
            print(e) 
            print("Warning: viber set_webhook unsuccessfully")
            return False 
        
    def unset_callback_hook(self):
        self.viber.unset_webhook()
        return True 

    def get_bot_info(self):
        bot_info = self.viber.get_account_info()
        return bot_info

    def save_data_to_bot_model(self):
        bot_model, created = BotModel.objects.get_or_create(
            auth_token=self.auth_token
        )
        if created: 
            bot_model.name = self.bot_name 
            bot_model.bot_type = self.bot_type 
            bot_model.save()

    def get_bot_model(self):
        if not self.bot_model:
            bot_model = BotModel.objects.get(
                auth_token = self.viber_token 
            )
            self.bot_model = bot_model 
        
        return self.bot_model 
            
    def get_bot_subcribers(self):
        bot_model = self.get_bot_model()
        subcribers = bot_model.subcribers.all()
        return subcribers

    def send_notification_to_bot_subcribers(self, notification, display_command_keyboard=False, display_command_keyboard_function=None): 
        viber = self.viber 
        for subcriber in self.get_bot_subcribers():
            try: 
                uid = subcriber.uid 
                display_bot_notification(viber, uid, notification)
                if display_command_keyboard: 
                    display_command_keyboard_function(viber, uid, hide_message=True)
            except Exception as e:
                print(e)  


    def send_xsmb_result_to_bot_subcribers(self, xsmb_result, display_command_keyboard=False, display_command_keyboard_function=None): 
        viber = self.viber 
        for subcriber in self.get_bot_subcribers():
            try: 
                uid = subcriber.uid 
                display_xsmb_result(viber, uid, xsmb_result)
                if display_command_keyboard: 
                    display_command_keyboard_function(viber, uid, hide_message=True)
            except Exception as e:
                print(e)  

    def send_xsmb_so_dep_to_bot_subcribers(self, xsmb_so_dep, display_command_keyboard=False, display_command_keyboard_function=None): 
        viber = self.viber 
        for subcriber in self.get_bot_subcribers():
            try: 
                uid = subcriber.uid 
                display_xsmb_good_number_today(viber, uid, xsmb_so_dep)
                if display_command_keyboard: 
                    display_command_keyboard_function(viber, uid, hide_message=True)

            except Exception as e:
                print(e)  
    

def get_viber_bot_from_bot_model(bot_model):
    viber_bot = ViberBot(
        bot_name = bot_model.name, 
        viber_token = bot_model.auth_token, 
        bot_type = bot_model.bot_type, 
        bot_model = bot_model
    )
    return viber_bot

def get_all_viber_bots(bot_types:List[BotModel.BotType]):
    viber_bots = []
    for bot_type in bot_types: 
        for bot_model in BotModel.objects.filter(bot_type=bot_type).all():
            viber_bot = get_viber_bot_from_bot_model(bot_model)
            if viber_bot: 
                viber_bots.append(viber_bot)
    return viber_bots


def get_viber_bot_from_callback_request(request):
    for bot_model in BotModel.objects.all():
        viber_bot = get_viber_bot_from_bot_model(bot_model)
        if viber_bot.verify_request_belong_to_this_bot(request):
            return viber_bot
    return None 


def set_viber_callback_hook_based_on_bot_type(viber_bot):
    if viber_bot.bot_type == BotModel.BotType.FREE_BOT:
        result = viber_bot.set_callback_hook(
            url = os.environ.get("DJANGO_HOST", '') + '/api/free_viber_callback/'
        )
    elif viber_bot.bot_type == BotModel.BotType.PREMIUM_BOT:
        result = viber_bot.set_callback_hook(
            url = os.environ.get("DJANGO_HOST", '') + '/api/premium_viber_callback/'
        )
    elif viber_bot.bot_type == BotModel.BotType.FREE_TEST_BOT:
        result = viber_bot.set_callback_hook(
            url = os.environ.get("DJANGO_HOST", '') + '/api/free_test_viber_callback/'
        )
    elif viber_bot.bot_type == BotModel.BotType.PREMIUM_TEST_BOT:
        result = viber_bot.set_callback_hook(
            url = os.environ.get("DJANGO_HOST", '') + '/api/premium_test_viber_callback/'
        )
    else:
        pass 
    return result


def process_feature_message(bot_model, viber, viber_request, uid):
    subcriber = get_subcriber_from_uid(uid)
    feature_session = None 
    step_code = None 

    if isinstance(viber_request.message, TextMessage):
        text = viber_request.message.text 
        
        feature_session = None 
        step_code = None 

        if text in [BOT_FEATURE_1_TEXT, BOT_FEATURE_2_TEXT, BOT_FEATURE_3_TEXT, BOT_FEATURE_4_TEXT, 
            # BOT_FEATURE_5_TEXT, 
            BOT_FEATURE_6_TEXT, BOT_FEATURE_7_TEXT
            ]:
            if subcriber.is_in_feature_session(): # clear feature session if user click on new feature 
                subcriber.finish_feature_session()

        if subcriber.is_in_feature_session():
            feature_session, step_code = subcriber.get_feature_session()
                
        if text == BOT_FEATURE_1_TEXT or feature_session == BOT_FEATURE_1_TEXT:
            execute_show_lastest_result(bot_model, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard)
         
        elif text == BOT_FEATURE_2_TEXT or feature_session == BOT_FEATURE_2_TEXT:
            execute_show_result_by_date(bot_model, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)

        elif text == BOT_FEATURE_3_TEXT or feature_session == BOT_FEATURE_3_TEXT:
            execute_quick_statistics(bot_model, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)
            
        elif text == BOT_FEATURE_4_TEXT or feature_session == BOT_FEATURE_4_TEXT:
            execute_show_today_good_number(bot_model, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)
            # display_free_viber_in_development_feature(viber, uid)

        # elif text == BOT_FEATURE_5_TEXT or feature_session == BOT_FEATURE_5_TEXT:
        #     display_free_viber_in_development_feature(viber, uid)

        elif text == BOT_FEATURE_6_TEXT or feature_session == BOT_FEATURE_6_TEXT:
            execute_calculate_number_statistics(bot_model, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)

        elif text == BOT_FEATURE_7_TEXT or feature_session == BOT_FEATURE_7_TEXT:
            execute_share_bot(bot_model, viber, subcriber, feature_session, step_code, text, display_free_viber_command_keyboard, display_message_function)

        else: # unrecognized user commands
            if subcriber.is_in_feature_session():
                subcriber.finish_feature_session()
            display_unrecognized_command(viber, uid, unrecognized_command=text)
            display_free_viber_command_keyboard(viber, uid)
    else:
        pass 


class FreeViberBot(ViberBot):
    def execute_request(self, request):
        try: 
            viber_request = self.viber.parse_request(json.dumps(request.data))
        except Exception as e:
            viber_request = None 
            print(e)
        
        if isinstance(viber_request, ViberConversationStartedRequest):
            user_profile = viber_request.user
            
            if viber_request.subscribed: # user has subcribed
                send_welcome_after_subcribe_free_viber_bot(self.viber, user_profile.id, get_user_provided_name(user_profile.id))
            else: 
                new_subcriber = create_bot_subcriber_from_viber_user_profile(self.bot_name, user_profile)
                self.viber.send_messages(
                    to=new_subcriber.uid, 
                    messages=[
                        TextMessage(text=BOT_MESSAGES['FREE_VIBER_BOT_WELCOME'])
                    ]
                )
        elif isinstance(viber_request, ViberSubscribedRequest):
            user_profile = viber_request.sender
            send_welcome_after_subcribe_free_viber_bot(self.viber, user_profile.id, user_profile.name)

        elif isinstance(viber_request, ViberUnsubscribedRequest):
            unsubcribe_bot(viber_request.user_id)

        elif isinstance(viber_request, ViberMessageRequest):
            uid = viber_request.sender.id 
            if not check_subcribed_bot(uid): # not subcribed yet, this is first message (user provided name)
                if isinstance(viber_request.message, TextMessage):
                    user_provided_name = viber_request.message.text 
                    set_user_provided_name(uid, user_provided_name)
                    send_welcome_after_subcribe_free_viber_bot(self.viber, uid, user_provided_name)
                else:
                    pass 
                set_subcribed_bot(uid, True)
            else: 
                process_feature_message(self.bot_model, self.viber, viber_request, uid)       
        else: # not recognize viber request
            print(viber_request)
            pass  

        return 200


class PremiumViberBot(ViberBot):
    def execute_request(self, request):
        try: 
            viber_request = self.viber.parse_request(json.dumps(request.data))
        except Exception as e:
            viber_request = None 
            print(e) 
        return 200