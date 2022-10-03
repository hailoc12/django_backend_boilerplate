from veminhhoa.users.models import User, Pocket, Bill, Notification
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created: # first login
        pocket = Pocket.objects.create(
            user=instance, 
            balance = 0 
        )
        bill = Bill.objects.create(
            pocket = pocket, 
            amount = settings.NEW_USER_REWARD, 
            name = f'Tặng {settings.NEW_USER_REWARD} lượt vẽ tranh miễn phí cho thành viên mới', 
            description = ''
        )

        bill.process_bill()

        Notification.objects.create(
            user = user, 
            name = f'Bạn đã được tặng {settings.NEW_USER_REWARD} lượt vẽ tranh miễn phí', 
            detail = 'Mỗi lượt vẽ tranh tương đương một bức ảnh 512x512 pixel', 
            has_read = False
        )