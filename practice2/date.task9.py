from datetime import datetime, timedelta

def working_hours(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

    work_start_time = start.replace(hour=9, minute=0, second=0, microsecond=0)
    work_end_time = start.replace(hour=18, minute=0, second=0, microsecond=0)

    if start > end:
        start, end = end, start

    total_work_hours = 0

    while start < end:
        if start.weekday() < 5:
            if start.date() == end.date():
                total_work_hours += (end - start).seconds / 3600
                break
            else:
                total_work_hours += (work_end_time - work_start_time).seconds / 3600
        start = (start + timedelta(days=1)).replace(hour=9, minute=0, second=0, microsecond=0)
    return total_work_hours


start_date = input("Enter starting date and time(in format: YYYY-MM-DD HH:MM:SS): ")
end_date = input("Enter ending date and time(in format: YYYY-MM-DD HH:MM:SS): ")

try:
    result = working_hours(start_date, end_date)
    print(f"Amount of working hours between those dates: {result}")
except ValueError as e:
    print(f"Error: {e}")