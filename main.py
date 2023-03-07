from app.menu import Menu
from app.utils import delete_file

if __name__ == "__main__":
    delete_file(file="data/events.json")
    menu = Menu()
    menu.main_menu()
