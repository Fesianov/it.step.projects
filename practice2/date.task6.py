from datetime import datetime

def birthday_weekend_cnt(birthday, year):
    birth_date_year = f'{birthday}{year}'
    try:
        birth_datetime = datetime.strptime(birth_date_year, '%d.%m.%Y')
        if birth_datetime.weekday() == 5 or birth_datetime.weekday() == 6:
            return True
        return False
    except ValueError as VE:
        raise ValueError(f'Error: {VE}')

birthday = input('Enter birth date (example: 21.08.): ')
year = int(input('Enter year to check: '))

if birthday_weekend_cnt(birthday, year):
    print(f'Birthday {birthday} in {year} gonna be on weekend.')
else:
    print(f'Birthday {birthday} in {year} not gonna be in weekend.')