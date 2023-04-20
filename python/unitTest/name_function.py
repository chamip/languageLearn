def get_formatted_name(first, last, middle=''):
    """给定名和姓，返回全名"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()