from django.db import models
from typing import Tuple

class BotModel(models.Model):
    class BotType(models.IntegerChoices): 
        FREE_BOT = 1 
        PREMIUM_BOT = 2
        FREE_TEST_BOT = 3 
        PREMIUM_TEST_BOT = 4 

    class Meta:
        verbose_name = "Quản lý bot"

    name = models.TextField(default='', blank=True)
    bot_type = models.IntegerField(choices=BotType.choices, default=BotType.FREE_BOT)
    auth_token = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name 

BotModel.verbose_name = 'Quản lý Bot'

class BotSubcriber(models.Model):
    class SubscriptionChoices(models.IntegerChoices):
        FREE_USER = 1
        PREMIUM_USER = 2

    class Meta:
         verbose_name = "Quản lý Subcribers"

    name = models.TextField(default='')
    user_provided_name = models.TextField(default='')
    avatar = models.TextField(default='', null=True)
    uid = models.TextField(default='')
    has_subcribed = models.BooleanField(default=False)
    subscription_type = models.IntegerField(choices = SubscriptionChoices.choices, default=SubscriptionChoices.FREE_USER)
    bot = models.ForeignKey(BotModel, related_name='subcribers',  on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True) # subcriber is subcribing or deleting bot?

    feature_session = models.TextField(default='')
    feature_step = models.TextField(default='')
    feature_args = models.JSONField(verbose_name="Tham số", blank=True, null=True)
    unlocked_features = models.JSONField(verbose_name="Mở khóa tính năng", blank=True, null=True)

    def start_feature_session(self, feature_code:str, step_code:str, args:dict=None):
        """Save subcriber state when they are using bot feature"""
        self.feature_session = feature_code
        self.feature_step = step_code
        self.feature_args = args
        self.save()
    
    def finish_feature_session(self):
        self.feature_session = '' 
        self.save()

    def get_feature_session(self)->Tuple[str, str]:
        """Get subcriber state when they are using bot feature"""
        return self.feature_session, self.feature_step

    def get_feature_args(self):
        if not self.feature_args: 
            self.feature_args = {}
            self.save()
        
        return self.feature_args
            
    def set_feature_session(self, feature_code, step_code, args:dict=None)->Tuple[str, str]:
        """Set subcriber state when they are using bot feature"""
        self.feature_session = feature_code
        self.feature_step = step_code
        self.feature_args = args
        self.save()

    def is_in_feature_session(self):
        return self.feature_session 

    def get_unlock_all_features(self):
        if self.unlocked_features:
            if 'unlock_all_features' in self.unlocked_features:
                return self.unlocked_features['unlock_all_features']
        else:
            return False 

    def set_unlock_all_features(self):
        if self.unlocked_features:
            self.unlocked_features['unlock_all_features'] = True 
        else: 
            self.unlocked_features = {
                'unlock_all_features': True 
            }
        self.save()

    def __str__(self):
        return self.name 

BotSubcriber.verbose_name = 'Quản lý người dùng'
    
def get_subcriber_from_uid(uid):
    subcriber = BotSubcriber.objects.filter(uid=uid).first()
    return subcriber

def create_bot_subcriber_from_viber_user_profile(bot_name:str, user_profile) -> BotSubcriber:
    bot, _ = BotModel.objects.get_or_create(
        name = bot_name
    )
    subcriber, _ = BotSubcriber.objects.get_or_create(
        name = user_profile.name, 
        uid = user_profile.id, 
        avatar = user_profile.avatar,
        bot = bot
    )
    subcriber.is_active = True 
    subcriber.save()

    return subcriber

def check_subcribed_bot(uid:str) -> bool:
    subcriber = BotSubcriber.objects.filter(uid=uid).first()
    if subcriber:
        return subcriber.has_subcribed
    else:
        return False 

def set_subcribed_bot(uid:str, value:bool):
    subcriber = BotSubcriber.objects.filter(uid=uid).first()
    if subcriber:
        subcriber.has_subcribed = value 
        subcriber.save()
    else:
        return False 

def delete_bot_subcriber(uid:str): 
    subcriber = BotSubcriber.objects.filter(uid=uid).first()
    if subcriber:
        subcriber.delete()

def unsubcribe_bot(uid:str):
    subcriber = BotSubcriber.objects.filter(uid=uid).first()
    if subcriber:
        subcriber.is_active = False 
        subcriber.save()

def set_user_provided_name(uid, user_provided_name:str) -> bool:
    subcriber = BotSubcriber.objects.filter(uid=uid).first()
    if subcriber: 
        subcriber.user_provided_name = user_provided_name
        subcriber.save()
        return True 
    else:
        return False 

def get_user_provided_name(uid:str) -> str:
    subcriber = BotSubcriber.objects.filter(uid=uid).first()
    if subcriber: 
        return subcriber.user_provided_name
    else:
        return 'Unknown'


class Notification(models.Model):
    class Meta:
        verbose_name = "Quản lý thông báo"

    message = models.TextField(verbose_name = 'Nội dung')

    def get_message(self):
        return self.message


class BotUsage(models.Model):
    """Model to log all bot usage for reporting"""
    class Meta:
        verbose_name = "Thống kê sử dụng"

    bot = models.ForeignKey(BotModel, on_delete=models.SET_NULL, null=True)
    subcriber = models.ForeignKey(BotSubcriber, on_delete=models.SET_NULL, null=True)
    feature = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.bot and self.subcriber:
            message = '{0} dùng "{1}" trên bot {2}'.format(self.subcriber.name, self.feature, self.bot.name)
            return message 
        else:
            return "Unknown"