import django
from django.core.management.base import BaseCommand
from django.conf import settings
from bot_xsmb.kq_xo_so.models import XoSoMienBac

class Command(BaseCommand):
    def handle(self, **options):
        for ketqua in XoSoMienBac.objects.all():
            ketqua.recalculate_loto()
        print("OK")

