import datetime 
import django 

from viberbot.api.messages import (
    TextMessage,
    ContactMessage,
    PictureMessage,
    VideoMessage, 
    KeyboardMessage
)

from bot_xsmb.bots.lib.bot_messages import (
    BOT_MESSAGES, VIBER_COMMAND_KEYBOARD_FREEUSER, VIBER_COMMAND_KEYBOARD_START_USING_BOT, 
    BOT_FEATURE_1_TEXT, BOT_FEATURE_2_TEXT, 
    BOT_FEATURE_3_TEXT, BOT_FEATURE_3_ASK_FOR_STATISTIC_TYPE_INPUT, BOT_FEATURE_3_STATISTIC_TYPE_KEYBOARD_COMMAND, BOT_FEATURE_3_INVALID_STATISTIC_TYPE_INPUT, 
    BOT_FEATURE_4_TEXT, 
    #BOT_FEATURE_5_TEXT,
    BOT_FEATURE_6_TEXT, BOT_FEATURE_6_CONTINUE_DISPLAY, BOT_FEATURE_6_ASK_FOR_DATE_RANGE_INPUT, BOT_FEATURE_6_DATE_RANGE_KEYBOARD_COMMAND, 
    BOT_FEATURE_7_TEXT, BOT_FEATURE_7_QR_URL, BOT_FEATURE_7_QR_TEXT, BOT_FEATURE_7_SHARE_BOT_COMMAND, 
    YES_NO_COMMAND_BOARD
)

from bot_xsmb.bots.lib.utils import get_weekday_translation

from bot_xsmb.kq_xo_so.models import (
    XSMB_So_Dep, 
    XSMB_Number_Statistic, 
    XSMB_Quick_Statistic_Loto, 
    XSMB_Quick_Statistic_Giai_Dac_Biet
)

def send_welcome_after_subcribe_free_viber_bot(viber, uid, subcriber_name):
    viber.send_messages(
        to=uid, 
        messages=[
            TextMessage(text=BOT_MESSAGES['FREE_VIBER_BOT_AFTER_SUBCRIBE'].format(subcriber_name)),
            TextMessage(text=BOT_MESSAGES['FREE_VIBER_BOT_START_COMMAND']),
            KeyboardMessage(keyboard=VIBER_COMMAND_KEYBOARD_FREEUSER)
        ]
    )

def display_free_viber_command_keyboard(viber, uid, hide_message=False):
    if hide_message: 
        messages =  [
            KeyboardMessage(keyboard=VIBER_COMMAND_KEYBOARD_FREEUSER)
        ]
    else: 
        messages =  [
            TextMessage(text=BOT_MESSAGES['FREE_VIBER_BOT_START_COMMAND']),
            KeyboardMessage(keyboard=VIBER_COMMAND_KEYBOARD_FREEUSER)
        ]

    viber.send_messages(
        to=uid, 
        messages=messages
    )

def display_feature_6_date_range_command_keyboard(viber, uid, message):
    messages =  [
        TextMessage(text=message),
        KeyboardMessage(keyboard=BOT_FEATURE_6_DATE_RANGE_KEYBOARD_COMMAND)
    ]

    viber.send_messages(
        to=uid, 
        messages=messages
    )

def display_feature_3_statistic_type_command_keyboard(viber, uid):
    messages =  [
        TextMessage(text=BOT_FEATURE_3_ASK_FOR_STATISTIC_TYPE_INPUT),
        KeyboardMessage(keyboard=BOT_FEATURE_3_STATISTIC_TYPE_KEYBOARD_COMMAND)
    ]

    viber.send_messages(
        to=uid, 
        messages=messages
    )

def display_feature_3_invalid_statistic_type(viber, uid): 
    messages =  [
        TextMessage(text=BOT_FEATURE_3_INVALID_STATISTIC_TYPE_INPUT),
    ]

    viber.send_messages(
        to=uid, 
        messages=messages
    )


def display_yes_no_command_keyboard(viber, uid):
    messages =  [
        KeyboardMessage(keyboard=YES_NO_COMMAND_BOARD)
    ]

    viber.send_messages(
        to=uid, 
        messages=messages
    )

def display_unrecognized_command(viber, uid:str, unrecognized_command:str):
    viber.send_messages(
        to=uid, 
        messages=[
            TextMessage(text=BOT_MESSAGES['FREE_VIBER_BOT_UNRECOGNIZED_COMMAND'].format(unrecognized_command)),
        ]
    )

def display_free_viber_in_development_feature(viber, uid):
    viber.send_messages(
        to=uid, 
        messages=[
            TextMessage(text=BOT_MESSAGES['IN_DEVELOPMENT_FEATURE_MESSAGE']),
            KeyboardMessage(keyboard=VIBER_COMMAND_KEYBOARD_FREEUSER)
        ]
    )

def display_guide_on_auto_alert_feature(viber, uid): 
    viber.send_messages(
        to=uid, 
        messages=[
            TextMessage(text=BOT_MESSAGES['GUIDE_ON_AUTO_ALERT_FEATURE']),
            KeyboardMessage(keyboard=VIBER_COMMAND_KEYBOARD_FREEUSER)
        ]
    )

def append_loto_field_display(message, result_list): 
    if result_list:
        result_list.sort()
        for result in result_list[:-1]:
            if result.isdigit(): 
                message += '{0} | '.format(result)
        if result_list[-1].isdigit():
            message += '{0}\n'.format(result_list[-1])
        else:
            message += '\n'
    else:
        message += '\n'
    return message

def display_xsmb_result(viber, uid, xsmb_result):
    message  = '*XỔ SỐ MIỀN BẮC {0} {1}*\n'.format(get_weekday_translation(xsmb_result.ngay_trao_giai), xsmb_result.ngay_trao_giai.strftime('%d/%m/%y'))
    message += '=====================\n'
    if xsmb_result.giai_dac_biet: 
        xsmb_result.giai_dac_biet.sort()
        message += 'Đặc biệt: *{0}*\n'.format(xsmb_result.giai_dac_biet[0])
    if xsmb_result.giai_nhat:
        xsmb_result.giai_nhat.sort()
        message += 'Giải nhất: {0}\n'.format(xsmb_result.giai_nhat[0])
    if xsmb_result.giai_nhi:
        message += 'Giải nhì: '
        xsmb_result.giai_nhi.sort()
        for result in xsmb_result.giai_nhi[:-1]:
            message += '{0} | '.format(result)
        message += '{0}\n'.format(xsmb_result.giai_nhi[-1])
    if xsmb_result.giai_ba:
        message += 'Giải ba: '
        xsmb_result.giai_ba.sort()
        for result in xsmb_result.giai_ba[:-1]:
            message += '{0} | '.format(result)
        message += '{0}\n'.format(xsmb_result.giai_ba[-1])
    if xsmb_result.giai_tu:
        message += 'Giải tư: '
        xsmb_result.giai_tu.sort()
        for result in xsmb_result.giai_tu[:-1]:
            message += '{0} | '.format(result)
        message += '{0}\n'.format(xsmb_result.giai_tu[-1])
    if xsmb_result.giai_nam:
        message += 'Giải năm: '
        xsmb_result.giai_nam.sort()
        for result in xsmb_result.giai_nam[:-1]:
            message += '{0} | '.format(result)
        message += '{0}\n'.format(xsmb_result.giai_nam[-1])
    if xsmb_result.giai_sau:
        message += 'Giải sáu: '
        xsmb_result.giai_sau.sort()
        for result in xsmb_result.giai_sau[:-1]:
            message += '{0} | '.format(result)
        message += '{0}\n'.format(xsmb_result.giai_sau[-1])
    if xsmb_result.giai_bay:
        message += 'Giải bảy: '
        xsmb_result.giai_bay.sort()
        for result in xsmb_result.giai_bay[:-1]:
            message += '{0} | '.format(result)
        message += '{0}\n'.format(xsmb_result.giai_bay[-1])

    message_chinh = message

    message  = 'Đầu lô tô\n'
    message += '0: '
    message = append_loto_field_display(message, xsmb_result.dau_lo_to_dau0)
    
    message += '1: '
    message = append_loto_field_display(message, xsmb_result.dau_lo_to_dau1)

    message += '2: '
    message = append_loto_field_display(message, xsmb_result.dau_lo_to_dau2)

    message += '3: '
    message = append_loto_field_display(message, xsmb_result.dau_lo_to_dau3)

    message += '4: '
    message = append_loto_field_display(message, xsmb_result.dau_lo_to_dau4)

    message += '5: '
    message = append_loto_field_display(message, xsmb_result.dau_lo_to_dau5)

    message += '6: '
    message = append_loto_field_display(message, xsmb_result.dau_lo_to_dau6)

    message += '7: '
    message = append_loto_field_display(message, xsmb_result.dau_lo_to_dau7)

    message += '8: '
    message = append_loto_field_display(message, xsmb_result.dau_lo_to_dau8)

    message += '9: '
    message = append_loto_field_display(message, xsmb_result.dau_lo_to_dau9)

    message_dau_lo_to = message 


    message  = 'Đuôi lô tô\n'
    message += '0: '
    message = append_loto_field_display(message, xsmb_result.duoi_lo_to_dau0)

    message += '1: '
    message = append_loto_field_display(message, xsmb_result.duoi_lo_to_dau1)

    message += '2: '
    message = append_loto_field_display(message, xsmb_result.duoi_lo_to_dau2)

    message += '3: '
    message = append_loto_field_display(message, xsmb_result.duoi_lo_to_dau3)

    message += '4: '
    message = append_loto_field_display(message, xsmb_result.duoi_lo_to_dau4)

    message += '5: '
    message = append_loto_field_display(message, xsmb_result.duoi_lo_to_dau5)

    message += '6: '
    message = append_loto_field_display(message, xsmb_result.duoi_lo_to_dau6)

    message += '7: '
    message = append_loto_field_display(message, xsmb_result.duoi_lo_to_dau7)

    message += '8: '
    message = append_loto_field_display(message, xsmb_result.duoi_lo_to_dau8)

    message += '9: '
    message = append_loto_field_display(message, xsmb_result.duoi_lo_to_dau9)
    message_cuoi_lo_to = message 

    message  = 'Kép: '
    message = append_loto_field_display(message, xsmb_result.ket_qua_kep)
    message_kep = message

    viber.send_messages(
        to=uid, 
        messages=[
            TextMessage(text=message_chinh),
            TextMessage(text=message_dau_lo_to),
            TextMessage(text=message_cuoi_lo_to),
            TextMessage(text=message_kep),
        ]
    )


def display_bot_notification(viber, uid, notification): 
    viber.send_messages(
        to=uid, 
        messages=[
            TextMessage(text=notification.get_message()),
        ]
    )

def display_message_function(viber, uid, message:str):
    viber.send_messages(
        to=uid, 
        messages=[
            TextMessage(text=message),
        ]
    )

def display_xsmb_good_number_today(viber, uid, xsmb_so_dep:XSMB_So_Dep):
    today = django.utils.timezone.now().date()

    message  = '*Số đẹp hôm nay, {0} {1}*\n'.format(get_weekday_translation(today), today.strftime('%d/%m/%y'))
    message += '=====================\n'
    message += '🔥 Bạch thủ\n'
    message += '💰 Đầu đuôi giải đặc biệt: *{0}*\n'.format(' - '.join(xsmb_so_dep.dau_duoi_giai_dac_biet))
    #message += '💰 Lô tô 2 số đẹp: {0}\n'
    #message += '💰 Lô tô xiên 2, xiên 3: {0}\n'
    message += '💰 Lô tô kép: {0}\n'.format(' - '.join(xsmb_so_dep.lo_to_kep))
    message += '=====================\n'
    for dau_cam in xsmb_so_dep.dau_cam_hom_qua:
        message += 'Đầu câm hôm qua: {0}\n'.format(dau_cam)
        message += '💰 Số đẹp: {0}\n'.format(' - '.join(xsmb_so_dep.dau_cam_dep[dau_cam]))
    
    for duoi_cam in xsmb_so_dep.duoi_cam_hom_qua:
        message += 'Đuôi câm hôm qua: {0}\n'.format(duoi_cam)
        message += '💰 Số đẹp: {0}\n'.format(' - '.join(xsmb_so_dep.duoi_cam_dep[duoi_cam]))

    display_message_function(viber, uid, message)
    return True 

def display_number_statistic(viber, uid, number_stat:XSMB_Number_Statistic, display_header=True, start=0):
    """
        @Return:
            0: false 
            1: continue display
            2: ok 
            
    """
    MAX_OCCURENCE_PER_MESSAGE = 20

    if display_header:
        message  = '{0} - {1}\n'.format(number_stat.from_date.strftime('%d/%m/%Y'), number_stat.to_date.strftime('%d/%m/%Y'))
        message += 'Số *{0}* xuất hiện {1} lần\n'.format(number_stat.number, number_stat.number_freq)
        message += '=====================\n'
    else:
        message = ''

    length = len(number_stat.occurrences)
    count = start 
    while (count < length):
        occurence = number_stat.occurrences[count]
        count += 1
        message += '{0} | {1} | {2:^8}\n'.format(occurence['number'].ljust(6, ' '), occurence['giai'].ljust(9, ' '), occurence['date'].strftime('%d/%m/%y'))

        if count % MAX_OCCURENCE_PER_MESSAGE == 0:
            display_message_function(viber, uid, message=message)

            display_message_function(viber, uid, message=BOT_FEATURE_6_CONTINUE_DISPLAY.format(length - count))
            display_yes_no_command_keyboard(viber, uid)
            return 1, count 
    
    display_message_function(viber, uid, message=message)
    return 2, count  

def display_loto_freq_statistic(viber, uid, result:XSMB_Quick_Statistic_Loto):
    # display lo to xuat hien nhieu nhat 
    message  = 'Lô tô xuất hiện nhiều nhất trong 60 kỳ quay gần nhất\n' 
    message += '=====================\n'
    count = 0
    result.lo_to_nhieu_nhat.sort(key=lambda x:x['count'], reverse=True)
    for lo_to in result.lo_to_nhieu_nhat:
        count += 1
        message += '*{0}* ({1})  '.format(lo_to['lo_to'], lo_to['count'])
        if count % 3 == 0:
            message += '\n'
    display_message_function(viber, uid, message)

    # display lo to xuat hien it nhat 
    message  = 'Lô tô xuất hiện ít nhất trong 60 kỳ quay gần nhất\n' 
    message += '=====================\n'
    count = 0
    for lo_to in result.lo_to_it_nhat:
        count += 1
        message += '*{0}* ({1})  '.format(lo_to['lo_to'], lo_to['count'])
        if count % 3 == 0:
            message += '\n'
    display_message_function(viber, uid, message)

    # display lo khan
    message  = 'Lô khan (các bộ số chưa xuất hiện từ 10 ngày trở lên)\n' 
    message += '=====================\n'
    count = 0
    for lo_to in result.lo_khan:
        count += 1
        message += '*{0}* ({1} ngày)  '.format(lo_to['lo_to'], lo_to['interval'])
        if count % 3 == 0:
            message += '\n'
    display_message_function(viber, uid, message)
    
    # display lo roi 
    message  = 'Các bộ số xuất hiện liên tiếp\n' 
    message += '=====================\n'
    count = 0
    for lo_to in result.lo_roi:
        count += 1
        message += '*{0}* ({1} ngày)  '.format(lo_to['lo_to'], lo_to['count'])
        if count % 3 == 0:
            message += '\n'
    display_message_function(viber, uid, message)

    # display thong ke dau so 
    message  = 'Thống kê số lần xuất hiện từng đầu số trong 60 ngày gần nhất\n' 
    message += '=====================\n'
    count = 0
    for dau_so in result.dau_so_freq:
        count += 1
        message += '*{0}* ({1})  '.format(dau_so[0], dau_so[1])
        if count % 3 == 0:
            message += '\n'
    display_message_function(viber, uid, message)

    # display thong ke duoi so 
    message  = 'Thống kê số lần xuất hiện từng đầu số trong 60 ngày gần nhất\n' 
    message += '=====================\n'
    count = 0
    for duoi_so in result.duoi_so_freq:
        count += 1
        message += '*{0}* ({1})  '.format(duoi_so[0], duoi_so[1])
        if count % 3 == 0:
            message += '\n'
    display_message_function(viber, uid, message)

    # display lo to ve nhieu nhat khi giai dac biet 
    message  = 'Lô tô về nhiều nhất ngày hôm sau khi giải đặc biệt về *{0}* trong vòng 5 năm gần đây\n'.format(result.giai_dac_biet_hom_qua)
    message += '=====================\n'
    count = 0
    for loto in result.lo_to_ve_nhieu_giai_dac_biet:
        count += 1
        message += '*{0}* ({1})  '.format(loto['lo_to'], lo_to['count'])
        if count % 3 == 0:
            message += '\n'
    display_message_function(viber, uid, message)

    # dipslay lo to ve nhieu nhat khi dau cam la x
    for dau_cam in result.lo_to_ve_nhieu_dau_cam:
        message  = 'Lô tô về nhiều nhất ngày hôm sau khi *đầu câm là {0}* trong vòng 5 năm gần đây\n'.format(dau_cam)
        message += '=====================\n'
        count = 0
        for loto in result.lo_to_ve_nhieu_dau_cam[dau_cam]:
            count += 1
            message += '*{0}* ({1})  '.format(loto['lo_to'], lo_to['count'])
            if count % 3 == 0:
                message += '\n'
        display_message_function(viber, uid, message)

    # dipslay lo to ve nhieu nhat khi duoi cam la x
    for duoi_cam in result.lo_to_ve_nhieu_duoi_cam:
        message  = 'Lô tô về nhiều nhất ngày hôm sau khi *đuôi câm là {0}* trong vòng 5 năm gần đây\n'.format(duoi_cam)
        message += '=====================\n'
        count = 0
        for loto in result.lo_to_ve_nhieu_duoi_cam[duoi_cam]:
            count += 1
            message += '*{0}* ({1})  '.format(loto['lo_to'], lo_to['count'])
            if count % 3 == 0:
                message += '\n'
        display_message_function(viber, uid, message)

    return True 

def display_giai_dac_biet_freq_statistic(viber, uid, result:XSMB_Quick_Statistic_Giai_Dac_Biet): 
    # hai so cuoi giac dac biet
    message  = '*Hai số cuối giải đặc biệt* Xổ Số Miền Bắc (truyền thống) trong 30 ngày gần đây\n' 
    message += '=====================\n'
    count = 0 
    for ket_qua in result.hai_so_cuoi_30:
        count += 1
        message += '{0} | *{1}*   '.format(ket_qua['day'], ket_qua['giai_dac_biet']) 
        if count % 2 == 0:
            message += '\n'
    
    display_message_function(viber, uid, message)

    # thong ke so cuoi giai dac biet
    message  = '*2 số cuối giải đặc biệt* về nhiều trong 365 ngày gần đây\n' 
    message += '=====================\n'
    count = 0 
    for ket_qua in result.hai_so_cuoi_365:
        count += 1
        message += '*{0}* ({1})  '.format(ket_qua[0], ket_qua[1]['count']) 
        if count % 3 == 0:
            message += '\n'
    
    display_message_function(viber, uid, message)

    # thong ke dau so cuoi giai dac biet
    message  = '*Đầu 2 số cuối giải đặc biệt* về nhiều trong 365 ngày gần đây\n' 
    message += '=====================\n'
    count = 0 
    for ket_qua in result.dau_so_cuoi_365:
        count += 1
        message += '*{0}* ({1})  '.format(ket_qua[0], ket_qua[1]) 
        if count % 3 == 0:
            message += '\n'
    
    display_message_function(viber, uid, message)

    # thong ke duoi so cuoi giai dac biet
    message  = '*Đuôi 2 số cuối giải đặc biệt* về nhiều trong 365 ngày gần đây\n' 
    message += '=====================\n'
    count = 0 
    for ket_qua in result.duoi_so_cuoi_365:
        count += 1
        message += '*{0}* ({1})  '.format(ket_qua[0], ket_qua[1]) 
        if count % 3 == 0:
            message += '\n'
    
    display_message_function(viber, uid, message)

    # thong ke giai dac biet lau chua ve
    message  = '2 số cuối giải đặc biệt *lâu về nhất*\n' 
    message += '=====================\n'
    count = 0 
    for ket_qua in result.hai_so_cuoi_lau_ve_365:
        count += 1
        message += '*{0}* ({1} ngày)  '.format(ket_qua['giai_dac_biet'], ket_qua['interval']) 
        if count % 3 == 0:
            message += '\n'
    
    display_message_function(viber, uid, message)

    # thong ke giai dac biet ve lau nhat 
    message  = 'Giải đặc biệt về nhiều nhất ngày hôm sau khi giải đặc biệt về *{0}* trong vòng 5 năm gần đây\n'.format(result.giai_db_hom_qua) 
    message += '=====================\n'
    count = 0 
    for ket_qua in result.giai_db_ve_nhieu_nhat_hom_sau:
        count += 1
        message += '*{0}* ({1})  '.format(ket_qua[0], ket_qua[1]) 
        if count % 3 == 0:
            message += '\n'
    
    display_message_function(viber, uid, message)

def display_share_bot_information(viber, uid):
    qr_code_message = PictureMessage(
        media = BOT_FEATURE_7_QR_URL, 
        # text = BOT_FEATURE_7_QR_TEXT
    )

    message = 'Giới thiệu bạn bè sử dụng bot\n'
    message += '=====================\n'
    message += '🔥 Hướng dẫn chia sẻ & mở khóa tính năng:\n'
    message += '💰 B1: copy tin nhắn này, ấn Chia sẻ/Forward trên Viber\n'
    message += '💰 B2: chọn bạn bè muốn giới thiệu và ấn Gửi\n'
    message += '💰 B3: các tính năng cao cấp sẽ tự động được mở khóa\n'
    message += '\n'
    message += '🔥 Hướng dẫn mở bot:\n'
    message += '💰 B1: click vào đường link viber://pa?chatURI=ketquaxsmb\n'
    message += '💰 B2: bot XSMB tự động mở ra trên Viber\n'
    message += '💰 B3: chat theo hướng dẫn của bot để bắt đầu sử dụng\n'
    message += '\n'
    message += '🔥 Lưu ý: quét mã QR Code nếu bot không tự động mở khi ấn vào link\n'

    viber.send_messages(
        to=uid, 
        messages=[
            TextMessage(text=message),
            qr_code_message, 
        ]
    )

def display_require_unlock_feature(viber, uid):
    message = BOT_MESSAGES['REQUIRE_UNLOCK_FEATURE_MESSAGE']

    viber.send_messages(
        to=uid, 
        messages=[
            TextMessage(text=message),
            KeyboardMessage(keyboard=BOT_FEATURE_7_SHARE_BOT_COMMAND)
        ]
    )

def display_unlock_feature_successfully(viber, uid):
    message = BOT_MESSAGES['UNLOCK_FEATURE_SUCCESSFUL_MESSAGE']

    viber.send_messages(
        to=uid, 
        messages=[
            TextMessage(text=message),
        ]
    )