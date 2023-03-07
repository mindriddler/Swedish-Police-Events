import json
import requests


class DataHandler:
    def __init__(self) -> None:
        self.data = self.get_data()
        self.save_data_to_json()

    def get_all_data_from_json(self):
        return self.data

    def get_latest_data_from_json(self):
        data = self.make_data_pretty(data=self.data[0])
        return data

    def get_events_by_argument(self, filter):
        num_of_events = 0
        if filter == "location":
            location = input("Enter location: ")
            for event in self.data:
                if event["location"]["name"] == location:
                    num_of_events += 1
            print(f"The number of events in {location} is {num_of_events}")
            choice = input("Do you want to display them all?: ")
            if choice == "yes":
                formated_events = []
                for event in self.data:
                    if event["location"]["name"] == location:
                        formated = self.make_data_pretty(event)
                        formated_events.append(formated)
                return formated_events
            else:
                return
        elif filter == "date":
            date = input("Enter date: ")
            for event in self.data:
                if event["datetime".split(" ")] == date:
                    num_of_events += 1
            print(f"The number of events on {date} is {num_of_events}")
            choice = input("Do you want to display them all?: ")
            if choice == "yes":
                formated_events = []
                for event in self.data:
                    if event["datetime"] == date:
                        formated = self.make_data_pretty(event)
                        formated_events.append(formated)
                return formated_events
            else:
                return
        elif filter == "type":
            type = input("Enter type: ")
            for event in self.data:
                if event["type"] == type:
                    num_of_events += 1
            print(f"The number of events of type {type} is {num_of_events}")
            choice = input("Do you want to display them all?: ")
            if choice == "yes":
                formated_events = []
                for event in self.data:
                    if event["type"] == type:
                        formated = self.make_data_pretty(event)
                        formated_events.append(formated)
                return formated_events
            else:
                return
        else:
            print("Invalid filter")

    def get_specific_number_of_events(self, num_of_events):
        list_of_events = []
        formated_events = []
        for event in self.data:
            if num_of_events == 0:
                break
            else:
                list_of_events.append(event)
                num_of_events -= 1
        for event in list_of_events:
            formated = self.make_data_pretty(event)
            formated_events.append(formated)
        return formated_events

    def make_data_pretty(self, data):
        date = "\nTime and date: " + data["datetime"]
        location = "Location: " + data["location"]["name"]
        gps = "GPS coordinates: " + data["location"]["gps"]
        summary = "Summary: " + data["summary"]
        type = "Type: " + data["type"]
        url = "URL: " + "https://polisen.se" + data["url"]

        return (date, location, gps, summary, type, url)

    def save_data_to_json(self):
        print("Saving data to 'data/events.json' file")
        with open("data/events.json", "w", encoding="UTF-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
        f.close()

    def get_data(self):
        print("Getting data from polisens API")
        response_api = requests.get("https://polisen.se/api/events")
        return response_api.json()
