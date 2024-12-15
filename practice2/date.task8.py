import time
from datetime import datetime

def countdown():
    target_date = input("Enter target date and time(in format: YYYY-MM-DD HH:MM): ")

    try:
        target = datetime.strptime(target_date, '%Y-%m-%d %H:%M')
    except ValueError:
        print("Wrong format of date and time, use 'YYYY-MM-DD HH:MM'.")
        return

    while True:
        now = datetime.now()
        time_left = target - now

        if time_left.total_seconds() <= 0:
            print("Time is out!")
            break

        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Left: {time_left.days} days, {hours} hours, {minutes} minutes")
        time.sleep(60)


countdown()