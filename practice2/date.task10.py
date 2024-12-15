from datetime import datetime

calendar_events = {}


def add_event(date, event):
    if date not in calendar_events:
        calendar_events[date] = []
    calendar_events[date].append(event)
    print(f"Event '{event}' added to date {date}.")


def display_events(date):
    if date in calendar_events and calendar_events[date]:
        print(f"Events on {date}:")
        for idx, event in enumerate(calendar_events[date], start=1):
            print(f"{idx}. {event}")
    else:
        print(f"No events on {date}.")


def main():
    while True:
        print("\nMenu:")
        print("1. Add event")
        print("2. Display events")
        print("3. Exit")

        choice = input("Enter an option(1-3): ")

        if choice == '1':
            date = input("Enter date of event(in format YYYY-MM-DD): ")
            try:
                datetime.strptime(date, '%Y-%m-%d')
                event = input("Event: ")
                add_event(date, event)
            except ValueError:
                print("Wrong format.")
        elif choice == '2':
            date = input("Enter date to display events(in format YYYY-MM-DD): ")
            try:
                datetime.strptime(date, '%Y-%m-%d')
                display_events(date)
            except ValueError:
                print("Wrong format.")
        elif choice == '3':
            print("Exit")
            break
        else:
            print("There is no such an option.")


main()