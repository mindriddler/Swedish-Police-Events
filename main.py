from app.utils import splash_screen, main_menu, filter_menu
from rich.console import Console
from beaupy import confirm, select
from app.datahandler import DataHandler


class Menu:

    def __init__(self, console) -> None:
        self.console = console
        self.dh = DataHandler(console=console)
        self.main_menu_running = True
        self.sub_menu_running = False

    def run(self):
        self.console.print(100 * "-")
        self.console.print(f"{main_menu()}", style="bold green")
        self.console.print(100 * "-")
        try:
            while self.main_menu_running:
                menu_choices = [
                    "Display all events (500 events)",
                    "Display latest events",
                    "Display specific number of events",
                    "Filter events",
                    "Exit",
                ]
                choice = select(menu_choices,
                                cursor=">",
                                cursor_style="bold blue",
                                cursor_index=0)
                if "Display all events" in choice:
                    if confirm("Are you sure you want to display all events?"):
                        self.dh.display_events()
                elif "Display latest events" in choice:
                    self.dh.display_latest_events()
                elif "Display specific number of events" in choice:
                    self.dh.display_specific_number_of_events()
                elif "Filter events" in choice:
                    self.sub_menu_running = True
                    self.sub_menu()
                elif "Exit" in choice:
                    self.console.print("Exiting program", style="bold red")
                    self.main_menu_running = False
        except TypeError:
            self.console.print("Exiting program", style="bold red")

    def sub_menu(self):
        try:
            self.console.print(100 * "-")
            self.console.print(f"{filter_menu()}", style="bold green")
            self.console.print(100 * "-")
            while self.sub_menu_running:
                menu_choices = [
                    "Date",
                    "Type",
                    "Location",
                    "Back",
                ]
                choice = select(menu_choices,
                                cursor=">",
                                cursor_style="bold blue",
                                cursor_index=0)
                if choice == "Date":
                    self.dh.filter_by_date()
                elif choice == "Type":
                    self.console.print(
                        "This filter seems to be broken at the API level. Not much i can do about it sadly.",
                        style="bold red",
                    )
                elif choice == "Location":
                    self.dh.filter_by_location()
                elif choice == "Back":
                    self.console.print("Going back to main menu",
                                       style="bold red")
                    self.console.print(100 * "-")
                    self.sub_menu_running = False
        except TypeError:
            self.console.print("Exiting program", style="bold red")
            self.main_menu_running = False
            self.sub_menu_running = False


if __name__ == "__main__":
    console = Console()
    console.print(100 * "-")
    console.print(splash_screen())
    menu = Menu(console=console)
    menu.run()
