from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import AllowAny

class User(AbstractUser):
    """
    Default custom user model for veminhhoa.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class Notification(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.TextField(blank=True)
    detail = models.TextField(blank=True)
    has_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

class Pocket(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    balance = models.FloatField(default=0)

    def change_balance(self, amount):
        self.balance += amount 
        self.save()

class Bill(models.Model):
    pocket = models.ForeignKey(Pocket, null=True, on_delete=models.SET_NULL)
    amount = models.FloatField(default=0)
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    has_processed = models.BooleanField(default=False)

    def process_bill(self):
        if not self.has_processed:
            self.pocket.change_balance(self.amount)
            self.has_processed = True
            self.save()

