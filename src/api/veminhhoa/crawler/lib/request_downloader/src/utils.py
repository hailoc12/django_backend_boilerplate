import codecs
import datetime
import sys
import traceback
import re

def check_contain_filter(topic, contain_filter):
    '''
    function
    --------
    check if topic satisfiy contain_filters in format "a;b;c" means (a or b or c)
    :input:
        topic (string|list): string|list to search
    '''
    if isinstance(topic, list):
        content_string = [x.lower() for x in topic]
    else:
        content_string = topic.lower()
    search_string = contain_filter.lower()

    or_term_satisfy = False
    for or_term in search_string.split(';'):
        if or_term.strip() != '':
            if or_term.strip() in content_string: # current or_term is in search_string
                or_term_satisfy = True
                break

    return or_term_satisfy

def check_keyword_filter(document, main_keyword, support_keyword=None, exclude_keyword=None):
    """Filter document with keywords"""
    main_filter = check_contain_filter(document, main_keyword)

    if support_keyword:
        support_filter = check_contain_filter(document, support_keyword)
    else:
        support_filter = True
    
    if exclude_keyword:
        exlude_filter = check_contain_filter(document, exclude_keyword)
    else:
        exclude_filter = False
    
    return main_filter and support_filter and (not exclude_filter)




def open_utf8_file_to_read(filename):
    try:
        return codecs.open(filename, "r", "utf-8")
    except:
        return None


def open_utf8_file_to_write(filename):
    try:
        return codecs.open(filename, "w+", "utf-8")
    except:
        return None

def print_exception():
    # Print error message in try..exception
    exec_info = sys.exc_info()
    traceback.print_exception(*exec_info)

def try_to_parse_date_from_text(publish_date):
    re_list = [
        '(\d{1,2} thg \d{1,2}, \d{2,4})'
    ]

    fmt_list = [
        '%d thg %m, %Y'
    ]

    total = len(re_list)
    for i in range(0, total):
        try:
            match = re.search(re_list[i], publish_date)
            if match:
                date_group = str(match.group(1))
                date = datetime.datetime.strptime(date_group, fmt_list[i])
                return date
        except:
            pass
    
    return None

def get_time_from_uri(api_uri):
    start_time = None
    end_time = None
    try:
        start_str = ''
        end_str = ''
        if api_uri.find('start-date') != 1:
            start_match = re.search('start-date=(.+?)&end-date=', api_uri)
            if start_match:
                start_str = start_match.group(1)
            end_match = re.search(r'(?<=end-date=)[^.\s]*', api_uri)
            if end_match:
                end_str = end_match.group(0)
        if end_str != '' and start_str == '':
            start_str = '1010-10-10'
        if start_str != '':
            start_time = datetime.datetime.strptime(start_str, '%Y-%m-%d')
        if end_str != '':
            end_time = datetime.datetime.strptime(end_str, '%Y-%m-%d')
    except:
        print('input date error')
    return (start_time, end_time)