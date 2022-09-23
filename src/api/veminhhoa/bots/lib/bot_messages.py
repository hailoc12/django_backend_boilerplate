import os

BOT_FEATURE_1_TEXT = 'Kết quả mới nhất'
BOT_FEATURE_1_STEP_CODES = [
    {'code': '00', 
    'step_name': ''},
]

BOT_FEATURE_2_TEXT = 'Tra kết quả theo ngày'
BOT_FEATURE_2_STEP_CODES = [
    {'code': '00', 
    'step_name': 'ask for date'},
    {'code': '01', 
    'step_name': 'got input date'},
]
BOT_FEATURE_2_ASK_FOR_DATE_INPUT = 'Nhập ngày theo định dạng:\nNgày/Tháng/Năm\nVí dụ: 12/05/2022'
BOT_FEATURE_2_INVALID_DATE_INPUT = 'Dữ liệu sai định dạng'
BOT_FEATURE_2_FAIL_TO_GET_RESULT = 'Rất tiếc! Bot không có kết quả cho ngày này'

BOT_FEATURE_3_TEXT = 'Thống kê nhanh'
BOT_FEATURE_3_STEP_CODES = [
    {'code': '00', 
    'step_name': 'ask for statistic type'},
    {'code': '01', 
    'step_name': 'display feature 1 result'},
    {'code': '02', 
    'step_name': 'continue display feature 1 result'},
]

BOT_FEATURE_3_ASK_FOR_STATISTIC_TYPE_INPUT = 'Chọn loại thống kê'
BOT_FEATURE_3_INVALID_STATISTIC_TYPE_INPUT = 'Loại thống kê không hợp lệ'
BOT_FEATURE_3_STATISTIC_TYPE_1 = 'Tần suất lô tô'
BOT_FEATURE_3_STATISTIC_TYPE_2 = 'Giải đặc biệt'
BOT_FEATURE_3_STATISTIC_TYPE_EXIT = 'Quay trở lại'



BOT_FEATURE_3_STATISTIC_TYPE_KEYBOARD_COMMAND = {
        "Type": "keyboard",
        "Buttons": [{
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_3_STATISTIC_TYPE_1}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_3_STATISTIC_TYPE_1}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/9tncn0r85/sushi.png"
        }, {
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_3_STATISTIC_TYPE_2}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_3_STATISTIC_TYPE_2}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/ntpef5syd/french.png"
        }, 
        {
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_3_STATISTIC_TYPE_EXIT}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_3_STATISTIC_TYPE_EXIT}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/ntpef5syd/french.png"
        }, 
        ]
    }


BOT_FEATURE_4_TEXT = 'Số đẹp hôm nay'
BOT_FEATURE_4_STEP_CODES = [
    {'code': '00', 
    'step_name': 'ask for today lucky numbers'},
]
#BOT_FEATURE_5_TEXT = 'Vietlott'
BOT_FEATURE_6_TEXT = 'Dò kết quả'
BOT_FEATURE_6_STEP_CODES = [
    {'code': '00', 
    'step_name': 'ask for date range'},
    {'code': '01', 
    'step_name': 'ask for number'},
    {'code': '02', 
    'step_name': 'got number'},
    {'code': '03', 
    'step_name': 'continue_displaying'},
]
BOT_FEATURE_6_ASK_FOR_DATE_RANGE_INPUT = 'Lựa chọn khoảng thời gian dò kết quả'
BOT_FEATURE_6_ASK_FOR_NUMBER_INPUT = 'Nhập số cần dò'
BOT_FEATURE_6_INVALID_DATE_RANGE_INPUT = 'Khoảng thời gian dò kết quả không hợp lệ'
BOT_FEATURE_6_INVALID_NUMBER_INPUT = 'Số cần dò không hợp lệ'
BOT_FEATURE_6_CAN_NOT_CALCULATE_NUMBER_STATISTIC = 'Không có giải nào về {0} trong {1} qua'
BOT_FEATURE_6_CONTINUE_DISPLAY = 'Bạn có muốn tiếp tục hiển thị {0} lần xuất hiện còn lại ?'

BOT_FEATURE_6_DATE_RANGE_1 = '1 tuần qua'
BOT_FEATURE_6_DATE_RANGE_1_VALUE = 7
BOT_FEATURE_6_DATE_RANGE_1_UNIT = "day"
BOT_FEATURE_6_DATE_RANGE_2 = '1 tháng qua'
BOT_FEATURE_6_DATE_RANGE_2_VALUE = 1
BOT_FEATURE_6_DATE_RANGE_2_UNIT = "month"
BOT_FEATURE_6_DATE_RANGE_3 = '2 tháng qua'
BOT_FEATURE_6_DATE_RANGE_3_VALUE = 2
BOT_FEATURE_6_DATE_RANGE_3_UNIT = "month"
BOT_FEATURE_6_DATE_RANGE_4 = '3 tháng qua'
BOT_FEATURE_6_DATE_RANGE_4_VALUE = 3
BOT_FEATURE_6_DATE_RANGE_4_UNIT = "month"
BOT_FEATURE_6_DATE_RANGE_5 = '1 năm qua'
BOT_FEATURE_6_DATE_RANGE_5_VALUE = 1
BOT_FEATURE_6_DATE_RANGE_5_UNIT = "year"
BOT_FEATURE_6_DATE_RANGE_6 = '2 năm qua'
BOT_FEATURE_6_DATE_RANGE_6_VALUE = 2
BOT_FEATURE_6_DATE_RANGE_6_UNIT = "year"

BOT_FEATURE_6_DATE_RANGE_KEYBOARD_COMMAND = {
        "Type": "keyboard",
        "Buttons": [{
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_6_DATE_RANGE_1}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_6_DATE_RANGE_1}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/9tncn0r85/sushi.png"
        }, {
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_6_DATE_RANGE_2}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_6_DATE_RANGE_2}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/ntpef5syd/french.png"
        }, {
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_6_DATE_RANGE_3}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_6_DATE_RANGE_3}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/t8y4g4kid/mexican.png"
        }, {
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_6_DATE_RANGE_4}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_6_DATE_RANGE_4}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/x41iip3o5/itallian.png"
        }, {
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_6_DATE_RANGE_5}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_6_DATE_RANGE_5}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/wq06j3jkl/indi.png"
        }
        , {
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_6_DATE_RANGE_6}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_6_DATE_RANGE_6}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/wq06j3jkl/indi.png"
        }
        ]
    }


BOT_FEATURE_7_TEXT = 'Chia sẻ bot'
BOT_FEATURE_7_STEP_CODES = [
    {'code': '00', 
    'step_name': 'ask for date range'},
]

BOT_FEATURE_7_QR_URL = os.environ.get('DJANGO_HOST') + '/static/images/qr_code/free_xsmb_bot.jpg'
BOT_FEATURE_7_QR_TEXT = 'XSMB QRCode'

BOT_FEATURE_7_SHARE_BOT_COMMAND = {
        "Type": "keyboard",
        "Buttons": [{
            "Columns": 6,
            "Rows": 2,
            "Text": "<br><font color=\"#494E67\"><b>Chia sẻ ngay</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_7_TEXT}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/9tncn0r85/sushi.png"
        }]
}


BOT_MESSAGES = {
    'FREE_VIBER_BOT_WELCOME': 'Chào mừng đến kênh Thông tin Xổ Số tiện lợi trên ứng dụng chat Viber. Hãy cho tôi biết tên của bạn?',
    'FREE_VIBER_BOT_AFTER_SUBCRIBE': 'Xin chào {0}. Bạn đã đăng ký sử dụng Xổ Số tiện lợi thành công. Gói tài khoản: miễn phí',
    'FREE_VIBER_BOT_START_COMMAND': 'Vui lòng chọn tính năng bạn muốn sử dụng!',
    'FREE_VIBER_BOT_UNRECOGNIZED_COMMAND': 'Câu lệnh {0} không khả dụng',
    'IN_DEVELOPMENT_FEATURE_MESSAGE': 'Tính năng này đang được phát triển. Xin mời quay lại sau', 
    'GUIDE_ON_AUTO_ALERT_FEATURE': f'Tin nhắn này được tự động gửi từ TTXSTL. Bạn có thể thay đổi tùy chọn nhận tin tự động trong mục "{BOT_FEATURE_7_TEXT}"',
    'REMIND_ON_RECEIVING_RESULT': 'Còn **{0}** nữa đến thời gian mở thưởng {1}.\n======================\nThời gian quay số bắt đầu lúc {2}',
    
    'PREMIUM_VIBER_BOT_WELCOME': 'Xin chào {0}! Chào mừng đến kênh Thông tin Xổ Số tiện lợi trên ứng dụng chat Viber',
    'FREE_VIBER_BOT_AFTER_SUBCRIBE': 'Xin chào {0}. Bạn đã đăng ký sử dụng Xổ Số tiện lợi thành công. Gói tài khoản: miễn phí',
    'PREMIUM_VIBER_BOT_START_COMMAND': 'Vui lòng chọn tính năng bạn muốn sử dụng!',
    'REQUIRE_UNLOCK_FEATURE_MESSAGE': f'Đây là tính năng cao cấp. Bạn cần "{BOT_FEATURE_7_TEXT}" để mở khóa chức năng này', 
    'UNLOCK_FEATURE_SUCCESSFUL_MESSAGE': 'Xin chúc mừng! Bạn đã mở khóa thành công các chức năng cao cấp của bot'
}

VIBER_COMMAND_KEYBOARD_START_USING_BOT = {
        "Type": "keyboard",
        "Buttons": [{
            "Columns": 6,
            "Rows": 2,
            "Text": "<br><font color=\"#494E67\"><b>Bắt đầu</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": "Bắt đầu",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/9tncn0r85/sushi.png"
        }]
}

YES_ANSWER = 'Có'
NO_ANSWER = 'Không'

YES_NO_COMMAND_BOARD = {
        "Type": "keyboard",
        "Buttons": [{
            "Columns": 3,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{YES_ANSWER}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{YES_ANSWER}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/9tncn0r85/sushi.png"
        }, 
        {
            "Columns": 3,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{NO_ANSWER}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{NO_ANSWER}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/9tncn0r85/sushi.png"
        }
        ]
}



VIBER_COMMAND_KEYBOARD_FREEUSER = {
        "Type": "keyboard",
        "Buttons": [{
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_1_TEXT}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_1_TEXT}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/9tncn0r85/sushi.png"
        }, {
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_2_TEXT}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_2_TEXT}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/ntpef5syd/french.png"
        }, {
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_3_TEXT}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_3_TEXT}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/t8y4g4kid/mexican.png"
        }, {
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_4_TEXT}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_4_TEXT}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/x41iip3o5/itallian.png"
        # }, {
        #     "Columns": 2,
        #     "Rows": 2,
        #     "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_5_TEXT}</b></font>",
        #     "TextSize": "large",
        #     "TextHAlign": "center",
        #     "TextVAlign": "middle",
        #     "ActionType": "reply",
        #     "ActionBody": f"{BOT_FEATURE_5_TEXT}",
        #     "BgColor": "#d4cdcd",
        #     #"Image": "https://s18.postimg.org/wq06j3jkl/indi.png"
        }, {
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_6_TEXT}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_6_TEXT}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/ylmyu98et/more_Options.png"
        },
        {
            "Columns": 2,
            "Rows": 2,
            "Text": f"<br><font color=\"#494E67\"><b>{BOT_FEATURE_7_TEXT}</b></font>",
            "TextSize": "large",
            "TextHAlign": "center",
            "TextVAlign": "middle",
            "ActionType": "reply",
            "ActionBody": f"{BOT_FEATURE_7_TEXT}",
            "BgColor": "#d4cdcd",
            #"Image": "https://s18.postimg.org/ylmyu98et/more_Options.png"
        }
        
        ]
    }