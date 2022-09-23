import datetime 

def get_weekday_translation(date):
    weekday = datetime.datetime.weekday(date)
    WEEKDAYS = {
        0: 'Thứ 2', 
        1: 'Thứ 3', 
        2: 'Thứ 4', 
        3: 'Thứ 5', 
        4: 'Thứ 6', 
        5: 'Thứ 7', 
        6: 'Chủ nhật', 
    }
    return WEEKDAYS[weekday]