import calendar

def calendar_generator(year, month):

    try:
        cal = calendar.TextCalendar()
        return cal.formatmonth(year, month)
    except calendar.IllegalMonthError:
        return "Month has to be in range 1-12."
    except ValueError:
        return "Year has to be 'int' number."


try:
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    print("\nText calendar:")
    print(calendar_generator(year, month))
except ValueError as e:
    print(f"Error: {e}")