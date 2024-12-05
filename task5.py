from datetime import datetime

def days_cnt(date1, date2):
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    diff = abs((d2 - d1).days)
    return diff

date1 = input('Enter first date in format 2022-11-21: ')
date2 = input('Enter second date in format 2022-11-21: ')
result = days_cnt(date1, date2)
print(f'Days counter: {result}')