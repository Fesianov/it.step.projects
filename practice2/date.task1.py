from datetime import datetime, timedelta

def calculator(start, duration):
    start_date = datetime.strptime(start, '%Y-%m-%d %H:%M')
    arrival_date = start_date + timedelta(hours=duration)
    return arrival_date.strftime('%Y-%m-%d %H:%M')

user_start = input('Enter start date (example: 2024-12-09 19:00): ')
overall_duration = float(input('Enter duration (example: 3.5): '))
result = calculator(user_start, overall_duration)
print(f'Arrival time: {result}')