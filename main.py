import os
import requests
import json


def save_data_to_json(data):
    print("Saving data to 'events.json' file")
    with open("events.json", "w", encoding="UTF-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    f.close()


def get_data():
    print("Getting data from polisens API")
    response_api = requests.get("https://polisen.se/api/events")

    data = response_api.json()
    save_data_to_json(data)


def get_events_by_location(location):
    num_of_events = 0

    with open("events.json", "r", encoding="UTF-8") as f:
        data = json.load(f)

    for event in data:
        if event["location"]["name"] == location:
            num_of_events += 1
    print(f"The number of events in {location} is {num_of_events}")
    choice = input("Do you want to display them all?: (yes/no)")
    if choice == "yes":
        for event in data:
            if event["location"]["name"] == location:
                print(event)
    else:
        return


def sub_menu():
    running = True

    while running:
        print(
            """
1. Show all events in specific location
2. Show all events on specific date
3. Show all events on specific type
4. Back to main menu
"""
        )
        choice = int(input("Enter your choice: "))
        if choice == 1:
            location = input("Enter location: ")
            get_events_by_location(location)


def main_menu():
    running = True
    while running:
        print(
            """
Latest 500 Police events in Sweden.

1. Show all events
2. Show most recent event
3. Show specific number of events
4. More options
5. Exit"""
        )
        choice = int(input("Enter your choice: "))

        if choice == 1:
            confirmation = input(
                "It 500 events, are you sure you want to display them all?: (yes/no)"
            )
            if confirmation == "yes":
                get_events(num_of_events_to_display=500)
            else:
                pass
        elif choice == 2:
            num_of_events_to_display = 1
            get_events(num_of_events_to_display)
        elif choice == 3:
            num_of_events_to_display = int(
                input("How many events do you want to display?: ")
            )
            get_events(num_of_events_to_display)
        elif choice == 4:
            sub_menu()
        elif choice == 5:
            exit()


def delete_file(file):
    if os.path.exists(file):
        os.remove(file)
        print("Removed events.json")
    else:
        print("file not found")


if __name__ == "__main__":
    delete_file(file="events.json")
    get_data()
    main_menu()
