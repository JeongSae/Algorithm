import datetime

def solution(a, b):
    answer = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    date = datetime.date(2016, a, b)

    return answer[date.weekday()]