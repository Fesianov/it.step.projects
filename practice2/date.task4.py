from datetime import datetime

def calculator(birthday):
    birthday_date = datetime.strptime(birthday, '%Y-%m-%d')
    today = datetime.now()
    years = today.year - birthday_date.year
    months = today.month - birthday_date.month
    days = today.day - birthday_date.day

    if days < 0:
        months -= 1
        prev_month = (today.month - 1) % 12 or 12
        prev_month_days = (datetime(today.year, prev_month + 1, 1) - datetime(today.year if prev_month != 12 else today.year - 1, prev_month, 1)).days
        days += prev_month_days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

user_birthday = input('Enter day of birthday (example: 2024-12-09): ')
year, month, day = calculator(user_birthday)
print(f'Age: {year} years, {month} months, {day} days.')