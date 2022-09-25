from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from veminhhoa.users.forms import UserAdminChangeForm, UserAdminCreationForm
from veminhhoa.users.models import Bill, Notification, Pocket 

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]

class PocketAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')

class BillAdmin(admin.ModelAdmin):
    list_display = ('pocket', 'amount', 'name', 'has_processed')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'has_sent', 'has_read')

admin.site.register(Pocket, PocketAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Notification, NotificationAdmin)