from pprint import pprint
from app.datahandler import DataHandler


class Menu:
    def __init__(self) -> None:
        self.dh = DataHandler()
        self.main_menu_running = True
        self.sub_menu_running = False

    def main_menu(self):
        while self.main_menu_running:
            print(
                """
Latest 500 Police events in Sweden.

1. Show all events
2. Show most recent event
3. Show specific number of events
4. Show events by filter
5. Exit"""
            )
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                confirmation = input(
                    "Its 500 events, are you sure you want to display them all?: "
                )
                if confirmation == "yes":
                    data = self.dh.get_all_data_from_json()
                    pprint(data)
                elif confirmation == "no":
                    continue
                else:
                    print("Invalid choice")
            elif choice == 2:
                data = self.dh.get_latest_data_from_json()
                for entry in data:
                    print(entry)
            elif choice == 3:
                num_of_events = int(input("Enter number of events: "))
                data = self.dh.get_specific_number_of_events(num_of_events)
                for event in data:
                    for entry in event:
                        print(entry)
            elif choice == 4:
                self.sub_menu_running = True
                self.sub_menu()
            elif choice == 5:
                exit()

    def sub_menu(self):
        while self.sub_menu_running:
            print(
                """
Available filters
Location
Date
Type"""
            )
            filter = input("By what parameter do you want to filter?: ").lower()
            data = self.dh.get_events_by_argument(filter)
            for event in data:
                for entry in event:
                    print(entry)
            choice = input("Do you want to do more searches based on filters?: ")
            if choice == "yes":
                continue
            elif choice == "no":
                self.sub_menu_running = False
