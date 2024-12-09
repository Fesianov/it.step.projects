from datetime import datetime, timedelta

def monday_cnt(start, end):
    start_date = datetime.strptime(start, '%d.%m.%Y')
    end_date = datetime.strptime(end, '%d.%m.%Y')

    every_monday = (7-start_date.weekday())%7
    start_monday = start_date + timedelta(days=every_monday)

    mondays = []
    today = start_monday
    while today <= end_date:
        mondays.append(today.strftime('%d.%m.%Y'))
        today += timedelta(days=7)
    return mondays

start = input('Enter start date (example: 09.12.2024): ')
end = input('Enter end date (example: 09.12.2024): ')
result = monday_cnt(start, end)
print('Monday dates: ')
for monday in result:
    print(monday)