import requests
import re
from beaupy import prompt


class DataHandler:
    def __init__(self, console) -> None:
        self.console = console

    def make_api_call(self, event_type=None, filter=None):
        self.console.print("Getting data from polisens API", style="bold green")
        if event_type != None:
            self.console.print(
                f"Filtering data based on",
                style="bold green",
            )
            self.console.print(f"   - event type: {event_type}", style="yellow")
            self.console.print(f"   - filter: {filter}", style="yellow")
            data = requests.get(
                f"https://polisen.se/api/events?{event_type}={filter}"
            ).json()
            return [self.make_data_pretty(event) for event in data]
        data = requests.get("https://polisen.se/api/events").json()
        return [self.make_data_pretty(event) for event in data]

    def make_data_pretty(self, data):
        pretty_data = {
            "ID": data["id"],
            "Time and date": data["datetime"],
            "Location": data["location"]["name"],
            "GPS coordinates": data["location"]["gps"],
            "Summary": (
                "No summary available"
                if "Efter klockan" in data["summary"]
                else data["summary"]
            ),
            "Type": data["type"],
            "URL": "https://polisen.se" + data["url"],
        }

        return pretty_data

    def display_events(self):
        self.console.print("Displaying all events", style="bold green")
        data = self.make_api_call()
        self.display_data(data)

    def display_latest_events(self):
        data = self.make_api_call()
        self.display_data(data, event_count=1)

    def display_specific_number_of_events(self):
        event_count = prompt(
            "How many events do you want to display?: ",
            target_type=int,
            validator=lambda count: count > 0,
        )
        data = self.make_api_call()
        self.display_data(data, event_count)

    def display_data(self, data, event_count=None):
        num_of_events_showed = 0
        for event in data:
            for key, value in event.items():
                self.console.print(f"{key}: {value}")
            self.console.print("\n")
            num_of_events_showed += 1
            if event_count and num_of_events_showed == event_count:
                self.console.print(
                    f"{num_of_events_showed} {'event' if event_count == 1 else 'events'} displayed",
                    style="bold green",
                )
                self.console.print("Going back to menu", style="bold red")
                break

    def filter_by_date(self):
        date = prompt("Enter date: ")
        if (
            re.match(r"^\d{4}$", date)
            or re.match(r"^\d{4}-\d{2}$", date)
            or re.match(r"^\d{4}-\d{2}-\d{2}$", date)
        ):
            data = self.make_api_call(event_type="datetime", filter=date)
            self.display_data(data)
        else:
            self.console.print("Invalid date", style="bold red")
            self.console.print(100 * "-")

    def filter_by_location(self):
        location = prompt("Enter location: ")
        data = self.make_api_call(event_type="locationname", filter=location)
        self.display_data(data)
