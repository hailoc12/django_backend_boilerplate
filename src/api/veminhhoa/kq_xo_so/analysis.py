from bot_xsmb.kq_xo_so.models import (
    XoSoMienBac, 
    get_yesterday_xsmb_result, 
    XSMB_So_Dep, 
    XSMB_Number_Statistic, 
    XSMB_Quick_Statistic_Loto, 
    XSMB_Quick_Statistic_Giai_Dac_Biet
)

import datetime 
import django 
from typing import List
from collections import Counter 

def calculate_dau_duoi_giai_dac_biet(yesterday_result:XoSoMienBac)->List[str]:
    SAMPLE_RANGE = 3650 # days 
    now_date = django.utils.timezone.now().date()
    from_date = now_date - datetime.timedelta(days=SAMPLE_RANGE)

    # get all ket qua xs 
    list_ket_qua = XoSoMienBac.objects.filter(
        ngay_trao_giai__gte=from_date, 
        ngay_trao_giai__lte=now_date 
    ).order_by('ngay_trao_giai').all()

    length = len(list_ket_qua) - 1 

    giai_db_hom_qua = yesterday_result.get_duoi_giai_dac_biet(number=2)
    
    thong_ke_dau = {
        '0': 0, 
        '1': 0, 
        '2': 0, 
        '3': 0, 
        '4': 0, 
        '5': 0, 
        '6': 0, 
        '7': 0, 
        '8': 0, 
        '9': 0 
    }

    thong_ke_duoi = {
        '0': 0, 
        '1': 0, 
        '2': 0, 
        '3': 0, 
        '4': 0, 
        '5': 0, 
        '6': 0, 
        '7': 0, 
        '8': 0, 
        '9': 0 
    }
    
    # thong ke cac truong hop co giai dac biet trung voi hom qua 
    for i in range(0, length): 
        ket_qua_i = list_ket_qua[i]
        giai_dac_biet = ket_qua_i.get_duoi_giai_dac_biet(number=2)
        if giai_dac_biet != giai_db_hom_qua: 
            continue 
        else: # 
            ket_qua_next = list_ket_qua[i+1] # ket qua ngay tiep theo 
            dau_giai_dac_biet = ket_qua_next.get_dau_giai_dac_biet()
            duoi_giai_dac_biet = ket_qua_next.get_duoi_giai_dac_biet()
            

            thong_ke_dau[dau_giai_dac_biet] += 1 
            thong_ke_duoi[duoi_giai_dac_biet] += 1 

    # tinh dau giai, duoi giai cao nhat 
    thong_ke_dau = list(thong_ke_dau.items())
    thong_ke_dau.sort(key=lambda x:x[1], reverse=True)

    thong_ke_duoi = list(thong_ke_duoi.items())
    thong_ke_duoi.sort(key=lambda x:x[1], reverse=True)

    best_dau = thong_ke_dau[0][0]
    best_cuoi = thong_ke_duoi[0][0]

    return [best_dau, best_cuoi]
            

def calculate_lo_to_kep(yesterday_result:XoSoMienBac)->List[str]:
    SAMPLE_RANGE = 365 # days 
    now_date = django.utils.timezone.now().date()
    from_date = now_date - datetime.timedelta(days=SAMPLE_RANGE)

    # get all ket qua xs 
    list_ket_qua = XoSoMienBac.objects.filter(
        ngay_trao_giai__gte=from_date, 
        ngay_trao_giai__lte=now_date 
    ).order_by('ngay_trao_giai').all()

    length = len(list_ket_qua) - 1 

    giai_db_hom_qua = yesterday_result.get_duoi_giai_dac_biet(number=2)
    
    thong_ke_kep = {}
    
    # thong ke cac truong hop co giai dac biet trung voi hom qua 
    for i in range(0, length): 
        ket_qua_i = list_ket_qua[i]
        giai_dac_biet = ket_qua_i.get_duoi_giai_dac_biet(number=2)
        if giai_dac_biet != giai_db_hom_qua: 
            continue 
        else: # 
            ket_qua_next = list_ket_qua[i+1] # ket qua ngay tiep theo 
            for lo_to_kep in ket_qua_next.ket_qua_kep: 
                if lo_to_kep not in thong_ke_kep: 
                    thong_ke_kep[lo_to_kep] = 1 
                else:
                    thong_ke_kep[lo_to_kep] += 1

    # lay ra 3 lo_to_kep cao nhat 
    thong_ke_kep = list(thong_ke_kep.items())
    thong_ke_kep.sort(key=lambda x:x[1], reverse=True)

    return [thong_ke_kep[0][0], thong_ke_kep[1][0], thong_ke_kep[2][0]]

def calculate_lo_to_sau_giai_dac_biet(yesterday_result:XoSoMienBac, calculate_range=365)->List[str]:
    SAMPLE_RANGE = calculate_range # days 
    today = django.utils.timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    from_date = today - datetime.timedelta(days=SAMPLE_RANGE)

    # get all ket qua xs 
    list_ket_qua = XoSoMienBac.objects.filter(
        ngay_trao_giai__gte=from_date, 
        ngay_trao_giai__lte=yesterday 
    ).order_by('ngay_trao_giai').all()

    length = len(list_ket_qua)

    giai_db_hom_qua = yesterday_result.get_duoi_giai_dac_biet(number=2)
    
    thong_ke_loto = {}
    
    # thong ke cac truong hop co giai dac biet trung voi hom qua 
    for i in range(0, length-1): 
        ket_qua_i = list_ket_qua[i]
        giai_dac_biet = ket_qua_i.get_duoi_giai_dac_biet(number=2)
        if giai_dac_biet != giai_db_hom_qua: 
            continue 
        else: # 
            ket_qua_next = list_ket_qua[i+1] # ket qua ngay tiep theo 
            for lo_to in ket_qua_next.get_all_loto(): 
                if lo_to not in thong_ke_loto: 
                    thong_ke_loto[lo_to] = 1 
                else:
                    thong_ke_loto[lo_to] += 1 

    # lay ra 12 thong_ke_loto cao nhat 
    thong_ke_loto = list(thong_ke_loto.items())
    thong_ke_loto.sort(key=lambda x:x[1], reverse=True)

    return [
        {'lo_to': x[0], 
        'count': x[1]}
        for x in thong_ke_loto[:12]
    ]

def thong_ke_lo_to_dep(list_ket_qua, length, lo_to_cam:str)->List[str]:
    # thong ke cac truong hop co giai dac biet trung voi hom qua 
    thong_ke_dep = {}
    for i in range(0, length): 
        ket_qua_i = list_ket_qua[i]
        list_lo_to_cam = ket_qua_i.get_loto_cam()
        

        if lo_to_cam not in list_lo_to_cam:
            continue 
        else: # 
            ket_qua_next = list_ket_qua[i+1] # ket qua ngay tiep theo 
            for lo_to in ket_qua_next.get_all_loto():
                if lo_to: 
                    if lo_to not in thong_ke_dep: 
                        thong_ke_dep[lo_to] = 1 
                    else:
                        thong_ke_dep[lo_to] += 1

    # lay ra 3 lo_to_kep cao nhat 
    thong_ke_dep = list(thong_ke_dep.items())
    thong_ke_dep.sort(key=lambda x:x[1], reverse=True)

    return [thong_ke_dep[0][0], thong_ke_dep[1][0], thong_ke_dep[2][0]]

def thong_ke_lo_to_dep_in_detail(list_ket_qua, length, lo_to_cam:str)->List[str]:
    # thong ke cac truong hop co giai dac biet trung voi hom qua 
    thong_ke_dep = {}
    for i in range(0, length): 
        ket_qua_i = list_ket_qua[i]
        list_lo_to_cam = ket_qua_i.get_loto_cam()
        
        if lo_to_cam not in list_lo_to_cam:
            continue 
        else: # 
            ket_qua_next = list_ket_qua[i+1] # ket qua ngay tiep theo 
            for lo_to in ket_qua_next.get_all_loto():
                if lo_to: 
                    if lo_to not in thong_ke_dep: 
                        thong_ke_dep[lo_to] = {
                            'lo_to': lo_to, 
                            'count': 1 
                        } 
                    else:
                        thong_ke_dep[lo_to]['count'] += 1

    # lay ra 12 lo_to_kep cao nhat 
    thong_ke_dep = list(thong_ke_dep.items())
    thong_ke_dep.sort(key=lambda x:x[1]['count'], reverse=True)

    return [x[1] for x in thong_ke_dep[:12]]

def calculate_lo_to_dep(yesterday_result:XoSoMienBac, calculate_range=365):
    """
        @Return:
            loto_dau_cam_dep, loto_duoi_cam_dep
                - loto_dau_cam_dep = {
                    '{dau_cam_hom_truoc}': [str, str, str...]
                }
                - loto_duoi_cam_dep = {
                    '{duoi_cam_hom_truoc}': [str, str, str...]
                }
    """
    SAMPLE_RANGE = calculate_range # days 
    now_date = django.utils.timezone.now().date()
    from_date = now_date - datetime.timedelta(days=SAMPLE_RANGE)

    # get all ket qua xs 
    list_ket_qua = XoSoMienBac.objects.filter(
        ngay_trao_giai__gte=from_date, 
        ngay_trao_giai__lte=now_date 
    ).order_by('ngay_trao_giai').all()

    length = len(list_ket_qua) - 1

    # tinh lo to dep 
    dau_cam_hom_qua = yesterday_result.get_dau_cam_loto()
    dau_cam_dep = {}
    for lo_to_cam in dau_cam_hom_qua: 
        lo_to_dau_cam_dep = thong_ke_lo_to_dep(list_ket_qua, length, lo_to_cam)
        dau_cam_dep[lo_to_cam] = lo_to_dau_cam_dep

    duoi_cam_hom_qua = yesterday_result.get_duoi_cam_loto()
    duoi_cam_dep = {}
    for lo_to_cam in duoi_cam_hom_qua: 
        lo_to_duoi_cam_dep = thong_ke_lo_to_dep(list_ket_qua, length, lo_to_cam)
        duoi_cam_dep[lo_to_cam] = lo_to_duoi_cam_dep

    return dau_cam_dep, duoi_cam_dep
    
def calculate_lo_to_dep_in_detail(yesterday_result:XoSoMienBac, calculate_range=365):
    """
        @Return:
            loto_dau_cam_dep, loto_duoi_cam_dep
                - loto_dau_cam_dep = {
                    '{dau_cam_hom_truoc}': [{'lo_to':str, 'count': int}...]
                }
                - loto_duoi_cam_dep = {
                    '{duoi_cam_hom_truoc}': [{'lo_to':str, 'count': int}...]
                }
    """
    SAMPLE_RANGE = calculate_range # days 
    now_date = django.utils.timezone.now().date()
    from_date = now_date - datetime.timedelta(days=SAMPLE_RANGE)

    # get all ket qua xs 
    list_ket_qua = XoSoMienBac.objects.filter(
        ngay_trao_giai__gte=from_date, 
        ngay_trao_giai__lte=now_date 
    ).order_by('ngay_trao_giai').all()

    length = len(list_ket_qua) - 1

    # tinh lo to dep 
    dau_cam_hom_qua = yesterday_result.get_dau_cam_loto()
    dau_cam_dep = {}
    for lo_to_cam in dau_cam_hom_qua: 
        lo_to_dau_cam_dep = thong_ke_lo_to_dep_in_detail(list_ket_qua, length, lo_to_cam)
        dau_cam_dep[lo_to_cam] = lo_to_dau_cam_dep

    duoi_cam_hom_qua = yesterday_result.get_duoi_cam_loto()
    duoi_cam_dep = {}
    for lo_to_cam in duoi_cam_hom_qua: 
        lo_to_duoi_cam_dep = thong_ke_lo_to_dep_in_detail(list_ket_qua, length, lo_to_cam)
        duoi_cam_dep[lo_to_cam] = lo_to_duoi_cam_dep

    return dau_cam_dep, duoi_cam_dep

def calculate_good_number_today():
    yesterday_result = get_yesterday_xsmb_result()
    if not yesterday_result:
        return None 
    
    # calculate xsmb so dep
    today = django.utils.timezone.now().date()
    xsmb_so_dep = XSMB_So_Dep.objects.filter(
        ngay = today
    ).first()

    if not xsmb_so_dep: 

        dau_cam_dep, duoi_cam_dep = calculate_lo_to_dep(yesterday_result)

        xsmb_so_dep = XSMB_So_Dep.objects.create(
            ngay = today, 
            dau_cam_hom_qua = yesterday_result.get_dau_cam_loto(), 
            dau_cam_dep = dau_cam_dep, 
            duoi_cam_hom_qua = yesterday_result.get_duoi_cam_loto(), 
            duoi_cam_dep = duoi_cam_dep, 
            dau_duoi_giai_dac_biet = calculate_dau_duoi_giai_dac_biet(yesterday_result), 
            lo_to_kep = calculate_lo_to_kep(yesterday_result), 
        )

    return xsmb_so_dep

def calculate_number_statistic(date_value:int, date_unit:str, number:int):
    today = django.utils.timezone.now().date()

    if date_unit == 'day': 
        from_date = today - datetime.timedelta(days=date_value)
    elif date_unit == 'month': 
        from_date = today - datetime.timedelta(days=date_value * 30)
    elif date_unit == 'year': 
        from_date = today - datetime.timedelta(days=date_value * 365)
    else:
        return None 

    # get all ket qua xs 
    list_ket_qua = XoSoMienBac.objects.filter(
        ngay_trao_giai__gte=from_date, 
        ngay_trao_giai__lte=today 
    ).order_by('ngay_trao_giai').all()

    occurrences = []

    number_in_text = str(number)
    for ket_qua in list_ket_qua: 
        price_numbers = ket_qua.get_all_price_numbers_detail()
        for price_number in price_numbers:
            if price_number['number'].find(number_in_text, len(price_number['number']) - len(number_in_text)) > 0: 
                occurrences.append(price_number)

    if occurrences: 
        result = XSMB_Number_Statistic(
            from_date = from_date, 
            to_date = today, 
            number=number, 
            number_freq= len(occurrences), 
            occurrences=occurrences
        )
        
        return result 
    else:
        return None 


def _calculate_lo_to_nhieu_nhat_it_nhat(list_ket_qua):
    # dem du lieu 
    count_lo_to = {}
    count_dau = {}
    count_duoi = {}

    for ket_qua in list_ket_qua: 
        lo_to_list = ket_qua.get_all_loto()

        for lo_to in lo_to_list:
            # thong ke dau lo to 
            dau_lo_to = lo_to[0]
            if dau_lo_to not in count_dau:
                count_dau[dau_lo_to] = 1 
            else:
                count_dau[dau_lo_to] += 1 

            # thong ke duoi lo to
            duoi_lo_to = lo_to[1]
            if duoi_lo_to not in count_duoi:
                count_duoi[duoi_lo_to] = 1
            else:
                count_duoi[duoi_lo_to] += 1

            if lo_to not in count_lo_to:
                count_lo_to[lo_to] = 1
            else:
                count_lo_to[lo_to] += 1

    # tinh ket qua thong ke 
    count_lo_to_list = list(count_lo_to.items())
    count_lo_to_list.sort(key = lambda x:x[1])

    lo_to_nhieu_nhat = [
        {'lo_to': x, 
        'count': y}
        for x, y in count_lo_to_list[-12:]
    ]

    lo_to_it_nhat = [
        {'lo_to': x, 
        'count': y}
        for x, y in count_lo_to_list[:12]
    ]

    count_dau_list = list(count_dau.items())
    count_dau_list.sort(key = lambda x:x[0])

    count_cuoi_list = list(count_duoi.items())
    count_cuoi_list.sort(key = lambda x:x[0])

    return lo_to_nhieu_nhat, lo_to_it_nhat, count_dau_list, count_cuoi_list


def _calculate_lo_to_xuat_hien_lien_tiep(appear_dates):
    length = len(appear_dates)
    if length <= 1:
        return 0

    max_lien_tiep = 0
    
    is_in_lien_tiep = False 
    count_lien_tiep = 0 
    last_date = appear_dates[0]
    i = 1
    while i < length-1:
        current_date = appear_dates[i]
        if (current_date == last_date):
            i += 1 
            continue
        elif (current_date-last_date).days == 1: # consecutive date
            if is_in_lien_tiep:
                count_lien_tiep += 1
                if count_lien_tiep > max_lien_tiep:
                    max_lien_tiep = count_lien_tiep
            else:
                is_in_lien_tiep = True 
                count_lien_tiep = 2 
        else:
            is_in_lien_tiep = False
            count_lien_tiep = 0 

        last_date = current_date
        i += 1
    
    return max_lien_tiep    
    

def _calculate_lo_khan_lo_roi(list_ket_qua):
    today = django.utils.timezone.now().date()
    length = len(list_ket_qua)
    index = length-1 
    count_lo_to = {}

    while index > 0:
        ket_qua = list_ket_qua[index]
        lo_to_list = ket_qua.get_all_loto()

        for lo_to in lo_to_list:
            if lo_to not in count_lo_to:
                count_lo_to[lo_to] = {
                    'last_appear_interval': (today - ket_qua.ngay_trao_giai).days, 
                    'appear_dates': [ket_qua.ngay_trao_giai]
                }
            else:
                count_lo_to[lo_to]['appear_dates'].append(ket_qua.ngay_trao_giai)

        index -= 1 


    # tinh lo khan 
    for lo_to in range(0, 100):
        if lo_to < 10:
            lo_to_str = '0' + str(lo_to)
        else:
            lo_to_str = str(lo_to)
        if lo_to_str not in count_lo_to:
            count_lo_to[lo_to_str] = {
                'last_appear_interval': 60, 
                'appear_dates': []
            }

    lo_khan = [{'lo_to': x, 'interval': count_lo_to[x]['last_appear_interval']} for x in count_lo_to if count_lo_to[x]['last_appear_interval'] >= 10]
    lo_khan.sort(key=lambda x:x['interval'], reverse=True)

    # tinh lo roi 
    for lo_to in count_lo_to:
        count_lo_to[lo_to]['appear_dates'].reverse() # make dates asc
        count_lo_to[lo_to]['xh_lien_tiep'] = _calculate_lo_to_xuat_hien_lien_tiep(count_lo_to[lo_to]['appear_dates'])
    
    count_lo_to_list = list(count_lo_to.items())

    count_lo_to_list.sort(key=lambda x:x[1]['xh_lien_tiep'], reverse=True)

    lo_roi = [{'lo_to': x[0], 'count': x[1]['xh_lien_tiep']} for x in count_lo_to_list[:12] if x[1]['xh_lien_tiep'] > 1]
    
    return lo_khan, lo_roi

def calculate_loto_freq(): 
    # get 60 days dataset 
    today = django.utils.timezone.now().date()

    # get result from database 
    result = XSMB_Quick_Statistic_Loto.objects.filter(
        ngay = today, 
    ).first()

    if result: 
        return result 

    # can't get result from database, calculate it 

    yesterday = today - datetime.timedelta(days=1)
    from_date = today - datetime.timedelta(days=60)
    
    list_ket_qua = XoSoMienBac.objects.filter(
        ngay_trao_giai__gte=from_date, 
        ngay_trao_giai__lte=yesterday 
    ).order_by('ngay_trao_giai').all()

    length = len(list_ket_qua)
    yesterday_result = list_ket_qua[length-1]

    lo_to_nhieu_nhat, lo_to_it_nhat, count_dau_list, count_cuoi_list = _calculate_lo_to_nhieu_nhat_it_nhat(list_ket_qua)

    # tinh lo khan 
    lo_khan_list, lo_roi_list = _calculate_lo_khan_lo_roi(list_ket_qua)

    # tinh lo to ve nhieu giai dac biet
    lo_to_ve_nhieu_giai_dac_biet = calculate_lo_to_sau_giai_dac_biet(yesterday_result, calculate_range=365*5)

    # tinh dau cam, duoi cam dep ve nhieu sau giai dac biet
    dau_cam_dep, duoi_cam_dep = calculate_lo_to_dep_in_detail(yesterday_result, calculate_range=365*5)

    result = XSMB_Quick_Statistic_Loto(
        ngay = today, 
        lo_to_nhieu_nhat = lo_to_nhieu_nhat, 
        lo_to_it_nhat = lo_to_it_nhat, 
        lo_khan = lo_khan_list, 
        lo_roi = lo_roi_list, 
        dau_so_freq = count_dau_list, 
        duoi_so_freq = count_cuoi_list, 
        giai_dac_biet_hom_qua = yesterday_result.get_duoi_giai_dac_biet(number=2),
        lo_to_ve_nhieu_giai_dac_biet = lo_to_ve_nhieu_giai_dac_biet, 
        lo_to_ve_nhieu_dau_cam = dau_cam_dep, 
        lo_to_ve_nhieu_duoi_cam = duoi_cam_dep
    )

    return result 

def _calculate_hai_so_cuoi_giai_dac_biet(list_ket_qua_30): 
    result = []
    for ket_qua in list_ket_qua_30: 
        result.append(
            {
                'day': ket_qua.ngay_trao_giai.strftime('%d/%m/%y'), 
                'giai_dac_biet': ket_qua.get_duoi_giai_dac_biet(number=2)
            }
        )
    return result 

def _calculate_giai_dac_biet_lau_ve_nhat(count_2_so_cuoi, date_range=365):
    # tinh giai dac biet khan 
    today = django.utils.timezone.now().date()

    for dac_biet in range(0, 100):
        if dac_biet < 10:
            dac_biet_str = '0' + str(dac_biet)
        else:
            dac_biet_str = str(dac_biet)

        if dac_biet_str not in count_2_so_cuoi:
            pass 
            # count_2_so_cuoi[dac_biet_str] = {
            #     'last_appear_interval': date_range, 
            #     'occurence': []
            # }
        else:
            count_2_so_cuoi[dac_biet_str]['last_appear_interval'] = (today - count_2_so_cuoi[dac_biet_str]['occurence'][-1]).days

    dac_biet_khan = [{'giai_dac_biet': x, 'interval': count_2_so_cuoi[x]['last_appear_interval']} for x in count_2_so_cuoi if count_2_so_cuoi[x]['last_appear_interval'] >= 10]
    dac_biet_khan.sort(key=lambda x:x['interval'], reverse=True)
    return dac_biet_khan

def _calculate_dau_cuoi_giai_dac_biet(date_range=365):
    today = django.utils.timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    from_date = today - datetime.timedelta(days=date_range)
    
    list_ket_qua = XoSoMienBac.objects.filter(
        ngay_trao_giai__gte=from_date, 
        ngay_trao_giai__lte=yesterday 
    ).order_by('ngay_trao_giai').all()

    count_2_so_cuoi = {}
    count_dau = {}
    count_cuoi = {}

    # dem ket qua 
    for ket_qua in list_ket_qua: 
        hai_so_cuoi = ket_qua.get_duoi_giai_dac_biet(number=2)
        
        if hai_so_cuoi not in count_2_so_cuoi:
            count_2_so_cuoi[hai_so_cuoi] = {
                'count': 1, 
                'occurence': [
                    ket_qua.ngay_trao_giai
                ]
            }
        else:
            count_2_so_cuoi[hai_so_cuoi]['count'] += 1

        if hai_so_cuoi[0] not in count_dau: 
            count_dau[hai_so_cuoi[0]] = 1
        else:
            count_dau[hai_so_cuoi[0]] += 1

        if hai_so_cuoi[1] not in count_cuoi:
            count_cuoi[hai_so_cuoi[1]] = 1
        else:
            count_cuoi[hai_so_cuoi[1]] += 1

    # thong ke 
    count_2_so_cuoi_list = list(count_2_so_cuoi.items())
    count_2_so_cuoi_list.sort(key=lambda x:x[1]['count'], reverse=True)

    # drop 'occurence' from result 
    count_2_so_cuoi_result = [
        (x, {'count': y['count']})
        for x, y in count_2_so_cuoi_list
    ]
    
    count_dau_list = list(count_dau.items())
    count_dau_list.sort(key=lambda x:x[1], reverse=True)

    count_cuoi_list = list(count_cuoi.items())
    count_cuoi_list.sort(key=lambda x:x[1], reverse=True)



    return count_2_so_cuoi_result[:12], count_dau_list[:12], count_cuoi_list[:12]

def _calculate_giai_dac_biet_lau_ve(date_range=3650):
    today = django.utils.timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    from_date = today - datetime.timedelta(days=date_range)
    
    list_ket_qua = XoSoMienBac.objects.filter(
        ngay_trao_giai__gte=from_date, 
        ngay_trao_giai__lte=yesterday 
    ).order_by('ngay_trao_giai').all()

    count_2_so_cuoi = {}

    # dem ket qua 
    for ket_qua in list_ket_qua: 
        hai_so_cuoi = ket_qua.get_duoi_giai_dac_biet(number=2)
        
        if hai_so_cuoi not in count_2_so_cuoi:
            count_2_so_cuoi[hai_so_cuoi] = {
                'count': 1, 
                'occurence': [
                    ket_qua.ngay_trao_giai
                ]
            }
        else:
            count_2_so_cuoi[hai_so_cuoi]['count'] += 1
            count_2_so_cuoi[hai_so_cuoi]['occurence'].append(ket_qua.ngay_trao_giai)

    # danh sach 2 so cuoi lau ve nhat
    count_lau_ve_nhat = _calculate_giai_dac_biet_lau_ve_nhat(count_2_so_cuoi, date_range=date_range)
    return count_lau_ve_nhat[:12]


def _calculate_giai_dac_biet_ve_nhieu_nhat_hom_sau(date_range=3650):
    today = django.utils.timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    from_date = today - datetime.timedelta(days=date_range)
    
    list_ket_qua = XoSoMienBac.objects.filter(
        ngay_trao_giai__gte=from_date, 
        ngay_trao_giai__lte=yesterday 
    ).order_by('ngay_trao_giai').all()

    length = len(list_ket_qua)

    yesterday_result = list_ket_qua[length-1]
    giai_db_hom_qua = yesterday_result.get_duoi_giai_dac_biet(number=2)

    index = 0 
    count_next_kq = {}

    for index in range(0, length-1): 
        ket_qua = list_ket_qua[index]
        giai_dac_biet = ket_qua.get_duoi_giai_dac_biet(number=2)
        if giai_dac_biet != giai_db_hom_qua: 
            continue
        else:
            next_ket_qua = list_ket_qua[index+1]
            next_giai_dac_biet = next_ket_qua.get_duoi_giai_dac_biet(number=2)
            
            if next_giai_dac_biet not in count_next_kq:
                count_next_kq[next_giai_dac_biet] = 1 
            else:
                count_next_kq[next_giai_dac_biet] += 1 

    count_next_kq_list = list(count_next_kq.items())
    count_next_kq_list.sort(key=lambda x:x[1], reverse=True)

    return count_next_kq_list[:12]

def calculate_giai_dac_biet_freq():
    today = django.utils.timezone.now().date()
    
    # get result from database 
    result = XSMB_Quick_Statistic_Giai_Dac_Biet.objects.filter(
        ngay = today, 
    ).first()

    if result: 
        return result 

    # can't get result from database, calculate it 
    yesterday = today - datetime.timedelta(days=1)
    from_date_30 = today - datetime.timedelta(days=30)
    
    list_ket_qua_30 = XoSoMienBac.objects.filter(
        ngay_trao_giai__gte=from_date_30, 
        ngay_trao_giai__lte=today 
    ).order_by('ngay_trao_giai').all()

    length = len(list_ket_qua_30)
    yesterday_result = list_ket_qua_30[length-1]
    giai_db_hom_qua = yesterday_result.get_duoi_giai_dac_biet(number=2)

    # hai so cuoi giai dac biet trong 30 ngay 
    list_hai_so_cuoi_giai_dac_biet = _calculate_hai_so_cuoi_giai_dac_biet(list_ket_qua_30)

    # 2 so cuoi giai dac biet ve nhieu trong 365 
    hai_so_cuoi_365, dau_so_cuoi_365, duoi_so_cuoi_365 = _calculate_dau_cuoi_giai_dac_biet(date_range=365)
    hai_so_cuoi_lau_ve = _calculate_giai_dac_biet_lau_ve(date_range=3650)

    # giai dac biet ve nhieu nhat hom sau
    giai_db_ve_nhieu_nhat_hom_sau = _calculate_giai_dac_biet_ve_nhieu_nhat_hom_sau(date_range=3650)

    result = XSMB_Quick_Statistic_Giai_Dac_Biet(
        ngay = today, 
        hai_so_cuoi_30 = list_hai_so_cuoi_giai_dac_biet, 
        hai_so_cuoi_365 = hai_so_cuoi_365, 
        dau_so_cuoi_365 = dau_so_cuoi_365, 
        duoi_so_cuoi_365 = duoi_so_cuoi_365, 
        hai_so_cuoi_lau_ve_365 = hai_so_cuoi_lau_ve, 
        giai_db_hom_qua = giai_db_hom_qua, 
        giai_db_ve_nhieu_nhat_hom_sau = giai_db_ve_nhieu_nhat_hom_sau 
    )
    result.save()

    return result 

