from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django_better_admin_arrayfield.models.fields import ArrayField

import datetime 
import django 

class XSMB_Number_Statistic(models.Model):
    from_date = models.DateField(verbose_name='Từ ngày')
    to_date = models.DateField(verbose_name='Tới ngày')
    number = models.IntegerField(verbose_name='Số thống kê', default=0)
    number_freq = models.IntegerField(verbose_name='Số lần xuất hiện', default=0)
    occurrences = models.JSONField(verbose_name="Xuất hiện", blank=True, null=True)

class XSMB_Quick_Statistic_Loto(models.Model):
    ngay = models.DateField(verbose_name='Ngày thống kê')
    giai_dac_biet_hom_qua = models.TextField(default='', verbose_name="Giải đặc biệt hôm qua", blank=True)
    lo_to_nhieu_nhat = models.JSONField(verbose_name="Lô tô nhiều nhất", blank=True, null=True)
    lo_to_it_nhat = models.JSONField(verbose_name="Lô tô ít nhất", blank=True, null=True)
    lo_khan = models.JSONField(verbose_name="Lô tô khan", blank=True, null=True)
    lo_roi = models.JSONField(verbose_name="Lô rơi", blank=True, null=True)
    dau_so_freq = models.JSONField(verbose_name="Đầu số", blank=True, null=True)
    duoi_so_freq = models.JSONField(verbose_name="Đuôi số", blank=True, null=True)
    lo_to_ve_nhieu_giai_dac_biet = models.JSONField(verbose_name="Lô tô về nhiều", blank=True, null=True)
    lo_to_ve_nhieu_dau_cam = models.JSONField(verbose_name="Lô tô về nhiều đầu câm", blank=True, null=True)
    lo_to_ve_nhieu_duoi_cam = models.JSONField(verbose_name="Lô tô về nhiều đuôi câm", blank=True, null=True)

class XSMB_Quick_Statistic_Giai_Dac_Biet(models.Model):
    ngay = models.DateField(verbose_name='Ngày thống kê')
    hai_so_cuoi_30 = models.JSONField(verbose_name="Hai số cuối 30 ngày", blank=True, null=True)
    hai_so_cuoi_365 = models.JSONField(verbose_name="Hai số cuối 365 ngày", blank=True, null=True)
    dau_so_cuoi_365 = models.JSONField(verbose_name="Đầu hai số cuối 365 ngày", blank=True, null=True)
    duoi_so_cuoi_365 = models.JSONField(verbose_name="Đầu hai số cuối 365 ngày", blank=True, null=True)
    hai_so_cuoi_lau_ve_365 = models.JSONField(verbose_name="Hai số cuối lâu về 365 ngày", blank=True, null=True)
    giai_db_hom_qua = models.TextField(default='', verbose_name="Giải đặc biệt hôm qua", blank=True)
    giai_db_ve_nhieu_nhat_hom_sau = models.JSONField(verbose_name="Giải đặc biệt về nhiều nhất hôm sau", blank=True, null=True)

class XSMB_So_Dep(models.Model):
    ngay = models.DateField(verbose_name='Ngày trao giải')

    dau_duoi_giai_dac_biet = ArrayField(
        models.TextField(default='', verbose_name="Đầu đuôi đặc biệt", blank=True)
    )     

    lo_to_kep = ArrayField(
        models.TextField(default='', verbose_name="Lô tô kép", blank=True)
    )     

    dau_cam_hom_qua = ArrayField(
        models.TextField(default='', verbose_name="Đầu câm hôm qua", blank=True)
    )     

    dau_cam_dep = models.JSONField(verbose_name="Đầu câm đẹp", blank=True, null=True)

    duoi_cam_hom_qua = ArrayField(
        models.TextField(default='', verbose_name="Đuôi câm hôm qua", blank=True)
    )  

    duoi_cam_dep = models.JSONField(verbose_name="Đuôi câm đẹp", blank=True, null=True)

class XoSoMienBac(models.Model):
    ngay_trao_giai = models.DateField(verbose_name='Ngày trao giải')

    giai_dac_biet = ArrayField(
        models.TextField(default='', verbose_name="Giải đặc biệt", blank=True)
    )

    giai_nhat = ArrayField(
        models.TextField(default='', verbose_name="Giải nhất", blank=True), 
    )
    giai_nhi = ArrayField(
        models.TextField(default='', verbose_name="Giải nhì", blank=True)
    )
    giai_ba = ArrayField(
        models.TextField(default='', verbose_name="Giải ba", blank=True)
    )
    giai_tu = ArrayField(
        models.TextField(default='', verbose_name="Giải tư", blank=True)
    )
    giai_nam = ArrayField(
        models.TextField(default='', verbose_name="Giải năm", blank=True)
    )
    giai_sau = ArrayField(
        models.TextField(default='', verbose_name="Giải sáu", blank=True)
    )
    giai_bay = ArrayField(
        models.TextField(default='', verbose_name="Giải bảy", blank=True)
    )
    dau_lo_to_dau0 = ArrayField(
        models.TextField(default=[], verbose_name="Đầu lô tô đầu 0", blank=True), 
        null=True,
    )
    dau_lo_to_dau1 = ArrayField(
        models.TextField(default=[], verbose_name="Đầu lô tô đầu 1", blank=True), 
        null=True,
    )
    dau_lo_to_dau2 = ArrayField(
        models.TextField(default=[], verbose_name="Đầu lô tô đầu 2", blank=True), 
        null=True,
    )
    dau_lo_to_dau3 = ArrayField(
        models.TextField(default=[], verbose_name="Đầu lô tô đầu 3", blank=True), 
        null=True,
    )
    dau_lo_to_dau4 = ArrayField(
        models.TextField(default=[], verbose_name="Đầu lô tô đầu 4", blank=True), 
        null=True,
    )
    dau_lo_to_dau5 = ArrayField(
        models.TextField(default=[], verbose_name="Đầu lô tô đầu 5", blank=True), 
        null=True,
    )
    dau_lo_to_dau6 = ArrayField(
        models.TextField(default='', verbose_name="Đầu lô tô đầu 6", blank=True), 
        null=True,
    )
    dau_lo_to_dau7 = ArrayField(
        models.TextField(default='', verbose_name="Đầu lô tô đầu 7", blank=True),
        null=True,
    )
    dau_lo_to_dau8 = ArrayField(
        models.TextField(default='', verbose_name="Đầu lô tô đầu 8", blank=True),
        null=True,
    )
    dau_lo_to_dau9 = ArrayField(
        models.TextField(default='', verbose_name="Đầu lô tô đầu 9", blank=True),
        null=True,
    )

    duoi_lo_to_dau0 = ArrayField(
        models.TextField(default='', verbose_name="Đuôi lô tô đầu 0", blank=True),
        null=True,
    )
    duoi_lo_to_dau1 = ArrayField(
        models.TextField(default='', verbose_name="Đuôi lô tô đầu 1", blank=True),
        null=True,
    )
    duoi_lo_to_dau2 = ArrayField(
        models.TextField(default='', verbose_name="Đuôi lô tô đầu 2", blank=True), 
        null=True,
    )
    duoi_lo_to_dau3 = ArrayField(
        models.TextField(default='', verbose_name="Đuôi lô tô đầu 3", blank=True),
        null=True,
    )
    duoi_lo_to_dau4 = ArrayField(
        models.TextField(default='', verbose_name="Đuôi lô tô đầu 4", blank=True), 
        null=True,
    )
    duoi_lo_to_dau5 = ArrayField(
        models.TextField(default='', verbose_name="Đuôi lô tô đầu 5", blank=True), 
        null=True,
    )
    duoi_lo_to_dau6 = ArrayField(
        models.TextField(default='', verbose_name="Đuôi lô tô đầu 6", blank=True), 
        null=True,
    )
    duoi_lo_to_dau7 = ArrayField(
        models.TextField(default='', verbose_name="Đuôi lô tô đầu 7", blank=True), 
        null=True,
    )
    duoi_lo_to_dau8 = ArrayField(
        models.TextField(default='', verbose_name="Đuôi lô tô đầu 8", blank=True), 
        null=True,
    )
    duoi_lo_to_dau9 = ArrayField(
        models.TextField(default='', verbose_name="Đuôi lô tô đầu 9", blank=True), 
        null=True,
    )

    ket_qua_kep = ArrayField(
        models.TextField(default='', verbose_name="Kép", blank=True), 
        null=True,
    )

    def get_giai_dac_biet(self): 
        if self.giai_dac_biet:
            return self.giai_dac_biet[0]
        else:
            return None 

    def get_duoi_giai_dac_biet(self, number:int=1):
        giai_dac_biet = self.get_giai_dac_biet()
        if giai_dac_biet:
            return giai_dac_biet[-number:]
        else:
            return None 

    def get_dau_giai_dac_biet(self, number:int=1):
        giai_dac_biet = self.get_giai_dac_biet()
        if giai_dac_biet:
            return giai_dac_biet[:number]
        else:
            return None 


    def get_all_price_numbers_detail(self):
        price_fields = [
                {
                    'value': self.giai_dac_biet, 
                    'name': "Giải đặc biệt", 
                }, 
                {
                    'value': self.giai_nhat,
                    'name': "Giải nhất", 
                }, 
                {
                    'value': self.giai_nhi,
                    'name': "Giải nhì"
                },
                {
                    'value': self.giai_ba, 
                    'name': "Giải ba"
                }, 
                {
                    'value': self.giai_tu, 
                    'name': 'Giải tư', 
                }, 
                {
                    'value': self.giai_nam,
                    'name': 'Giải năm', 
                },  
                {
                    'value': self.giai_sau,
                    'name': "Giải sáu"
                }, 
                {
                    'value': self.giai_bay, 
                    'name': "Giải bảy"
                }
        ]

        numbers = []
        for item in price_fields:
            values = item['value']
            name = item['name']
            for number in values:
                numbers.append(
                    {
                        'number': number, 
                        'giai': name, 
                        'date': self.ngay_trao_giai
                    }
                )

        return numbers 


    def get_all_price_numbers(self):
        price_fields = [
                self.giai_dac_biet, self.giai_nhat, self.giai_nhi, self.giai_ba, 
                self.giai_tu, self.giai_nam, self.giai_sau, self.giai_bay
        ]

        numbers = []
        for field in price_fields:
                numbers.extend(field)
        return numbers 

    def _assign_number_to_dau_lo_to_field(self, number): 
        dau_lo_to = number[-2:]
        
        if dau_lo_to[0] == '0': 
                self.dau_lo_to_dau0 = self._append_to_lo_to_field(self.dau_lo_to_dau0, dau_lo_to)
        elif dau_lo_to[0] == '1': 
                self.dau_lo_to_dau1 = self._append_to_lo_to_field(self.dau_lo_to_dau1, dau_lo_to)
        elif dau_lo_to[0] == '2': 
                self.dau_lo_to_dau2 = self._append_to_lo_to_field(self.dau_lo_to_dau2, dau_lo_to)
        elif dau_lo_to[0] == '3': 
                self.dau_lo_to_dau3 = self._append_to_lo_to_field(self.dau_lo_to_dau3, dau_lo_to)
        elif dau_lo_to[0] == '4': 
                self.dau_lo_to_dau4 = self._append_to_lo_to_field(self.dau_lo_to_dau4, dau_lo_to)
        elif dau_lo_to[0] == '5': 
                self.dau_lo_to_dau5 = self._append_to_lo_to_field(self.dau_lo_to_dau5, dau_lo_to)
        elif dau_lo_to[0] == '6': 
                self.dau_lo_to_dau6 = self._append_to_lo_to_field(self.dau_lo_to_dau6, dau_lo_to)
        elif dau_lo_to[0] == '7': 
                self.dau_lo_to_dau7 = self._append_to_lo_to_field(self.dau_lo_to_dau7, dau_lo_to)
        elif dau_lo_to[0] == '8': 
                self.dau_lo_to_dau8 = self._append_to_lo_to_field(self.dau_lo_to_dau8, dau_lo_to)
        elif dau_lo_to[0] == '9': 
                self.dau_lo_to_dau9 = self._append_to_lo_to_field(self.dau_lo_to_dau9, dau_lo_to)
        else:
                pass 

    def _append_to_lo_to_field(self, field, number):
        if not field: 
                field = [] 
        field.append(number)
        return field  

    def _assign_number_to_cuoi_lo_to_field(self, number): 
        cuoi_lo_to = number[-2:]
        
        if cuoi_lo_to[-1] == '0': 
                self.duoi_lo_to_dau0 = self._append_to_lo_to_field(self.duoi_lo_to_dau0, cuoi_lo_to)
        elif cuoi_lo_to[-1] == '1': 
                self.duoi_lo_to_dau1 = self._append_to_lo_to_field(self.duoi_lo_to_dau1, cuoi_lo_to)
        elif cuoi_lo_to[-1] == '2': 
                self.duoi_lo_to_dau2 = self._append_to_lo_to_field(self.duoi_lo_to_dau2, cuoi_lo_to)
        elif cuoi_lo_to[-1] == '3': 
                self.duoi_lo_to_dau3 = self._append_to_lo_to_field(self.duoi_lo_to_dau3, cuoi_lo_to)
        elif cuoi_lo_to[-1] == '4': 
                self.duoi_lo_to_dau4 = self._append_to_lo_to_field(self.duoi_lo_to_dau4, cuoi_lo_to)
        elif cuoi_lo_to[-1] == '5': 
                self.duoi_lo_to_dau5 = self._append_to_lo_to_field(self.duoi_lo_to_dau5, cuoi_lo_to)
        elif cuoi_lo_to[-1] == '6': 
                self.duoi_lo_to_dau6 = self._append_to_lo_to_field(self.duoi_lo_to_dau6, cuoi_lo_to)
        elif cuoi_lo_to[-1] == '7': 
                self.duoi_lo_to_dau7 = self._append_to_lo_to_field(self.duoi_lo_to_dau7, cuoi_lo_to)
        elif cuoi_lo_to[-1] == '8': 
                self.duoi_lo_to_dau8 = self._append_to_lo_to_field(self.duoi_lo_to_dau8, cuoi_lo_to)
        elif cuoi_lo_to[-1] == '9': 
                self.duoi_lo_to_dau9 = self._append_to_lo_to_field(self.duoi_lo_to_dau9, cuoi_lo_to)
        else:
                pass 

    def _assign_number_to_double_loto_field(self, number): 
        # dau_lo_to = number[-2:]
        cuoi_lo_to = number[-2:]

        # if dau_lo_to[0] == dau_lo_to[1]:
        #         self.ket_qua_kep = self._append_to_lo_to_field(self.ket_qua_kep, dau_lo_to)

        if cuoi_lo_to[0] == cuoi_lo_to[1]:
                self.ket_qua_kep = self._append_to_lo_to_field(self.ket_qua_kep, cuoi_lo_to)


    def recalculate_loto(self): 
        self.duoi_lo_to_dau0 = [] 
        self.duoi_lo_to_dau1 = [] 
        self.duoi_lo_to_dau2 = [] 
        self.duoi_lo_to_dau3 = [] 
        self.duoi_lo_to_dau4 = [] 
        self.duoi_lo_to_dau5 = [] 
        self.duoi_lo_to_dau6 = [] 
        self.duoi_lo_to_dau7 = [] 
        self.duoi_lo_to_dau8 = [] 
        self.duoi_lo_to_dau9 = [] 
        
        self.dau_lo_to_dau0 = []
        self.dau_lo_to_dau1 = []
        self.dau_lo_to_dau2 = [] 
        self.dau_lo_to_dau3 = [] 
        self.dau_lo_to_dau4 = [] 
        self.dau_lo_to_dau5 = [] 
        self.dau_lo_to_dau6 = [] 
        self.dau_lo_to_dau7 = [] 
        self.dau_lo_to_dau8 = [] 
        self.dau_lo_to_dau9 = [] 

        self.ket_qua_kep = []

        self.auto_calculate_loto(save_after=True)

    def auto_calculate_loto(self, save_after=False):
        """Autofill loto fields with data calculated from price fields"""
        numbers = self.get_all_price_numbers()
        for number in numbers:
            self._assign_number_to_dau_lo_to_field(number)
            self._assign_number_to_cuoi_lo_to_field(number)
            self._assign_number_to_double_loto_field(number)
        
        if save_after:
                self.save()

    def _is_empty_lo_to(self, field):
        return (not field) or (not field[0])

    def get_dau_cam_loto(self):
        dau_cam = []
        if self._is_empty_lo_to(self.dau_lo_to_dau0):
            dau_cam.append('0')
        
        if self._is_empty_lo_to(self.dau_lo_to_dau1):
            dau_cam.append('1')

        if self._is_empty_lo_to(self.dau_lo_to_dau2):
            dau_cam.append('2')

        if self._is_empty_lo_to(self.dau_lo_to_dau3):
            dau_cam.append('3')
    
        if self._is_empty_lo_to(self.dau_lo_to_dau4):
            dau_cam.append('4')

        if self._is_empty_lo_to(self.dau_lo_to_dau5):
            dau_cam.append('5')

        if self._is_empty_lo_to(self.dau_lo_to_dau6):
            dau_cam.append('6')

        if self._is_empty_lo_to(self.dau_lo_to_dau7):
            dau_cam.append('7')

        if self._is_empty_lo_to(self.dau_lo_to_dau8):
            dau_cam.append('8')

        if self._is_empty_lo_to(self.dau_lo_to_dau9):
            dau_cam.append('9')

        return dau_cam

    def get_duoi_cam_loto(self):
        duoi_cam = []
        if self._is_empty_lo_to(self.duoi_lo_to_dau0):
            duoi_cam.append('0')
        
        if self._is_empty_lo_to(self.duoi_lo_to_dau1):
            duoi_cam.append('1')

        if self._is_empty_lo_to(self.duoi_lo_to_dau2):
            duoi_cam.append('2')

        if self._is_empty_lo_to(self.duoi_lo_to_dau3):
            duoi_cam.append('3')
    
        if self._is_empty_lo_to(self.duoi_lo_to_dau4):
            duoi_cam.append('4')

        if self._is_empty_lo_to(self.duoi_lo_to_dau5):
            duoi_cam.append('5')

        if self._is_empty_lo_to(self.duoi_lo_to_dau6):
            duoi_cam.append('6')

        if self._is_empty_lo_to(self.duoi_lo_to_dau7):
            duoi_cam.append('7')

        if self._is_empty_lo_to(self.duoi_lo_to_dau8):
            duoi_cam.append('8')

        if self._is_empty_lo_to(self.duoi_lo_to_dau9):
            duoi_cam.append('9')

        return duoi_cam

    def get_loto_cam(self):
        dau_cam = self.get_dau_cam_loto()
        duoi_cam = self.get_duoi_cam_loto() 
        dau_cam.extend(duoi_cam)
        return dau_cam

    def get_all_loto(self):
        result = []
        if self.dau_lo_to_dau0: 
            result.extend(self.dau_lo_to_dau0)
        if self.dau_lo_to_dau1: 
            result.extend(self.dau_lo_to_dau1)
        if self.dau_lo_to_dau2: 
            result.extend(self.dau_lo_to_dau2)
        if self.dau_lo_to_dau3: 
            result.extend(self.dau_lo_to_dau3)
        if self.dau_lo_to_dau4: 
            result.extend(self.dau_lo_to_dau4)
        if self.dau_lo_to_dau5: 
            result.extend(self.dau_lo_to_dau5)
        if self.dau_lo_to_dau6: 
            result.extend(self.dau_lo_to_dau6)
        if self.dau_lo_to_dau7: 
            result.extend(self.dau_lo_to_dau7)
        if self.dau_lo_to_dau8: 
            result.extend(self.dau_lo_to_dau8)
        if self.dau_lo_to_dau9: 
            result.extend(self.dau_lo_to_dau9)

        if self.duoi_lo_to_dau0: 
            result.extend(self.duoi_lo_to_dau0)
        if self.duoi_lo_to_dau1: 
            result.extend(self.duoi_lo_to_dau1)
        if self.duoi_lo_to_dau2: 
            result.extend(self.duoi_lo_to_dau2)
        if self.duoi_lo_to_dau3: 
            result.extend(self.duoi_lo_to_dau3)
        if self.duoi_lo_to_dau4: 
            result.extend(self.duoi_lo_to_dau4)
        if self.duoi_lo_to_dau5: 
            result.extend(self.duoi_lo_to_dau5)
        if self.duoi_lo_to_dau6: 
            result.extend(self.duoi_lo_to_dau6)
        if self.duoi_lo_to_dau7: 
            result.extend(self.duoi_lo_to_dau7)
        if self.duoi_lo_to_dau8: 
            result.extend(self.duoi_lo_to_dau8)
        if self.duoi_lo_to_dau9: 
            result.extend(self.duoi_lo_to_dau9)
        
        return result 

    def __str__(self):
        try: 
            return self.ngay_trao_giai.strftime("Kết quả XSMB ngày %d/%m/%y")
        except:
            return "Unknown"

def get_latest_xsmb_result():
        return XoSoMienBac.objects.latest('ngay_trao_giai')

def get_yesterday_xsmb_result():
    today = django.utils.timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    
    xsmb_result = XoSoMienBac.objects.filter(
        ngay_trao_giai = yesterday
    ).first()

    return xsmb_result

def check_if_specific_xsmb_result_exist(date:datetime.date)-> bool:
    return XoSoMienBac.objects.filter(
        ngay_trao_giai = date
    ).exists()